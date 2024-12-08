#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <regex>
#include <sstream>



void day3()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day3_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day3.txt"));
    std::stringstream ss;
    ss << inputFile.rdbuf();
    std::string input = ss.str();
    std::regex reg("mul\\((\\d{1,3}),(\\d{1,3})\\)");
    std::regex num("(\\d{1,3})");
    auto match_begin =
        std::sregex_iterator(input.begin(), input.end(), reg);
    auto match_end = std::sregex_iterator();
    int acc=0;
    for (auto it = match_begin; it != match_end; it++)
    {
        int prod=1;
        std::smatch match = *it;
        std::smatch::iterator numbers = match.begin();
        for (std::advance(numbers,1);numbers!=match.end();std::advance(numbers,1)){
            prod*=std::stoi(*numbers);
        }
        acc+=prod;
    }
    std::cout << "Day3 task1: " << acc << std::endl;
    std::cout << "Day3 task2: " << std::endl;
}
