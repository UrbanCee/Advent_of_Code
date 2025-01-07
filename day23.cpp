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
#include <unordered_map>



struct hashFunction
{
    size_t operator()(const std::pair<std::string,std::string> &x) const
    {
        std::hash<std::string> strHash;
        return strHash(x.first) ^ strHash(x.second);
    }
};

static std::pair<std::string,std::string> asLexPair(const std::string &s1, const std::string&s2){
    if (s1<s2)
        return {s1,s2};
    else
        return {s2,s1};
}

void day23()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day23_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day23.txt"));
    std::unordered_map<std::string,std::unordered_set<std::string>> connections;
    std::vector<std::pair<std::string,std::string>> pairs;
    std::unordered_set<std::pair<std::string,std::string>,hashFunction> uniquePairs;
    std::regex pairReg("([a-z]{2})-([a-z]{2})");
    for (std::string line; std::getline(inputFile,line);)
    {
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
            pairs.push_back({adrMatch[1],adrMatch[2]});
            uniquePairs.insert(asLexPair(adrMatch[1],adrMatch[2]));
        }
    }

    std::unordered_set<std::string> triples;
    for (auto [com1,com2]:uniquePairs){
        for (auto com3:connections.at(com1)){
            if (connections.at(com2).contains(com3)){
                std::vector<std::string> vstr={com1,com2,com3};
                std::sort(vstr.begin(),vstr.end());
                triples.insert(vstr.at(0)+","+vstr.at(1)+","+vstr.at(2));
            }
        }
    }

    std::vector<std::string> biggestGroup;

    for (auto [com,con]:connections)
    {
        std::vector<std::string> currentGroup;
    }




    std::regex startsWitht("t[a-z]");
    std::cout << "Day23 task1: " << std::count_if(triples.begin(),triples.end(),[&startsWitht](auto s){return std::regex_search(s,startsWitht);}) << std::endl;
    std::cout << "Day23 task2: " << std::endl;
}
