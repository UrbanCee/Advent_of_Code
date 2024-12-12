#include "Advent_of_Code.h"

#include <iostream>
#include <cmath>
#include <array>
#include <stack>

static std::array<Vec,8> dirs= {{{1,0},{0,1},{-1,0},{0,-1}}};

void day12()
{
    Coord c;
    //std::string playfield = file2LongStringWithCoords("../../inputs/day12_training.txt",c);
    std::string playfield = file2LongStringWithCoords("../../inputs/day12.txt",c);
    std::vector<int> plotIds(playfield.size(),0);
    int iCurrentPlotIndex=1;
    std::stack<int> neighborIndices;
    long long score=0;
    for (int i=0;i<playfield.size();i++)
    {
        if (plotIds.at(i)) continue; //plot already visited
        long long area=0;
        long long perimeter=0;
        neighborIndices.push(i);
        plotIds[i]=iCurrentPlotIndex;
        while(!neighborIndices.empty()){
            Vec curr = c.toVec(neighborIndices.top());
            neighborIndices.pop();
            for (auto &&dir:dirs){
                Vec newPos = curr + dir;
                if (c.outOfBounds(newPos) || playfield.at(c.toIndex(curr))!=playfield.at(c.toIndex(newPos))){
                    perimeter++;
                    continue;
                }
                if (!plotIds.at(c.toIndex(newPos)))
                {
                    neighborIndices.push(c.toIndex(newPos));
                    plotIds[c.toIndex(newPos)]=iCurrentPlotIndex;
                }
            }
            area++;
        }
        iCurrentPlotIndex++;
        score+=area*perimeter;
    }
    std::cout << "Day12 task1: " << score << std::endl;
    std::cout << "Day12 task2: " << std::endl;
}
