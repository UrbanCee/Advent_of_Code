#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>

struct Machine{
    Machine():a(),b(),prize(){}
    Machine(const Machine &m):a(m.a),b(m.b),prize(m.prize){}
    lVec a, b, prize;
    Machine &operator=(const Machine &o){a=o.a;b=o.b;prize=o.prize;return *this;}
};

lVec matchIt2Vec(std::smatch::iterator &it)
{
    int x = std::stoi(*(++it));
    int y = std::stoi(*(++it));
    return lVec(x,y);
}

long long task1(const std::vector<Machine> &machines)
{
    long long tokens=0;
    for (auto &&machine:machines)
    {
        long long det = machine.a.x*machine.b.y-machine.b.x*machine.a.y;
        if (det==0){
            std::cout << "zeroroooo" << std::endl;
            tokens+=machine.prize.x/machine.b.x;
            continue;
        }
        long long na = (machine.prize.x*machine.b.y-machine.prize.y*machine.b.x)/det;
        long long nb = (-machine.prize.x*machine.a.y+machine.prize.y*machine.a.x)/det;
        if (na*machine.a+nb*machine.b==machine.prize)
        {
            tokens+=na*3+nb;
        }
    }
    return tokens;
}


void day13()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day13_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day13.txt"));
    Machine currentMachine;
    std::vector<Machine> machines;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::regex regBut("Button ([AB]): X\\+(\\d*), Y\\+(\\d*)");
        std::regex regPrize("Prize: X=(\\d*), Y=(\\d*)");
        std::smatch match;
        if (std::regex_match(line,match,regBut)){
            std::smatch::iterator it = match.begin();
            std::string ab = *(++it);
            if (ab=="A"){
                currentMachine.a=matchIt2Vec(it);
            }else{
                currentMachine.b=matchIt2Vec(it);
            }
        }else if (std::regex_match(line,match,regPrize)){
            std::smatch::iterator it = match.begin();
            currentMachine.prize=matchIt2Vec(it);
            machines.push_back(currentMachine);
        }
    }
    std::cout << "Day13 task1: " << task1(machines) << std::endl;
    for (auto &&machine : machines)
    {
        machine.prize.x+=10000000000000;
        machine.prize.y+=10000000000000;
    }
    std::cout << "Day13 task2: "  << task1(machines) << std::endl;
}
