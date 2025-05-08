#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <list>
#include <regex>
#include <sstream>


bool goodQueue(const std::vector<int> &queue,const std::unordered_multimap<int,int> &rules)
{
    for (int i=0;i<queue.size();i++)
    {
        for (int j=i+1;j<queue.size();j++)
        {
            auto range = rules.equal_range(queue[j]);
            for (auto it = range.first;it != range.second;it++)
            {
                if (queue[i]==it->second)
                    return false;
            }
        }
    }
    return true;
}

bool lessThan(const std::unordered_multimap<int,int> &rules,int a, int b)
{
    for (auto [it, ite]=rules.equal_range(a);it!=ite;it++)
    {
        if (it->second==b)
            return true;
    }
    return false;
}

void swap(std::vector<int> &vec,int pos1, int pos2)
{
    auto tmp = vec.at(pos1);
    vec[pos1]=vec.at(pos2);
    vec[pos2]=tmp;
}

void day5()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day5_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day5.txt"));
    std::unordered_multimap<int,int> keySmallerThanValue;
    std::vector<std::vector<int>> printQueues;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::regex reg("(\\d+)\\|(\\d+)");
        std::smatch sm;
        std::regex_match(line,sm,reg);
        if (sm.size()>0){
            auto it = std::next(sm.begin());
            keySmallerThanValue.insert({std::stoi(*it),stoi(*(std::next(it)))});
        }else{
            std::istringstream ss(line);
            std::vector<int> currQueue;
            std::string numStr;
            while(std::getline(ss,numStr,','))
            {
                currQueue.push_back(std::stoi(numStr));
            }
            if (!currQueue.empty()) printQueues.push_back(currQueue);
        }
    }

    int sumGood=0;
    int sumCorr=0;
    for (auto &&queue : printQueues)
    {
        if (goodQueue(queue,keySmallerThanValue))
            sumGood+=queue.at(queue.size()/2);
        else{
            for (int i=0;i<queue.size();i++){
                for (int j=i+1;j<queue.size();j++){
                    if (lessThan(keySmallerThanValue,queue[j],queue[i]))
                        swap(queue,i,j);
                }
            }
            sumCorr+=queue.at(queue.size()/2);;
        }
    }
    std::cout << "Day5 task1: " << sumGood << std::endl;
    std::cout << "Day5 task2: " << sumCorr << std::endl;
}
