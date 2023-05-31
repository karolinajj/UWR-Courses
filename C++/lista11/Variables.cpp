#pragma once
#include<bits/stdc++.h>
#include"Calculator.hpp"

namespace calculator
{
    Operands::Variables::Variables(){}

    void Operands::Variables::Add(string n, double v)
    {
        vars[n] = v;
    }

    double Operands::Variables::GetValue(string n) //WYJĄTEK
    {
        return vars[n];
    }


}