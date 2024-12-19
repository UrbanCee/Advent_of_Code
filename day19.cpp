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

//pair: first: pos in pattern, second: currentbasePattern

bool matchPattern(int &posInString, const std::string &pattern,std::string basePat)
{
    int newPosInString = posInString;
    auto pat_it=pattern.cbegin()+posInString;
    for (auto token : basePat){
        if (pat_it==pattern.cend()) return false;
        if (*(pat_it++)!=token) return false;
        newPosInString++;
    }
    posInString=newPosInString;
    return true;
}


long long recConstr(const std::string &pattern,const std::vector<std::string> &basePatterns,std::unordered_map<int,long long>&subsolutions,int pos)
{
    long long solutions=0;
    for (auto basePat:basePatterns)
    {
        int newPos=pos;
        if (subsolutions.count(pos+basePat.size()) && subsolutions.at(pos+basePat.size())==0) continue;
        if (matchPattern(newPos,pattern,basePat))
        {
            if (newPos==pattern.size()) solutions++;
            else {
                if (!subsolutions.count(newPos)){
                    subsolutions[newPos]=recConstr(pattern,basePatterns,subsolutions,newPos);
                }
                solutions+=subsolutions.at(newPos);
            }
        }
    }
    return solutions;
}


void day19()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day19_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day19.txt"));

    std::string basePatternString;
    std::getline(inputFile,basePatternString);
    std::vector<std::string> patterns;
    for (std::string line; std::getline(inputFile,line);){
        if (line.empty()) continue;
        patterns.push_back(line);
    }
    std::regex pattReg(", ");
    std::vector<std::string> basePatterns;
    std::copy(std::sregex_token_iterator(basePatternString.begin(),basePatternString.end(),pattReg,-1),std::sregex_token_iterator(),std::back_inserter(basePatterns));
//    std::copy(basePatterns.begin(),basePatterns.end(),std::ostream_iterator<std::string>(std::cout,"\n"));

    int iCanBeConstructed=0;
    long long totalSolutions=0;
    for(auto &&pattern : patterns)
    {
        std::unordered_map<int,long long> subsolutions;
        long long solutions = recConstr(pattern,basePatterns,subsolutions,0);
        if (solutions>0){
            iCanBeConstructed++;
            totalSolutions+=solutions;
        }
    }




    std::cout << "Day19 task1: " << iCanBeConstructed << std::endl;
    std::cout << "Day19 task2: " << totalSolutions << std::endl;
}
