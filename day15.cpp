#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>

void outputMap(const std::vector<char> &map, const Coord &c)
{
    for (int y=0;y<c.height;y++)
    {
        std::string line;
        std::copy(map.begin()+(y*c.width),map.begin()+((y+1)*c.width),std::back_inserter(line));
        std::cout << line << std::endl;
    }
}

void moveBot(std::vector<char> &map,const Coord &c,Vec &bot,char cdir)
{
    Vec dir;
    switch(cdir)
    {
    case '^':dir=Vec(0,-1);break;
    case '>':dir=Vec(1,0);break;
    case 'v':dir=Vec(0,1);break;
    case '<':dir=Vec(-1,0);break;
    }
    int distToFree=0;
    int lookIndex=0;
    while(distToFree==0){
        Vec peekPos=bot+(++lookIndex)*dir;
        char currentMapChar = map.at(c.toIndex(peekPos));
        if (currentMapChar=='#') break;
        if (currentMapChar=='.') distToFree=lookIndex;
    }
    if (distToFree==0) return;
    for (int i=distToFree;i>1;i--)
    {
        map.at(c.toIndex(bot+i*dir))='O';
    }
    bot = bot + dir;
    map.at(c.toIndex(bot))='.';
}

long long score(const std::vector<char> &map,const Coord &c){
    long long score =0;
    for (int i=0;i<map.size();i++)
    {
        if (map.at(i)=='O')
        {
            score+=c.x(i)+c.y(i)*100;
        }
    }
    return score;
}

void day15()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day15_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day15.txt"));
    bool parseMap = true;
    Coord c;
    std::vector<char> map;
    std::vector<char> dirs;
    for (std::string line; std::getline(inputFile,line);)
    {
        if (c.width==0)
            c.width=line.size();
        if (line.empty()){
            parseMap =false;
            continue;
        }
        if (parseMap) c.height++;
        std::copy(line.begin(),line.end(),std::back_inserter(parseMap?map:dirs));
    }
    auto it = std::find(map.begin(),map.end(),'@');
    Vec bot = c.toVec(std::distance(map.begin(),it));
    *it = '.';
    outputMap(map,c);
    for (auto &&dir : dirs)
    {
        moveBot(map,c,bot,dir);
    }


    std::cout << "Day15 task1: " << score(map,c) << std::endl;
    std::cout << "Day15 task2: " << std::endl;
}
