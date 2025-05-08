#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>


bool fit(int key, int lock)
{
    for (int i=0;i<5;i++)
    {
        if (key%10+lock%10>5) return false;
        key/=10;
        lock/=10;
    }
    return true;
}


void day25()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day25_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day25.txt"));
    std::vector<int> keys;
    std::vector<int> locks;


    int keyOrLock=0; //1 lock; 2 key
    int currentDataRow=0;
    int currentPattern=0;
    for (std::string line; std::getline(inputFile,line);){
        if (line.empty()){
            continue;
        }
        if (keyOrLock==0){
            keyOrLock=line.starts_with('#')?1:2;
            currentDataRow=0;
            currentPattern=0;
            continue;
        }
        if (currentDataRow==5){
            if (keyOrLock==1)
                locks.push_back(currentPattern);
            else
                keys.push_back(currentPattern);
            keyOrLock=0;
            continue;
        }
        for (int i=0;i<line.size();i++)
        {
            if (line.at(i)=='#')
                currentPattern+=pow(10,4-i);
        }
        currentDataRow++;
    }

    int keyLockCombos=0;

    for (auto &&key:keys)
    {
        for (auto &&lock:locks){
            if (fit(key,lock)){
                keyLockCombos++;
            }
        }
    }



    std::cout << "Day25 task1: " << keyLockCombos << std::endl;
    std::cout << "Day25 task2: " << std::endl;
}
