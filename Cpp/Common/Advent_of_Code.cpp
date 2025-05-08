#include "Advent_of_Code.h"
#include <filesystem>
#include <fstream>

std::string file2LongStringWithCoords(const std::string &filename,Coord &c)
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day4_training.txt"));
    std::ifstream inputFile((std::filesystem::path(filename)));
    int width = 0;
    int height = 0;
    std::string playfield;
    for (std::string line; std::getline(inputFile,line);)
    {
        if (height==0)
            width = line.size();
        if (line.size()==width)
            height++;
        playfield.append(line);
    }
    c = Coord(width,height);
    return playfield;
}
