#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <sstream>




void day14()
{
    std::ifstream inputFile(std::filesystem::path("../../inputs/day14_training.txt"));
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day14.txt"));
    for (std::string line; std::getline(inputFile,line);)
    {
        std::istringstream in(line);
        std::istream_iterator<int> numberIt(in);
    }
    std::cout << "Day14 task1: " << std::endl;
    std::cout << "Day14 task2: " << std::endl;
}
