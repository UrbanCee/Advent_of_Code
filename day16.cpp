#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>


static std::array<Vec,4> dirs= {{{1,0},{0,1},{-1,0},{0,-1}}};

static void outputMap(const std::vector<char> &map, const Coord &c)
{
    for (int y=0;y<c.height;y++)
    {
        std::string line;
        std::copy(map.begin()+(y*c.width),map.begin()+((y+1)*c.width),std::back_inserter(line));
        std::cout << line << std::endl;
    }
}


void day16()
{
    std::ifstream inputFile(std::filesystem::path("../../inputs/day16_training_1.txt"));
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day16.txt"));
    std::vector<char> mace;
    Vec start;
    Vec end;
    int row=0;
    Coord c;
    for (std::string line; std::getline(inputFile,line);)
    {
        if (c.width==0)
            c.width=line.size();
        if (line.find("S")!=std::string::npos){
            start = Vec(line.find("S"),row);
        }
        if (line.find("E")!=std::string::npos){
            end = Vec(line.find("E"),row);
        }
        std::transform(line.begin(),line.end(),std::back_inserter(mace),[](char &ch){return ch=='#'?'#':'.';});
        row++;
    }
    c.height=row;
    outputMap(mace,c);
    std::cout << "Day16 task1: " << std::endl;
    std::cout << "Day16 task2: " << std::endl;
}
