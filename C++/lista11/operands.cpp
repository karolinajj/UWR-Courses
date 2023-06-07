#include "operands.hpp"

std::map<std::string, double> calculator::variable::var_list;

void calculator::number::eval(std::stack<double> &stos)
{
    stos.push(value);
}

void calculator::variable::eval(std::stack<double> &stos)
{
    stos.push(value);
}

void calculator::constant::eval(std::stack<double> &stos)
{
    stos.push(value);
}
