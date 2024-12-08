#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>



void day5()
{
    std::ifstream inputFile(std::filesystem::path("../../inputs/day5_training.txt"));
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day5.txt"));
    std::unordered_multimap<int,int> rules;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::cout << line << std::endl;
        std::regex reg("(\\d+)\\|(\\d+)");
        std::regex num("\\d+");
        std::smatch sm;
        std::regex_match(line,sm,reg);
        if (sm.size()>0){
            auto it = std::next(sm.begin());
            rules.insert({std::stoi(*it),stoi(*(std::next(it)))});
        }else{
            std::smatch dm;
            std::vector<int> numbers;
            while (std::regex_search(line,dm,num))
            {
                numbers.push_back(std::stoi(dm[0]));;
                line=dm.suffix();
            }

        }
    }
    std::cout << "Day5 task1: " << std::endl;
    std::cout << "Day5 task2: " << std::endl;
}
