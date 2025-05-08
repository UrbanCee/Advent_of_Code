#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>
#include <unordered_map>

class Gate{
public:
    Gate(const std::string &in1,const std::string &in2,const std::string &out,const std::string &operation):in1(in1),in2(in2),out(out){
        if (operation=="AND") op = AND;
        else if (operation=="OR") op = OR;
        else op=XOR;
    }
    std::string in1;
    std::string in2;
    std::string out;
    enum OP{AND,OR,XOR} op;
    bool ready(){
        return registers.contains(in1) && registers.contains(in2);
    }
    bool calc(){
        if (!ready())
            return false;
        switch (op) {
        case AND:
            registers.insert({out,registers.at(in1)&registers.at(in2)});
            break;
        case OR:
            registers.insert({out,registers.at(in1)|registers.at(in2)});
            break;
        case XOR:
            registers.insert({out,registers.at(in1)^registers.at(in2)});
            break;
        }
        return true;
    }
    static std::string op2Str(OP op){
        switch(op){
        case AND:
            return "AND";
        case OR:
            return "OR";
        case XOR:
            return "XOR";
        }
    }
    static std::unordered_map<std::string,int> registers;
    static std::vector<Gate> gates;
    static long long calcTotal(){
        bool allCalculated=false;
        while(!allCalculated){
            allCalculated=true;
            for (auto &&gate:gates)
            {
                allCalculated=gate.calc() && allCalculated;
            }
        }
        long long total=0;
        for (int i=63;i>=0;--i){
            std::string reg = std::string("z")+(i<10?"0":"")+std::to_string(i);
            if (registers.contains(reg)){
                std::cout << registers.at(reg);
                total+=(long long) registers.at(reg)*(1ll<<(long long)i);
            }
        }
        std::cout << std::endl;
        return total;
    }
};

std::unordered_map<std::string,int> Gate::registers;
std::vector<Gate> Gate::gates;



void day24()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day24_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day24.txt"));
    std::regex inReg("([a-z0-9]{3}):\\s([01])");
    std::regex opReg("([a-z0-9]{3})\\s([ANDXOR]{2,3})\\s([a-z0-9]{3})\\s\\-\\>\\s([a-z0-9]{3})");

    for (std::string line; std::getline(inputFile,line);){
        std::smatch match;
        if (std::regex_match(line,match,inReg)){
            Gate::registers.insert({match[1],std::stoi(match[2])});
        }else if (std::regex_match(line,match,opReg)){
            Gate::gates.push_back(Gate(match[1],match[3],match[4],match[2]));
        }
    }

    for (int i=43;i>=0;--i){
        std::string reg = std::string("x")+(i<10?"0":"")+std::to_string(i);
        std::cout << "input: " << reg << "  ";
        for (auto &&gate:Gate::gates)
        {
            if (gate.in1==reg || gate.in2==reg){
                std::cout << Gate::op2Str(gate.op) << " -> " << gate.out << "    ";
            }
        }
        std::cout << std::endl;
        reg = std::string("y")+(i<10?"0":"")+std::to_string(i);
        std::cout << "input: " << reg << "  ";
        for (auto &&gate:Gate::gates)
        {
            if (gate.in1==reg || gate.in2==reg){
                std::cout << Gate::op2Str(gate.op) << " -> " << gate.out << "    ";
            }
        }
        std::cout << std::endl;
    }


    std::cout << "Day24 task1: " << Gate::calcTotal() << std::endl;
    std::cout << "Day24 task2: " << std::endl;
}
