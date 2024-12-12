#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <sstream>

std::array<Vec,8> dirs_1= {{{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}}};
std::array<Vec,4> dias={{{1,1},{-1,-1},{1,-1},{-1,1}}};
std::array<char,4> xmas_1 = {{'X','M','A','S'}};


void output(std::string playfield, int height, int width)
{
    for (int y=0;y<height;y++){
        for (int x=0;x<width;x++)
        {
            std::cout << playfield.at(x+y*width);
        }
        std::cout<<std::endl;
    }
}


void day4()
{
    Coord c;
    //std::string playfield = file2LongStringWithCoords("../../inputs/day4_training.txt",c);
    std::string playfield = file2LongStringWithCoords("../../inputs/day4.txt",c);
    int count_1=0;
    for (int i=0;i<playfield.size();i++)
    {
        if (playfield.at(i)!=xmas_1[0]) continue;
        for (auto &&dir: dirs_1){
            Vec currPos=c.toVec(i);
            for(auto ch:xmas_1)
            {
                if (c.outOfBounds(currPos))break;
                if (playfield.at(c.toIndex(currPos))!=ch) break;
                if (ch==xmas_1.back()){
                    count_1++;
                }else{
                    currPos=currPos + dir;
                }
            }
        }
    }
    int count_2=0;
    for (int i=0;i<playfield.size();i++)
    {
        if (playfield.at(i)!='A') continue;
        Vec currentPos=c.toVec(i);
        auto checkDia = [&c,&playfield](const Vec& currentPos, int dir1,int dir2,char c1, char c2){
            return playfield.at(c.toIndex(currentPos+dias.at(dir1)))==c1
                   && playfield.at(c.toIndex(currentPos+dias.at(dir2)))==c2;
        };
        if (std::any_of(dias.cbegin(),dias.cend(),[&c,&currentPos](auto &vec){return c.outOfBounds(currentPos+vec);}))
            continue;
        if ((checkDia(currentPos,0,1,'S','M')||
             checkDia(currentPos,0,1,'M','S'))&&
            (checkDia(currentPos,2,3,'S','M')||
             checkDia(currentPos,2,3,'M','S'))
            ){
            std::cout << "x:" << c.x(i) << "   y:" << c.y(i) << std::endl;
            count_2++;
        }
    }
    std::cout << "Day4 task1: " << count_1 << std::endl;
    std::cout << "Day4 task2: " << count_2 << std::endl;
}
