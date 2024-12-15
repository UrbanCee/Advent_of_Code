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

void outputMap2(const std::vector<char> &map, const Coord &c, const Vec &bot)
{
    for (int y=0;y<c.height;y++)
    {
        std::string line;
        std::copy(map.begin()+(y*c.width),map.begin()+((y+1)*c.width),std::back_inserter(line));
        if (y==bot.y)
            line.at(bot.x)='@';
        std::cout << line << std::endl;
    }
}

Vec cdir2dir(char cdir)
{
    Vec dir;
    switch(cdir)
    {
    case '^':dir=Vec(0,-1);break;
    case '>':dir=Vec(1,0);break;
    case 'v':dir=Vec(0,1);break;
    case '<':dir=Vec(-1,0);break;
    }
    return std::move(dir);
}

void moveBot(std::vector<char> &map,const Coord &c,Vec &bot,char cdir)
{
    Vec dir=cdir2dir(cdir);
    int distToFree=0;
    int lookIndex=0;
    while(distToFree==0){
        Vec peekPos=bot+(++lookIndex)*dir;
        char currentMapChar = map.at(c.toIndex(peekPos));
        if (currentMapChar=='#') break;
        if (currentMapChar=='.') distToFree=lookIndex;
    }
    if (distToFree==0) return;
    for (int i=distToFree;i>0;i--)
    {
        map.at(c.toIndex(bot+i*dir))=map.at(c.toIndex(bot+(i-1)*dir));
    }
    bot = bot + dir;
    map.at(c.toIndex(bot))='.';
}

bool moveDoubleBoxVert(std::vector<char> &map, const Coord &c, const Vec &pos, const Vec&dir, bool checkOnly){
    if (map.at(c.toIndex(pos+dir))=='.') return true;
    //std::cout << "movecall" << std::endl;
    //outputMap2(map,c,pos);
    int indexoffset = map.at(c.toIndex(pos+dir))=='['?1:-1;
    if (indexoffset==-1 && !(map.at(c.toIndex(pos+dir))==']')) std::cout << "error char: " << map.at(c.toIndex(pos+dir)) << std::endl;
    if (map.at(c.toIndex(pos+2*dir))=='#' || map.at(c.toIndex(pos+2*dir)+indexoffset)=='#')
        return false;
    bool leftOk = map.at(c.toIndex(pos+2*dir))=='.';
    bool rightOk = map.at(c.toIndex(pos+2*dir)+indexoffset)=='.';
    if (leftOk && rightOk){
        if (!checkOnly){
            map.at(c.toIndex(pos+2*dir))=indexoffset>0?'[':']';
            map.at(c.toIndex(pos+2*dir)+indexoffset)=indexoffset>0?']':'[';
            map.at(c.toIndex(pos+dir))='.';
            map.at(c.toIndex(pos+dir)+indexoffset)='.';
            //std::cout << "after movement:" << std::endl;
            //outputMap2(map,c,pos);
        }
        return true;
    }
    leftOk = leftOk || moveDoubleBoxVert(map,c,pos+dir,dir,checkOnly);
    rightOk = rightOk || moveDoubleBoxVert(map,c,c.toVec(c.toIndex(pos+dir)+indexoffset),dir,checkOnly);
    if (checkOnly)
        return leftOk && rightOk;
    else{
        if (!rightOk || !leftOk)
            std::cout << "error:" << std::endl;
        else{
            //std::cout << "map before recursion:" << std::endl;
            //outputMap2(map,c,pos);
            return moveDoubleBoxVert(map,c,pos,dir,false);
        }
        return false;
    }
}

void moveBot2(std::vector<char> &map,const Coord &c,Vec &bot,char cdir)
{
    if (cdir=='<' || cdir=='>') return moveBot(map,c,bot,cdir);
    Vec dir=cdir2dir(cdir);
    if (map.at(c.toIndex(bot+dir))=='#') return;
    if (map.at(c.toIndex(bot+dir))=='.') {
        bot = bot + dir;
        return;
    }
    if (moveDoubleBoxVert(map,c,bot,dir,true)){
        moveDoubleBoxVert(map,c,bot,dir,false);
        bot = bot + dir;
        return;
    }

}

long long score(const std::vector<char> &map,const Coord &c,char scoreChar = 'O'){
    long long score =0;
    for (int i=0;i<map.size();i++)
    {
        if (map.at(i)==scoreChar)
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
    Vec bot2 = bot;
    std::vector<char> map2;
    bot2.x*=2;
    for(auto &&ch: map)
    {
        if (ch=='O'){
            map2.push_back('[');
            map2.push_back(']');
        }else{
            map2.push_back(ch);
            map2.push_back(ch);
        }
    }
    for (auto &&dir : dirs)
    {
        moveBot(map,c,bot,dir);
    }
    Coord c2(c.width*2,c.height);
    for (auto &&dir : dirs)
    {
        //std::cout << dir << std::endl;
        moveBot2(map2,c2,bot2,dir);
        //outputMap2(map2,c2,bot2);
        //std::cout << std::endl;
    }


    std::cout << "Day15 task1: " << score(map,c) << std::endl;
    std::cout << "Day15 task2: " << score(map2,c2,'[') << std::endl;
}
