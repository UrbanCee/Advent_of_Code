#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <numeric>
#include <cmath>

class Nmbrs
{
public:
    Nmbrs(const std::string &inputLine)
    {
        std::istringstream in(inputLine);
        in >> result;
        char delimiter;
        in >> delimiter;
        while (!in.eof())
        {
            operands.push_back(0);
            in >> operands.back();
        }
    }
    long long result;
    std::vector<long long> operands;

    void print()
    {
        std::cout << result << ":";
        for (auto &&value : operands)
        {
            std::cout << " " <<value;
        }
        std::cout << std::endl;
    }

    bool checkOperators(int operators, int base) const //0 ... add      1 ... mult         2 ... ||
    {
        auto operatorAddition = [&operators,base](long long result, long long operand){
                int currOp = operators;
                operators /= base;
                switch (currOp % base)
                {
                case 2:
                {
                    long long operand_=operand;
                    do{
                        result*=10;
                    }while(operand_/=10);
                    return result+operand;
                }
                case 1:
                    return result*operand;
                default:
                    return result+operand;
                }
        };
        return result == std::accumulate(std::next(operands.cbegin()),operands.cend(),operands.at(0),operatorAddition);
    }

    void printOperatorCalculation(int operators, int base) const
    {
        std::cout << result << "=";
        auto operatorOutput = [&operators,base](long long operand){
            int currOp = operators;
            operators /= base;
            switch (currOp % base)
            {
            case 2:
                std::cout << "||" << operand;
                break;
            case 1:
                std::cout << "*" << operand;
                break;
            default:
                std::cout << "+" << operand;
            }
        };
        std::cout << operands.at(0);
        std::for_each(std::next(operands.cbegin()),operands.cend(),operatorOutput);
        std::cout << std::endl;
    }

    std::vector<int> getValidOperatorList(int base)
    {
        std::vector<int> operatorList;
        for (int i=0;i<pow(base,operands.size()-1);i++)
        {
            if (checkOperators(i,base)){
                //printOperatorCalculation(i,base);
                operatorList.push_back(i);
            }
        }
        return operatorList;
    }
};



long long day7(int subtask)
{
    std::ifstream inputFile(std::filesystem::path("../../inputs/day7.txt"));
    long long result = 0;
    for (std::string line; std::getline(inputFile,line);)
    {
        Nmbrs number(line);
        if (!number.getValidOperatorList(1+subtask).empty())
        {
            result+=number.result;
        }
    }
    return result;
}


