#include "../Common/Advent_of_Code.h"


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <unordered_set>
#include <unordered_map>

static std::unordered_map<char,Vec> locNum={{'7',{0,0}},{'8',{1,0}},{'9',{2,0}},{'4',{0,1}},{'5',{1,1}},{'6',{2,1}},{'1',{0,2}},{'2',{1,2}},{'3',{2,2}},{'F',{0,3}},{'0',{1,3}},{'A',{2,3}}};
static std::unordered_map<char,Vec> locDir={{'F',{0,0}},{'^',{1,0}},{'A',{2,0}},{'<',{0,1}},{'v',{1,1}},{'>',{2,1}}};
static std::unordered_map<char,Vec> dirs={{'v',{0,1}},{'^',{0,-1}},{'<',{-1,0}},{'>',{1,0}}};

class Robot{
public:
    Robot(const std::string &name):name(name),lastPos('A'){}
    virtual std::unordered_set<std::string> getMovement(const std::string &code) = 0;
protected:
    std::unordered_set<std::string> calcMovements(const std::string&code, const std::unordered_map<char,Vec> &loc, bool downFirst){
        char last=lastPos;
        std::vector<std::unordered_set<std::string>> groupedMovements;
        for (auto &&ch:code){
            Vec delta=loc.at(ch)-loc.at(last);
            std::string horStr=std::string(abs(delta.x),delta.x>0?'>':'<');
            std::string vertStr=std::string(abs(delta.y),delta.y>0?'v':'^');
            if (delta.y==0){
                groupedMovements.push_back({horStr+"A"});
                last=ch;
                continue;
            }
            if (delta.x==0){
                groupedMovements.push_back({vertStr+"A"});
                last=ch;
                continue;
            }
            std::string baseString=horStr+vertStr;
            std::sort(baseString.begin(),baseString.end());
            std::unordered_set<std::string> movementPermutations;
            do{
                if (checkValid(baseString,loc,ch,last))
                    movementPermutations.insert(baseString+"A");
            }while(std::next_permutation(baseString.begin(),baseString.end()));
            last=ch;
            groupedMovements.push_back(movementPermutations);
        }
        std::unordered_set<std::string> finalMovements;
        for (auto &&currentPerms:groupedMovements){
            if (finalMovements.empty()) {
                finalMovements=currentPerms;
                continue;
            }
            auto lastSet=finalMovements;
            finalMovements.clear();
            for (auto &&mov1:lastSet){
                for (auto &&mov2:currentPerms){
                    finalMovements.insert(mov1+mov2);
                }
            }
        }
        return finalMovements;
    }
    bool checkValid(const std::string &move,const std::unordered_map<char,Vec> &loc,char ch, char last)
    {
        Vec pos=loc.at(last);
        Vec forbidden = loc.at('F');
        for (auto dirC:move)
        {
            pos = pos + dirs.at(dirC);
            if (pos==forbidden)
                return false;
        }
        return true;
    }
    std::string name;
    char lastPos;
};

class PadRobot : public Robot{
public:
    PadRobot(const std::string &name,Robot &child):Robot(name),child(child){}
    virtual std::unordered_set<std::string> getMovement(const std::string &code)override{
        std::unordered_set<std::string> movements;
        int minLength=0;
        for (auto &&movement:child.getMovement(code))
        {
            for (auto &&calcMovement:calcMovements(movement,locDir,true)){
                movements.insert(calcMovement);
                if (minLength==0) minLength=calcMovement.size();
                else minLength=minLength<=calcMovement.size()?minLength:calcMovement.size();
            }
        }
        std::unordered_set<std::string> bestMovements;
        for (auto &&movement:movements)
        {
            if (movement.size()==minLength)
                bestMovements.insert(movement);
        }
        return bestMovements;
    }
    Robot &child;
};

class NumRobot : public Robot{
public:
    NumRobot(const std::string &name):Robot(name){}
    virtual std::unordered_set<std::string> getMovement(const std::string &code)override{
        auto returnValue = calcMovements(code,locNum,false);
        lastPos=code.back();
        return returnValue;
    }
};


void day21()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day21_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day21.txt"));
    NumRobot numBot("Numpad Robot");
    PadRobot radBot("Radiated Robot",numBot);
    PadRobot freezeBot("Freezing Robot",radBot);

    int score=0;
    for (std::string line; std::getline(inputFile,line);){
        int steps=0;
        for (auto ch: line)
            steps+=(*freezeBot.getMovement(std::string(1,ch)).begin()).size();
        std::cout << line << ": " << steps << " steps" << std::endl;
        score+=steps*std::stoi(line.substr(0,line.size()-1));
    }
    std::cout << "Day21 task1: " <<score<< std::endl;
    std::cout << "Day21 task2: " << std::endl;
}
