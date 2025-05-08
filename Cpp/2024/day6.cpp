#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <sstream>


static void outputMap(std::vector<char> &map,const Coord &c,Vec pos)
{
    std::cout << std::endl;
    for (int y=0;y<c.height;y++)
    {
        for (int x=0;x<c.width;x++)
        {
            if (pos == Vec{x,y})
                std::cout << "X";
            else
                std::cout << map.at(c.toIndex({x,y}));
        }
        std::cout << std::endl;
    }
}

static std::array<Vec,4> dirs= {{{1,0},{0,1},{-1,0},{0,-1}}};

bool willLeaveMap(std::vector<char> &map,const Coord &c,Vec pos,int dir)
{
    while(true){
        Vec newPos = pos+dirs[dir];
        if (c.outOfBounds(newPos)){
            map.at(c.toIndex(pos))='0'+dir;
            return true;
        }
        if (map.at(c.toIndex(newPos))=='#'){
            dir=(dir+1)%4;
            continue;
        }
        if (map.at(c.toIndex(pos))=='0'+dir) // loop
            return false;
        map.at(c.toIndex(pos))='0'+dir;
        pos=newPos;
   }
}

void day6()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day6_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day6.txt"));
    std::vector<char> map;
    Coord c;
    Vec start;
    for (std::string line; std::getline(inputFile,line);)
    {
        if (c.width==0)
            c.width = line.size();
        std::copy(line.begin(),line.end(),std::back_inserter(map));
        int startx = line.find('^');
        if (startx!=std::string::npos) start = {startx,c.height};
        ++c.height;
    }
    int loopingPositions=0;
    for (int i=0;i<map.size();i++)
    {
        auto m(map);
        m.at(i)='#';
        if (!willLeaveMap(m,c,start,3))
            loopingPositions++;
    }
    willLeaveMap(map,c,start,3);


    std::cout << "Day6 task1: " << std::count_if(map.begin(),map.end(),[](char c){return c>='0' && c<='3';}) << std::endl;
    std::cout << "Day6 task2: " << loopingPositions <<std::endl;
}
