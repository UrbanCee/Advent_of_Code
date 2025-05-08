#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <sstream>

long long checksum(const std::vector<int> &sectors)
{
    long long acc =0;
    for (int i=0;i<sectors.size();i++)
    {
        if (sectors.at(i)<0) continue;
        acc+=i*sectors.at(i);
    }
    return acc;
}


long long task1 (std::vector<int> sectors)
{
    int low=0;
    int high=sectors.size()-1;
    while (low<high)
    {
        while(sectors.at(low)>-1 && low<high){
            low++;
        }while(sectors.at(high)==-1 && low<high){
            high--;
        }
        sectors[low]=sectors[high];
        sectors[high]=-1;
    }
    return checksum(sectors);
}


long long task2 (std::vector<int> sectors)
{
    auto itMaxID=sectors.rbegin();
    while(*itMaxID==-1)--itMaxID;
    for (int id = *itMaxID;id>=0;--id)
    {
        int filesize=std::count(sectors.cbegin(),sectors.cend(),id);
        auto IDit=find(sectors.begin(),sectors.end(),id);
        auto freeIt=sectors.begin();
        int freeSpace=0;
        while (freeIt<=IDit && freeSpace<filesize){
            if (*(freeIt++)>-1)
                freeSpace = 0;
            else
                freeSpace++;
        }
        if (freeIt>IDit) continue;
        for (int i=0;i<freeSpace;i++)
        {
            *(--freeIt)=id;
            *(IDit++)=-1;
        }
    }
    return checksum(sectors);
}


void day9()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day9_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day9.txt"));
    std::string line;
    std::getline(inputFile,line);
    int discSize=std::accumulate(line.begin(),line.end(),0,[](int acc,char ch){return acc+(ch-'0');});
    std::vector<int> sectors;
    auto ins = std::back_inserter(sectors);
    for (int compactIndex=0;compactIndex<line.size();compactIndex++)
    {
        for (int i=0;i<line.at(compactIndex)-'0';i++)
        {
            if (compactIndex%2==1)
                *(ins++)=-1;
            else
                *(ins++)=compactIndex/2;
        }
    }
    std::cout << "Day9 discSize: " << discSize << std::endl;
    std::cout << "Day9 task1: " << task1(sectors) << std::endl;
    std::cout << "Day9 task2: " << task2(sectors) << std::endl;
}
