#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <queue>
#include <regex>
#include <sstream>
#include <unordered_set>


static std::array<Vec,4> dirs= {{{1,0},{0,1},{-1,0},{0,-1}}};

static void outputMap(const std::vector<char> &map, const Coord &c)
{
    for (int y=0;y<c.height;y++)
    {
        std::string line;
        std::copy(map.begin()+(y*c.width),map.begin()+((y+1)*c.width),std::back_inserter(line));
        std::cout << line << std::endl;
    }
}

struct Movement{
    Movement():pos{},dirIndex{0},cost{0}{}
    Movement(const Movement &other):pos{other.pos},dirIndex{other.dirIndex},cost{other.cost}{}
    Movement(const Vec&pos,int dirIndex,int cost):pos{pos},dirIndex{dirIndex},cost{cost}{}
    Vec pos;
    int dirIndex;
    int cost;
    bool operator>(const Movement &rhs)const{return cost>rhs.cost;}
    bool operator<(const Movement &rhs)const{return cost<rhs.cost;}
    bool operator==(const Movement &rhs)const{return pos==rhs.pos && dirIndex==rhs.dirIndex && cost==rhs.cost;}
    friend std::ostream& operator <<(std::ostream &os,const Movement &m);
    Movement &operator=(const Movement &other){pos=other.pos;dirIndex=other.dirIndex;cost=other.cost;return *this;}
};

std::ostream& operator <<(std::ostream &os,const Movement &m)
{
    os << "( " << m.pos.x << " , " << m.pos.y << " ) to dirIndex:" << m.dirIndex << "  at cost: " << m.cost << std::endl;
    return os;
}

class MovComp
{
public:
    bool operator()(const Movement &m1,const Movement &m2)
    {
        return m1>m2;
    }
};

static bool dirBlocked(const std::vector<char> &mace,const Coord &c,const Vec&pos, int dirIndex)
{
    Vec newPos=pos+dirs.at(dirIndex);
    return (c.outOfBounds(newPos) || mace.at(c.toIndex(newPos))=='#');
}

static void updatesMovements(std::priority_queue<Movement,std::vector<Movement>,MovComp> &openMovements,const Coord &c)
{

}

void day16()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day16_training_1.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day16.txt"));
    std::vector<char> mace;

    Vec start;
    Vec end;
    Coord c;
    for (std::string line; std::getline(inputFile,line);)
    {
        if (c.width==0)
            c.width=line.size();
        if (line.find("S")!=std::string::npos){
            start = Vec(line.find("S"),c.height);
        }
        if (line.find("E")!=std::string::npos){
            end = Vec(line.find("E"),c.height);
        }
        std::transform(line.begin(),line.end(),std::back_inserter(mace),[](char &ch){return ch=='#'?'#':'.';});
        c.height++;
    }

    std::priority_queue<Movement,std::vector<Movement>,MovComp> openMovements;
    std::map<int,std::vector<Movement>> visited;

    if (!dirBlocked(mace,c,start,0)){
        openMovements.push(Movement(start,0,1));
    }
    for (int i:{1,3})
    {
        if (!dirBlocked(mace,c,start,i))
            openMovements.push(Movement(start,i,1000));
    }
    if (!dirBlocked(mace,c,start,2))
        openMovements.push(Movement(start,2,2000));

    int index=0;
    int score1=0;
    std::vector<int> scoreMace(mace.size(),-1);
    scoreMace.at(c.toIndex(start))=0;
    while(!openMovements.empty())
    {
        Movement currMove = openMovements.top();
        openMovements.pop();
        visited[c.toIndex(currMove.pos)].push_back(currMove);
        Vec newPos=currMove.pos+dirs.at(currMove.dirIndex);
        int &scoreVal = scoreMace.at(c.toIndex(newPos));
        if (scoreVal==-1) scoreVal= currMove.cost+1;
        else scoreVal = scoreVal<currMove.cost+1?scoreVal:currMove.cost+1;
        if (newPos==end){
            score1=currMove.cost+1;
            break;
        }
        auto checkAndAdd=[&](int iDirIndex,int additionalCost){
            if (!dirBlocked(mace,c,newPos,iDirIndex)){
                if (visited.count(c.toIndex(newPos))==0 || std::none_of(visited.at(c.toIndex(newPos)).begin(),visited.at(c.toIndex(newPos)).end(),
                                                                          [&currMove,&additionalCost,&iDirIndex](const Movement &mov){return mov.dirIndex==iDirIndex && currMove.cost+additionalCost>=mov.cost;})){
                    openMovements.push(Movement(newPos,iDirIndex,currMove.cost+additionalCost));
                    //std::cout << "pushed: " << Movement(newPos,iDirIndex,currMove.cost+additionalCost);
                }
            }
        };
        checkAndAdd(currMove.dirIndex,1);
        for (int i:{(currMove.dirIndex+1)%4,(currMove.dirIndex+3)%4}){
            checkAndAdd(i,1001);
        }
    }

    std::queue<Vec> reverseTrail;
    std::unordered_set<int> visitedIndicies;
    reverseTrail.push(end);
    while (!reverseTrail.empty())
    {
        Vec currPos = reverseTrail.front();
        reverseTrail.pop();
        visitedIndicies.insert(c.toIndex(currPos));
        if (mace.at(c.toIndex(currPos))!='O'){
            mace.at(c.toIndex(currPos))='O';
        }
        for (auto dir:dirs)
        {
            Vec newPos=currPos+dir;
            std::cout << currPos.x << "," << currPos.y << "   " << newPos.x << "," << newPos.y << "   " << scoreMace.at(c.toIndex(currPos)) << "   " << scoreMace.at(c.toIndex(newPos)) << std::endl;
            if (c.outOfBounds(newPos)|| scoreMace.at(c.toIndex(newPos))<0) continue;
            if (scoreMace.at(c.toIndex(newPos)) < scoreMace.at(c.toIndex(currPos)) ||
                scoreMace.at(c.toIndex(newPos)) == scoreMace.at(c.toIndex(currPos))+999)
                reverseTrail.push(newPos);
        }
        scoreMace.at(c.toIndex(currPos))=-1;
    }
    outputMap(mace,c);


    std::cout << "Day16 task1: " << score1 << std::endl;
    std::cout << "Day16 task2: " << visitedIndicies.size() <<std::endl;
}
