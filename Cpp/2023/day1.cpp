#include "../Common/Advent_of_Code.h"
#include "AoC2023.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>



void day1_2023(){

    //std::ifstream inputFile(std::filesystem::path("../../2023/input/day1_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../2023/input/day1.txt"));
    std::regex digit("\\d");
    int sum=0;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::smatch l= *std::sregex_iterator(line.cbegin(), line.cend(), digit);
        std::string rev(line);
        std::reverse(rev.begin(),rev.end());
        std::smatch r= *std::sregex_iterator(rev.cbegin(), rev.cend(), digit);
        sum+=std::stoi(l[0])*10+stoi(r[0]);
    }
    std::cout << "2023 Day1 task1: " << sum << std::endl;
    std::cout << "2023 Day1 task2: " << std::endl;
}
