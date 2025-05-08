#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <queue>
#include <regex>
#include <sstream>
#include <unordered_set>
#include <unordered_map>


static std::array<Vec,4> dirs= {{{1,0},{0,1},{-1,0},{0,-1}}};

static auto gt = [](const std::pair<int,int> &p1, const std::pair<int,int> &p2){
    return p1.second>p2.second;
};



static void visualizeMap(const Coord &c, const std::unordered_set<int> &corr, const std::unordered_map<int,int>&costMap,const Vec &currentPos,
                         const std::priority_queue<std::pair<int,int>,std::vector<std::pair<int,int>>,decltype(gt)> &traverse)
{
    auto copyOfTrav(traverse);
    std::unordered_set<int> traverseContent;
    while (!copyOfTrav.empty()){
        traverseContent.insert(copyOfTrav.top().first);
        copyOfTrav.pop();
    }
    for (int y=0;y<c.height;y++){
        for (int x=0;x<c.width;x++){
            int index =c.toIndex({x,y});
            if (c.toIndex(currentPos)==index) std::cout << "X";
            else if (traverseContent.find(index)!=traverseContent.end()) std::cout << "T";
            else if (corr.find(index)!=corr.end()) std::cout<< "#";
            else if (costMap.find(index)!=costMap.end()) std::cout << "0";
            else std::cout << ".";

        }
        std::cout << std::endl;
    }
}


int traverseMemory(const Coord c,const std::unordered_set<int> &corr)
{
    std::priority_queue<std::pair<int,int>,std::vector<std::pair<int,int>>,decltype(gt)>traverse(gt);
    traverse.push({0,0});
    std::unordered_map<int,int> costMap;
    while(costMap.find(c.height*c.width-1)==costMap.end() && !traverse.empty()){
        std::pair current = traverse.top();
        traverse.pop();
        if (costMap.find(current.first)!=costMap.end()) continue;
        costMap.insert({current.first,current.second});
        for (auto &&dir:dirs)
        {
            Vec nextPos = c.toVec(current.first)+dir;
            int nextIndex=c.toIndex(nextPos);
            if (c.outOfBounds(nextPos)) continue;
            if (corr.find(nextIndex)!=corr.end()) continue;
            if (costMap.find(nextIndex)!=costMap.end() && costMap.at(nextIndex)<current.second+1) continue;
            traverse.push({nextIndex,current.second+1});
        }
        //Vec currPos = c.toVec(current.first);
//        std::cout << std::endl << "at: " << currPos.x << "," << currPos.y << "   trav size:" << traverse.size() << std::endl;
//        visualizeMap(c,corr,costMap,{0,0},traverse);
    }
    if (costMap.find(c.height*c.width-1)==costMap.end())
        return -1;
    return costMap.at(c.height*c.width-1);
}


void day18()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day18_training.txt"));
    //Coord c(7,7);
    //int bytes = 12;
    std::ifstream inputFile(std::filesystem::path("../../inputs/day18.txt"));
    Coord c(71,71);
    int bytes = 1024;

    std::vector<int> corrIndices;

    for (std::string line; std::getline(inputFile,line);){
        std::regex pairReg("(\\d+),(\\d+)");
        std::smatch digitMatch;
        if (std::regex_match(line,digitMatch,pairReg))
        {
            corrIndices.push_back(c.toIndex({std::stoi(digitMatch[1]),std::stoi(digitMatch[2])}));
        }
    }


    std::unordered_set<int> corr_1;
    std::copy(corrIndices.begin(),corrIndices.begin()+bytes,std::inserter(corr_1,corr_1.begin()));




    std::cout << "Day18 task1: " << traverseMemory(c,corr_1) << std::endl;
    int lastCorrCord = 0;
    std::unordered_set<int> corr_2;
    for (auto nextCorr : corrIndices)
    {
        lastCorrCord=nextCorr;
        corr_2.insert(nextCorr);
        int steps=traverseMemory(c,corr_2);
        if (steps<0) break;
        //std::cout << std::distance(corrIndices.begin(),std::find(corrIndices.begin(),corrIndices.end(),lastCorrCord)) << ": " <<
        //    c.toVec(lastCorrCord).x << "," << c.toVec(lastCorrCord).y << "  with " << steps << "steps!" << std::endl;
    }
    std::cout << "Day18 task2: " << c.toVec(lastCorrCord).x << "," << c.toVec(lastCorrCord).y << std::endl;
}
