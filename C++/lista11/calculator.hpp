#pragma once
#include "operands.hpp"
#include "operators.hpp"
#include "funbin.hpp"
#include "funun.hpp"
#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>
#include <exception>
#include <map>


namespace calculator
{
    static std::unordered_set<std::string> commands;
    static std::map<std::string, int> func_match;
    static std::map<std::string, int> con_match;

    bool parser(std::string, int, std::queue<symbol*>&);
    double evaluator(std::queue<symbol*>&);
    void update_vars(std::string, double);
    void make_dict();
    void func_parser(std::string, int, std::queue<symbol*>&);
    void con_parser(std::string, int, std::queue<symbol*>&);
    bool is_number(std::string);
    void make_actions();
}
