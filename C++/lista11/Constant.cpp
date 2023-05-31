#pragma once
#include<bits/stdc++.h>
#include"Calculator.hpp"

namespace calculator
{
    Operands::Constant::Constant(string n)
    {
        if(n == "pi")
        {
            this->name = "pi";
            this->value = 3,141592653589;
        }
        if(n == "e")
        {
            this->name = "e";
            this->value = 2,718281828459;
        }
        if(n == "fi")
        {
            this->name = "e";
            this->value = 1,618033988750;
        }
    }

}