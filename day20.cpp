#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <map>


static std::array<Vec,4> dirs= {{{1,0},{0,1},{-1,0},{0,-1}}};

static int manDist(const Vec &a, const Vec &b){
    return abs(a.x-b.x)+abs(a.y-b.y);
}

constexpr void createPossibleCheatLocations(std::vector<Vec> &pos,int iMaxDist)
{
    for (int y=-iMaxDist;y<=iMaxDist;y++){
        for (int x=-iMaxDist;x<=iMaxDist;x++){
            if (abs(x)+abs(y)>20 || abs(x)+abs(y)<2)
                continue;
            pos.push_back({x,y});
        }
    }
}



void day20()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day20_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day20.txt"));

    Coord c;
    Vec start,end;
    std::vector<int> raceTrack;
    for (std::string line; std::getline(inputFile,line);){
        if (c.width==0) c.width=line.size();
        for (auto ch: line){
            switch(ch)
            {
            case '#':raceTrack.push_back(-1);break;
            case 'S':raceTrack.push_back(0);start={(int) line.find(ch),c.height};break;
            case 'E':raceTrack.push_back(0);end={(int) line.find(ch),c.height};break;
            case '.':raceTrack.push_back(0);break;
            }
        }
        c.height++;
    }

    //normal race
    std::vector<Vec> racePos={start};
    while(racePos.back()!=end){
        for(auto &dir:dirs)
        {
            int nextIndex=c.toIndex(racePos.back()+dir);
            if (raceTrack.at(nextIndex) == 0 && !(racePos.back()+dir==start))
            {
                raceTrack.at(nextIndex)=raceTrack.at(c.toIndex(racePos.back()))+1;
                racePos.push_back(racePos.back()+dir);
                break;
            }
        }
    }

    std::vector<Vec> possibleCheatLocations;
    createPossibleCheatLocations(possibleCheatLocations,20);

    std::multimap<int,int> cheatsIndices_1;
    std::multimap<int,int> cheatsIndices_2;
    for (auto && pos : racePos)
    {
        for (auto &&offset:possibleCheatLocations){
            Vec peekPos=pos+offset;
            if (c.outOfBounds(peekPos)) continue;
            int savedTime=raceTrack.at(c.toIndex(peekPos))-manDist(peekPos,pos)-raceTrack.at(c.toIndex(pos));
            if (savedTime>=100){
                if (std::any_of(dirs.begin(),dirs.end(),[&](const Vec&vec){return offset==2*vec;}))
                    cheatsIndices_1.insert({savedTime,c.toIndex(peekPos)});
                cheatsIndices_2.insert({savedTime,c.toIndex(peekPos)});
            }
        }
    }



    std::cout << "Day20 task1: " << cheatsIndices_1.size() << std::endl;
    std::cout << "Day20 task2: " << cheatsIndices_2.size()<<  std::endl;
}
