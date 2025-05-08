#include "../Common/Advent_of_Code.h"


#include <deque>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <sstream>

template <typename T> int sgn(T val) {
    return (T(0) < val) - (val < T(0));
}

bool isSafe(const std::deque<int> &numbers)
{
    std::deque<int> differences;
    std::adjacent_difference(numbers.cbegin(),numbers.cend(),std::back_inserter(differences));
    differences.pop_front();
    return std::none_of(differences.cbegin(),differences.cend(),[](auto &&val){return abs(val)>3 || val==0;}) &&
           std::none_of(std::next(differences.cbegin()),differences.cend(),[&differences](auto value){return sgn(value) != sgn(differences.at(0));});
}

void day2()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day2_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day2.txt"));
    int count = 0;
    int dampenedCount = 0;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::istringstream in(line);
        std::istream_iterator<int> numberIt(in);
        std::deque<int> numbers;
        std::copy(numberIt,std::istream_iterator<int> (),std::back_insert_iterator(numbers));
        if (isSafe(numbers)) count++;
        else{
            for (int i=0;i<numbers.size();i++)
            {
                std::deque<int> numbersOneRemoved=numbers;
                numbersOneRemoved.erase(numbersOneRemoved.begin()+i);
                if (isSafe(numbersOneRemoved)){
                    dampenedCount++;
                    break;
                }
            }
        }
    }
    std::cout << "Day2 task1: " << count << std::endl;
    std::cout << "Day2 task2: " << count+dampenedCount << std::endl;
}
