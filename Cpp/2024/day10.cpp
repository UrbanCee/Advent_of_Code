#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>

static std::array<Vec,4> dirs = {{{1,0},{0,1},{-1,0},{0,-1}}};

class TopoMap{
public:
    TopoMap(std::ifstream &inputFile){
        int height=0;
        int width=0;
        for (std::string line; std::getline(inputFile,line);)
        {
            if (height==0)
                width=line.size();
            playfield.append(line);
            height++;
        }
        c = Coord(height,width);
    }
    std::pair<int,int> score(int startingIndex)
    {
        std::stack<Vec> branches;
        std::set<int> topPos;
        int score=0;
        branches.push(c.toVec(startingIndex));
        do{
            Vec currentPos=branches.top();
            branches.pop();
            if (ch(currentPos)=='9'){
                topPos.insert(c.toIndex(currentPos));
                score++;
            }
            else{
                for (auto &&dir:dirs)
                {
                    Vec peekPos=currentPos+dir;
                    if (c.outOfBounds(peekPos)) continue;
                    if (ch(peekPos)-ch(currentPos)==1)
                        branches.push(peekPos);
                }
            }
        }while(!branches.empty());
        return {topPos.size(),score};
    }
    std::pair<int,int> calcTotalScore()
    {
        std::pair<int,int> totalScore={0,0};
        for (int i=0;i<playfield.size();i++){
            if (playfield.at(i)=='0'){
                auto newScore = score(i);
                totalScore.first+=newScore.first;
                totalScore.second+=newScore.second;
            }

        }
        return totalScore;
    }
private:
    char ch(const Vec &v){return playfield.at(c.toIndex(v));}
    Coord c;
    std::string playfield;
};


void day10()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day10_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day10.txt"));
    TopoMap map(inputFile);
    auto score = map.calcTotalScore() ;
    std::cout << "Day10 task1: " << score.first << std::endl;
    std::cout << "Day10 task2: " << score.second << std::endl;
}
