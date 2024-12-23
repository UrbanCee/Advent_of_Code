#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>
#include <unordered_set>





void day23()
{
    std::ifstream inputFile(std::filesystem::path("../../inputs/day23_training.txt"));
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day23.txt"));
    std::unordered_map<std::string,std::unordered_set<std::string>> connections;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::regex pairReg("([a-z]{2})-([a-z]{2})");
        std::smatch adrMatch;
        if (std::regex_match(line,adrMatch,pairReg))
        {
            auto insertConnection = [&connections](const std::string &from,const std::string &to)
            {
                if (!connections.contains(from)){
                    connections[from]=std::unordered_set<std::string>();
                }
                connections[from].insert(to);
            };
            insertConnection(adrMatch[1],adrMatch[2]);
            insertConnection(adrMatch[2],adrMatch[1]);
        }
    }

    for (auto [key,value]:connections)
    {
        if (value.size()>1)
        {
            std::cout << key << ",";
            for(auto &com:value){
                std::cout << com << ",";
            }
            std::cout << std::endl;
        }
    }
    std::cout << "Day23 task1: " << std::endl;
    std::cout << "Day23 task2: " << std::endl;
}
