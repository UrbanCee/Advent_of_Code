#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <sstream>



void day6()
{
    std::ifstream inputFile(std::filesystem::path("../../inputs/day6_training.txt"));
    Coord c(7,7);
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day6.txt"));
    //Coord c(71,71);
    for (std::string line; std::getline(inputFile,line);)
    {
        std::istringstream in(line);
        std::istream_iterator<int> numberIt(in);
    }
    std::cout << "Day6 task1: " << std::endl;
    std::cout << "Day6 task2: " << std::endl;
}
