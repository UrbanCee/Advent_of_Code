#include "Advent_of_Code.h"

#include <filesystem>
#include <iostream>
#include <fstream>
#include <cmath>

void day1()
{
    std::vector<int> left, right;
    std::ifstream inputFile(std::filesystem::path("../../inputs/day1.txt"));
    for (std::string line; std::getline(inputFile,line);)
    {
        std::istringstream in(line);
        left.push_back(0);
        right.push_back(0);
        in >> left.back() >> right.back();
    }
    std::sort(left.begin(),left.end());
    std::sort(right.begin(),right.end());

    long long diff = 0;
    for (auto it = std::make_pair(left.cbegin(),right.cbegin());it.first!=left.cend();++it.first,++it.second)
    {
        diff += abs(*(it.first)-*(it.second));
    }
    std::cout << "Day1 task 1:" << diff << std::endl;

    long long simScore = 0;

    for (auto && elem : left)
    {
        simScore+=elem*std::count(right.cbegin(),right.cend(),elem);
    }
    std::cout << "Day1 task 2:" << simScore << std::endl;
}
