#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <set>
#include <sstream>

void output(std::vector<char> playfield, int height, int width)
{
    for (int y=0;y<height;y++){
        for (int x=0;x<width;x++)
        {
            std::cout << playfield.at(x+y*width);
        }
        std::cout<<std::endl;
    }
}

class Coord;

class Vec{
public:
    int x;
    int y;

    Vec(int x, int y):x(x),y(y){}
    Vec():x(0),y(0){}
    Vec(const Vec&vec):x(vec.x),y(vec.y){}
    friend Vec operator+(Vec lhs,const Vec&rhs){lhs.x+=rhs.x;lhs.y+=rhs.y;return lhs;}
    friend Vec operator-(Vec lhs,const Vec&rhs){lhs.x-=rhs.x;lhs.y-=rhs.y;return lhs;}
    friend Vec operator*(int lhs,Vec rhs){rhs.x*=lhs;rhs.y*=lhs;return rhs;}
    Vec& operator=(const Vec&other){x=other.x;y=other.y;return *this;}
};


class Coord {
public:
    Coord(int width,int height):width(width),height(height){}
    int x(int index)const{return index % width;}
    int y(int index)const{return index / width;}
    Vec toVec(int index)const{return Vec(x(index),y(index));}
    int toIndex(const Vec&v)const{return v.x+v.y*width;}
    bool outOfBounds(const Vec&v)const{return v.x<0||v.x>=width||v.y<0||v.y>=height;}
private:
    int width;
    int height;
    std::set<int> antinodes;
};


void day8()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day8_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day8.txt"));
    std::vector<char> playfield;
    int height=0, width=0;
    for (std::string line; std::getline(inputFile,line);)
    {
        width=line.length();
        std::istringstream in(line);
        std::istream_iterator<char> charIt(in);
        std::copy(charIt,std::istream_iterator<char> (),std::back_inserter(playfield));
        height++;
    }
    Coord c(width,height);
    std::unordered_map<char,std::vector<int>> towers;
    for (int i=0;i<playfield.size();i++){
        char ch = playfield.at(i);
        if ( (ch>='0'&&ch<='9') || (ch>='A'&&ch<='Z') || (ch>='a'&&ch<='z') ){
            if (towers.find(ch)==towers.end())
            {
                towers[ch]=std::vector<int>{i};
            }else{
                towers[ch].push_back(i);
            }
        }
    }

    std::set<int> antinodes_1;
    for (auto &&p:towers)
    {
        for (auto &&pos :p.second)
        {
            for (auto &&pos2: p.second)
            {
                if (pos2==pos) continue;
                Vec antiPos = (2*c.toVec(pos))-c.toVec(pos2);
                if (!c.outOfBounds(antiPos))
                    antinodes_1.insert(c.toIndex(antiPos));
            }
        }
    }

    std::set<int> antinodes_2;
    for (auto &&p:towers)
    {
        for (auto &&pos1 :p.second)
        {
            for (auto &&pos2: p.second)
            {
                if (pos2==pos1) continue;
                Vec p = c.toVec(pos1);
                Vec delta = c.toVec(pos2)-c.toVec(pos1);
                while (!c.outOfBounds(p))
                {
                    antinodes_2.insert(c.toIndex(p));
                    p=p+delta;
                }
            }
        }
    }

    std::cout << "Day8 task1: " << antinodes_1.size() << std::endl;
    std::cout << "Day8 task2: " << antinodes_2.size() <<std::endl;
}
