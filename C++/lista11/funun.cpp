#include "funun.hpp"

void calculator::unfun::eval(std::stack<double> &stos)
{
    double a;

    try
    {
        if (stos.size() < 1)
        {
            throw std::invalid_argument("+");
        }
        a = stos.top();
        stos.pop();

        a = op(a);
    }
    catch (std::invalid_argument e)
    {
        std::clog<< "ERROR! Unfun\n";
        throw std::invalid_argument("+");
    }

    stos.push(a);
}
