#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <set>
#include <sstream>
#include <unordered_set>

#include <chrono>




long long nextNumber(long long number)
{
    number ^= (number * 64);
    number %= 16777216;
    number ^= (number / 32);
    number %= 16777216;
    number ^= (number * 2048);
    number %= 16777216;
    return number;
}



struct Last4{
    Last4():value(0),readyCount(4){}
    int value;
    int readyCount;
    void encode(int nextDiff){
        value*=100;
        value%=100000000;
        value+=(nextDiff+10);
        if (readyCount>0) readyCount--;
    }
    bool ready(){return readyCount==0;}
    int operator[](int i){
        return val(value,i);
    }
    static int val(int value,int i){
        value/=pow(100,i);
        return (value%100)-10;
    }
    static void printvalue(int value)
    {
        for (int i=3;i>=0;i--)
            std::cout << val(value,i) << " ";
        std::cout << std::endl;
    }
};

struct SellerData{
    int sellerID;
    int price;
};

void day22()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day22_training2.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day22.txt"));
    long long score=0;
    std::unordered_multimap<int,SellerData> sellPrices;
    std::unordered_set<int> uniqueKeys;
    int currentSellerID=0;
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    for (std::string line; std::getline(inputFile,line);){
        long long secretNumber = std::stoi(line);
        int lastPrice=(int) (secretNumber%10ll);
        Last4 diffs;
        for (int i=0;i<2000;i++){
            secretNumber=nextNumber(secretNumber);
            int currentPrice = (int) (secretNumber%10ll);
            int diff = currentPrice-lastPrice;
            diffs.encode(diff);
            if (diffs.ready()){
                SellerData sdata={currentSellerID,currentPrice};
                if (sellPrices.count(diffs.value)==0)
                {
                    sellPrices.insert({diffs.value,sdata});
                    uniqueKeys.insert(diffs.value);
                }else{
                    auto sameDiff= sellPrices.equal_range(diffs.value);
                    if (std::none_of(sameDiff.first,sameDiff.second,[&currentSellerID](auto &diffSeller){return currentSellerID==diffSeller.second.sellerID;}))
                    {
                        sellPrices.insert({diffs.value,sdata});
                    }
                }
            }
            lastPrice=currentPrice;
        }
        currentSellerID++;
        score+=secretNumber;
    }
    int mostBananas=0;
    for (auto &&key:uniqueKeys)
    {
        auto sameDiff= sellPrices.equal_range(key);
        int currentBananas=std::accumulate(sameDiff.first,sameDiff.second,0,[](int bananas,auto pair){return bananas+pair.second.price;});
        if (currentBananas>mostBananas){
            mostBananas=currentBananas;
        }
    }

    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << "Day22 task1: " << score <<std::endl;
    std::cout << "Day22 task2: " << mostBananas << std::endl;
    std::cout << "Runtime = " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
}
