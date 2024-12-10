#ifndef ADVENT_OF_CODE_H
#define ADVENT_OF_CODE_H

#include<vector>


class Vec{
public:
    int x{};
    int y{};

    Vec(int x, int y):x{x},y{y}{}
    Vec():x{0},y{0}{}
    Vec(const Vec&vec):x(vec.x),y(vec.y){}
    friend Vec operator+(Vec lhs,const Vec&rhs){lhs.x+=rhs.x;lhs.y+=rhs.y;return lhs;}
    friend Vec operator-(Vec lhs,const Vec&rhs){lhs.x-=rhs.x;lhs.y-=rhs.y;return lhs;}
    friend Vec operator*(int lhs,Vec rhs){rhs.x*=lhs;rhs.y*=lhs;return rhs;}
    Vec& operator=(const Vec&other){x=other.x;y=other.y;return *this;}
};


class Coord {
public:
    Coord():width(0),height(0){}
    Coord(int width,int height):width(width),height(height){}
    int x(int index)const{return index % width;}
    int y(int index)const{return index / width;}
    Vec toVec(int index)const{return Vec(x(index),y(index));}
    int toIndex(const Vec&v)const{return v.x+v.y*width;}
    bool outOfBounds(const Vec&v)const{return v.x<0||v.x>=width||v.y<0||v.y>=height;}
    Coord &operator=(const Coord &) = default;
private:
    int width;
    int height;
};

void day1();
void day2();
void day2();
void day3();
void day4();
void day5();
void day6();
long long day7(int subtask);
void day8();
void day9();
void day10();
void day11();

void aoc2023();


#endif // ADVENT_OF_CODE_H
