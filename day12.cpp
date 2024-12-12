#include "Advent_of_Code.h"

#include <iostream>
#include <cmath>
#include <array>
#include <stack>
#include <unordered_map>

static std::array<Vec,4> dirs= {{{1,0},{0,1},{-1,0},{0,-1}}};



void day12()
{
    Coord c;
    //std::string playfield = file2LongStringWithCoords("../../inputs/day12_training.txt",c);
    std::string playfield = file2LongStringWithCoords("../../inputs/day12.txt",c);
    std::vector<int> plotIds(playfield.size(),0);
    int iCurrentPlotIndex=1;
    std::stack<int> neighborIndices;
    long long score=0;
    long long edgescore=0;
    for (int i=0;i<playfield.size();i++)
    {
        if (plotIds.at(i)) continue; //plot already visited
        long long area=0;
        long long perimeter=0;
        neighborIndices.push(i);
        plotIds[i]=iCurrentPlotIndex;
        std::unordered_map<int,int> edges;
        while(!neighborIndices.empty()){
            Vec curr = c.toVec(neighborIndices.top());
            neighborIndices.pop();
            for (int d=0;d<dirs.size();d++){
                Vec newPos = curr + dirs[d];
                if (c.outOfBounds(newPos) || playfield.at(c.toIndex(curr))!=playfield.at(c.toIndex(newPos))){
                    perimeter++;
                    if (edges.count(c.toIndex(curr))>0)
                        edges[c.toIndex(curr)]=edges[c.toIndex(curr)]|(1<<d);
                    else
                        edges[c.toIndex(curr)]=(1<<d);
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
        int numEdges=0;
        while(!edges.empty())
        {
            auto [index,bitmask]=*edges.begin();
            for (int e=0;e<4;e++)
            {
                auto currBitmask = (1<<e);
                if ((currBitmask&bitmask) == 0)
                    continue;
                Vec scanDir;
                if (currBitmask & 0b1010) //left right going
                    scanDir=Vec(1,0);
                else
                    scanDir=Vec(0,1);
                auto currentIndex=index;
                while (!c.outOfBounds(c.toVec(currentIndex)-scanDir) &&
                       edges.count(c.toIndex(c.toVec(currentIndex)-scanDir)) &&
                       (edges[c.toIndex(c.toVec(currentIndex)-scanDir)]&currBitmask))
                    currentIndex=c.toIndex(c.toVec(currentIndex)-scanDir); //go to first Element
                while(!c.outOfBounds(c.toVec(currentIndex)) && edges.count(currentIndex) && (edges[currentIndex]&currBitmask))
                {
                    int newBitmask = edges[currentIndex] & (~currBitmask);
                    if (newBitmask)
                        edges[currentIndex]=newBitmask;
                    else
                        edges.erase(currentIndex);
                    currentIndex = c.toIndex(c.toVec(currentIndex)+scanDir);
                }
                numEdges++;
            }
        }
        iCurrentPlotIndex++;
        score+=area*perimeter;
        edgescore+=area*numEdges;
    }
    std::cout << "Day12 task1: " << score << std::endl;
    std::cout << "Day12 task2: " << edgescore << std::endl;
}
