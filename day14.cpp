#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <sstream>


class Robot{
public:
    static int width,height;
    Vec pos,vel;
    void advance(){
        pos=pos+vel;
        if (pos.x<0) pos.x+=width;
        if (pos.x>=width) pos.x-=width;
        if (pos.y<0) pos.y+=height;
        if (pos.y>=height) pos.y-=height;
    }
};

int Robot::height=0;
int Robot::width=0;

long long calcScore(const std::vector<Robot> &robots)
{
    long long q1=0,q2=0,q3=0,q4=0;
    for (auto && bot : robots)
    {
        if (bot.pos.x<Robot::width/2){
            if (bot.pos.y<Robot::height/2)
                q1++;
            else if (bot.pos.y>Robot::height/2)
                q3++;
        }else if (bot.pos.x>Robot::width/2){
            if (bot.pos.y<Robot::height/2)
                q2++;
            else if (bot.pos.y>Robot::height/2)
                q4++;
        }
    }
    return q1*q2*q3*q4;
}

void display(const std::vector<Robot> &robots,int elapsedSec)
{
    std::vector<std::string> displayfield;
    for (int y=0;y<Robot::height;y++)
    {
        std::string line;
        for (int x=0;x<Robot::width;x++)
        {
            line.append(" ");
        }
        displayfield.push_back(line);
    }
    for (auto && bot : robots)
    {
        displayfield[bot.pos.y][bot.pos.x]='X';
    }
    std::cout << elapsedSec << ":" << std::endl;
    for (int y=0;y<Robot::height;y++){
        std::cout << displayfield[y] << std::endl;
    }
    std::cout << std::endl<< std::endl<< std::endl;
}



void day14()
{
    int seconds=100;
    int xmas=20000;
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day14_training.txt"));
    //Robot::width = 11;
    //Robot::height = 7;
    std::ifstream inputFile(std::filesystem::path("../../inputs/day14.txt"));
    Robot::width = 101;
    Robot::height = 103;
    std::vector<Robot> robots;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::regex regBot("p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)");
        std::smatch match;
        if (std::regex_match(line,match,regBot)){
            Robot robot;
            std::smatch::iterator it = std::next(match.begin());
            robot.pos.x=std::stoi(*(it++));
            robot.pos.y=std::stoi(*(it++));
            robot.vel.x=std::stoi(*(it++));
            robot.vel.y=std::stoi(*(it++));
            robots.push_back(robot);
        }
    }
    int score = 0;
    int xmasSeconds = -1;
    for (int s = 0; s<xmas; s++)
    {
        for (auto && robot:robots)
        {
            robot.advance();
            if (s==seconds-1)
                score = calcScore(robots);
        }
        if (s==7054)
            display(robots,s);
    }

    std::cout << "Day14 task1: " << score << std::endl;
    std::cout << "Day14 task2: " << std::endl;
}
