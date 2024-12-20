#include "Advent_of_Code.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <cmath>
#include <iterator>
#include <numeric>
#include <regex>
#include <set>
#include <sstream>


class Computer
{
public:
    Computer():A{0ll},B{0ll},C{0ll},pc{0ll},program{},output{}{}
    Computer(const Computer &o):A{o.A},B{o.B},C{o.C},pc{o.pc},program{o.program},output{o.output}{}
    void run();
    void outputState();
    std::string opCodeMnemonic(long long opcode, long long operand);
    std::string comboOpMn(long long operand);
    static std::string toString(const std::vector<long long> &mem){
        if (mem.empty())
            return "null";
        return std::accumulate(std::next(mem.begin()),mem.end(),std::to_string(mem.at(0)),[](const std::string &str,int i){return std::string(str).append(",").append(std::to_string(i));});
    }
    std::string outputProg(){return toString(program);}
    std::string outputOutput(){return toString(output);}
    void outputProgram();
    Computer & operator=(const Computer &o){
        this->A=o.A;
        this->B=o.B;
        this->C=o.C;
        this->pc=o.pc;
        this->output=o.output;
        this->program=o.program;
        return *this;
    }

    long long A,B,C;
    std::vector<long long> program;
    std::vector<long long> output;
    long long pc;
};

void Computer::run()
{
    while (pc<program.size())
    {
        long long opcode=program.at(pc);
        long long operand=program.at(pc+1ll);
        //check for combo operand
        //outputState();
        switch(opcode){
        case 0ll:
        case 2ll:
        case 5ll:
        case 6ll:
        case 7ll:
            {
                switch(operand){
                case 4ll:operand=A; break;
                case 5ll:operand=B; break;
                case 6ll:operand=C; break;
                }
            }
        default: break;
        }
        switch(opcode)
        {
        case 0: A>>=operand;break;
        case 1: B=B^operand;break;
        case 2: B=operand%8ll;break;
        case 3: pc=(A!=0ll?operand:pc+2ll);break;
        case 4: B=B^C;break;
        case 5: output.push_back(operand%8ll);break;
        case 6: B=A>>operand;break;
        case 7: C=A>>operand;break;
        }
        if (opcode!=3ll)
            pc+=2ll;
    }
}

void Computer::outputState()
{
    std::cout << "A: " << A << "  B: " << B << "  C: " << C << "  pc: " << pc << std::endl;
    std::cout << "op: ";
    if (pc<program.size())
    {
        std::cout << opCodeMnemonic(program[pc],program[pc+1]) << std::endl;

    }else{
        std::cout << "EoP" << std::endl;
    }
}

std::string Computer::opCodeMnemonic(long long opcode, long long operand)
{
    switch(opcode)
    {
    case 0: return "adv " + comboOpMn(operand);
    case 1: return "bxl " + std::to_string(operand);
    case 2: return "bst " + comboOpMn(operand);
    case 3: return "jnz " + std::to_string(operand);
    case 4: return "bxc " + std::to_string(operand);
    case 5: return "out " + comboOpMn(operand);
    case 6: return "bdv " + comboOpMn(operand);
    case 7: return "cdv " + comboOpMn(operand);
    }
    return "illegal opcode";
}

std::string Computer::comboOpMn(long long operand)
{
    switch(operand){
    case 4: return "A";
    case 5: return "B";
    case 6: return "C";
    }
    return std::to_string(operand);
}

void Computer::outputProgram()
{
    for (int i=0; i<program.size();i+=2)
    {
        std::cout << opCodeMnemonic(program[i],program[i+1]) << std::endl;
    }
}

void day17()
{
    //std::ifstream inputFile(std::filesystem::path("../../inputs/day17_training.txt"));
    std::ifstream inputFile(std::filesystem::path("../../inputs/day17.txt"));
    Computer c;
    c.pc=0;
    for (std::string line; std::getline(inputFile,line);)
    {
        std::regex registerRegex("Register ([ABC]): (\\d+)");
        std::regex digitRegex("\\d+");
        std::smatch regMatch;
        if (std::regex_match(line,regMatch,registerRegex)){
            auto it = regMatch.begin();
            std::string reg=*(++it);
            int value=std::stoi(*(++it));
            switch(reg.at(0)){
            case 'A':c.A=value;break;
            case 'B':c.B=value;break;
            case 'C':c.C=value;break;
            }
        }else{
            std::transform(std::sregex_iterator(line.begin(), line.end(), digitRegex),std::sregex_iterator(),std::back_inserter(c.program),
                           [](std::smatch m){return std::stoi(m[0]);});
        }

    }
    Computer s(c);
    s.A=0;
    c.run();
    std::cout << "Day17 task1: " << c.outputOutput() << std::endl;
    c.outputProgram();
    std::cout << "Target program: " << c.outputProg() << std::endl;
    std::function<bool(long long,int)> tryNumber;
    tryNumber = [&](long long lastA, int depth){
        if (depth<0){
            s.A=lastA;
            return true;
        }
        long long op = s.program[depth];
        for (long long j=0ll;j<8ll;j++){
            Computer t(s);
            long long ta = (lastA<<3)+j;
            t.A=ta;
            t.run();
            if (t.output.front()==op){
                if (tryNumber(ta,depth-1))
                {
                    return true;
                }
            }
        }
        return false;
    };
    tryNumber(0,s.program.size()-1);
    Computer t(s);
    t.run();
    std::cout << t.outputOutput() << std::endl;
    std::cout << "Day17 task2: " << s.A << std::endl;

}
