#ifndef ADVENT_OF_CODE_H
#define ADVENT_OF_CODE_H

#include<vector>
#include<string>

template <typename T>
class Vec_t{
public:
    T x{};
    T y{};

    Vec_t(T x, T y):x{x},y{y}{}
    Vec_t():x{},y{}{}
    Vec_t(const Vec_t&vec):x(vec.x),y(vec.y){}
    friend Vec_t operator+(Vec_t lhs,const Vec_t&rhs){lhs.x+=rhs.x;lhs.y+=rhs.y;return lhs;}
    friend Vec_t operator-(Vec_t lhs,const Vec_t&rhs){lhs.x-=rhs.x;lhs.y-=rhs.y;return lhs;}
    friend Vec_t operator*(int lhs,Vec_t rhs){rhs.x*=lhs;rhs.y*=lhs;return rhs;}
    Vec_t& operator=(const Vec_t&other){x=other.x;y=other.y;return *this;}
    bool operator==(const Vec_t&other)const {return x==other.x && y==other.y;}
};

typedef Vec_t<int> Vec;
typedef Vec_t<long long> lVec;

template <>
struct std::hash<Vec>
{
    std::size_t operator()(const Vec& k) const
    {
        using std::hash;

        // Compute individual hash values for first,
        // second and third and combine them using XOR
        // and bit shifting:

        return ((hash<int>()(k.x))
                 ^ (hash<int>()(k.y)));
    }
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
    int width;
    int height;
};

std::string file2LongStringWithCoords(const std::string &filename, Coord &c);

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
void day12();
void day13();
void day14();

void aoc2023();


#endif // ADVENT_OF_CODE_H
