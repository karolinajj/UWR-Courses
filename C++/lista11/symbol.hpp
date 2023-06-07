#pragma once
#include <iostream>
#include <stack>

namespace calculator
{
    class symbol
    {
        public:
            virtual void eval(std::stack<double> &stos) = 0;
    };
}
