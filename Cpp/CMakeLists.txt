cmake_minimum_required(VERSION 3.16)

project(Cpp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(Cpp
    2023/input/day1.txt 2023/input/day1_training.txt 2023/AoC2023.h 2023/day1.cpp 2023/main2023.cpp 2024/inputs/day1.txt 2024/inputs/day10.txt 2024/inputs/day10_training.txt 2024/inputs/day11.txt 2024/inputs/day11_training.txt 2024/inputs/day12.txt 2024/inputs/day12_t2.txt 2024/inputs/day12_training.txt 2024/inputs/day13.txt 2024/inputs/day13_training.txt 2024/inputs/day14.txt 2024/inputs/day14_training.txt 2024/inputs/day15.txt 2024/inputs/day15_training.txt 2024/inputs/day16.txt 2024/inputs/day16_training_1.txt 2024/inputs/day16_training_2.txt 2024/inputs/day17.txt 2024/inputs/day17_training.txt 2024/inputs/day18.txt 2024/inputs/day18_training.txt 2024/inputs/day19.txt 2024/inputs/day19_reini.txt 2024/inputs/day19_training.txt 2024/inputs/day1_training.txt 2024/inputs/day2.txt 2024/inputs/day20.txt 2024/inputs/day20_training.txt 2024/inputs/day21.txt 2024/inputs/day21_helper.txt 2024/inputs/day21_training.txt 2024/inputs/day22.txt 2024/inputs/day22_training.txt 2024/inputs/day22_training2.txt 2024/inputs/day23.txt 2024/inputs/day23_training.txt 2024/inputs/day24.txt 2024/inputs/day24_training.txt 2024/inputs/day25.txt 2024/inputs/day25_training.txt 2024/inputs/day2_training.txt 2024/inputs/day3.txt 2024/inputs/day3_test.txt 2024/inputs/day3_training.txt 2024/inputs/day3_training2.txt 2024/inputs/day4.txt 2024/inputs/day4_training.txt 2024/inputs/day5.txt 2024/inputs/day5_training.txt 2024/inputs/day6.txt 2024/inputs/day6_training.txt 2024/inputs/day7.txt 2024/inputs/day7_training.txt 2024/inputs/day8.txt 2024/inputs/day8_training.txt 2024/inputs/day9.txt 2024/inputs/day9_training.txt 2024/day1.cpp 2024/day10.cpp 2024/day11.cpp 2024/day12.cpp 2024/day13.cpp 2024/day14.cpp 2024/day15.cpp 2024/day16.cpp 2024/day17.cpp 2024/day18.cpp 2024/day19.cpp 2024/day2.cpp 2024/day20.cpp 2024/day21.cpp 2024/day22.cpp 2024/day23.cpp 2024/day24.cpp 2024/day25.cpp 2024/day3.cpp 2024/day4.cpp 2024/day5.cpp 2024/day6.cpp 2024/day7.cpp 2024/day8.cpp 2024/day9.cpp 2024/main.cpp
    Common/Advent_of_Code.cpp Common/Advent_of_Code.h
    Common/Advent_of_Code.cpp Common/Advent_of_Code.h )

include(GNUInstallDirs)
install(TARGETS Cpp
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
