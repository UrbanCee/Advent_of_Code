cmake_minimum_required(VERSION 3.16)

project(Advent_of_Code LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(Advent_of_Code main.cpp
    Advent_of_Code.h
    day6.cpp
    day7.cpp
    day1.cpp
    day2.cpp
    day3.cpp
    day4.cpp
    day6.cpp
    day5.cpp
    day8.cpp
    day9.cpp)

include(GNUInstallDirs)
install(TARGETS Advent_of_Code
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
