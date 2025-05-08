#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <map>
#include <numeric>
#include <unordered_map>
#include <sstream>
#include <stack>

class stone
{
public:
    stone():num(0),prev(nullptr),next(nullptr){}
    stone(const stone &n):num(n.num),prev(n.prev),next(n.next){}
    stone(int num):num(num),prev(nullptr),next(nullptr){}
    stone(int num, stone *prev, stone*next):num(num),prev(prev),next(next){}
    long long num;
    stone *prev;
    stone *next;
    stone *process();
};


stone *stone::process()
{
    if (num==0) {
        num=1;
        return next;
    }
    std::string numStr = std::to_string(num);
    if (numStr.size() % 2 ==0)
    {
        stone *newStone = new stone(std::stoi(numStr.substr(numStr.size()/2,std::string::npos)),this,this->next);
        if (this->next!=nullptr)
            this->next->prev=newStone;
        this->next=newStone;
        this->num = std::stoi(numStr.substr(0,numStr.size()/2));
        return newStone->next;
    }else
        num*=2024;
    return next;
}

void blink(stone *first)
{
    while ((first=first->process() )!= nullptr);
}

void clearStones(stone *first)
{
    stone *current=first;
    while(current!=nullptr){
        stone *next = current->next;
        delete current;
        current=next;
    }
}

void print(stone *first)
{
    while (first!=nullptr){
        std::cout << first->num << "  ";
        first=first->next;
    }
    std::cout << std::endl;
}


int count(stone *first)
{
    int size = 0;
    while(first!=nullptr){
        first = first->next;
        size++;
    }
    return size;
}

long long max(stone *first)
{
    int maxi = 0;
    while(first!=nullptr){
        maxi=first->num>maxi?first->num:maxi;
        first = first->next;
    }
    return maxi;
}


typedef long long mytype;

struct stackStone
{
    mytype num;
    char depth;
    bool operator==(const stackStone &o)const{ return (o.num==num && o.depth==depth);}
};

template <>
struct std::hash<stackStone>
{
    std::size_t operator()(const stackStone& k) const
    {
        using std::size_t;
        using std::hash;
        using std::string;

        // Compute individual hash values for first,
        // second and third and combine them using XOR
        // and bit shifting:

        return ((hash<mytype>()(k.num << 8)
                 ^ (hash<char>()(k.depth))));
    }
};

std::unordered_map<stackStone,mytype> savedInfo;

long long recSolve(stackStone stone)
{
    if (savedInfo.find(stone)!=savedInfo.end())
        return savedInfo.at(stone);
    long long value=0;
    if (stone.depth==0)
        return 1;
    char nextDepth = stone.depth-1;
    if (stone.num==0)
        value = recSolve({1,nextDepth});
    else {
        std::string numStr = std::to_string(stone.num);
        if (numStr.size() % 2 ==0){
            value = recSolve({std::stoi(numStr.substr(0,numStr.size()/2)),nextDepth})+
                    recSolve({std::stoi(numStr.substr(numStr.size()/2,std::string::npos)),nextDepth});
        }else{
            value = recSolve({stone.num*2024,nextDepth});
        }
    }
    savedInfo[stone]=value;
    return value;
}

void day11()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day11_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day11.txt"));

    stone *first = nullptr;
    stone *last = nullptr;
    const char total_depth = 75;
    std::stack<stackStone> stack;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::istringstream in(line);
        while (!in.eof()){
            long long num;
            in >> num;
            stack.push({num,total_depth});
            if (first==nullptr){
                first = new stone(num);
                last=first;
            }else{
                stone *newStone = new stone(num,last,nullptr);
                last->next=newStone;
                last=newStone;
            }
        }


    }
    for (int i=0;i<25;i++){
        blink(first);
    }
    long long stoneCount=0;
    while (!stack.empty())
    {
        stoneCount+=recSolve(stack.top());
        stack.pop();
    }
    std::cout << "Day11 task1: " << count(first) << std::endl;
    std::cout << "Day11 task2: " << stoneCount << std::endl;
    clearStones(first);
}
