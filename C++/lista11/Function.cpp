#pragma once
#include<bits/stdc++.h>
#include"Calculator.hpp"

namespace calculator
{

    double Operands::Function::add(double a, double b)
    {
        return a + b;
    }

    double Operands::Function::sub(double a, double b)
    {
        return a - b;
    }

    double Operands::Function::mul(double a, double b)
    {
        return a * b;
    }

    double Operands::Function::div(double a, double b) //WYJĄTEK
    {
        //if(b == 0)
        return a / b;
    }

    int Operands::Function::mod(int a, int b)
    {
        return a % b;
    }
    double min(const vector<double>& v)
    {
        if (v.empty()) {
            throw runtime_error("Vector is empty");
        }

        double minValue = v[0];
        for (size_t i = 1; i < v.size(); ++i)
        {
            if (v[i] < minValue) {
                minValue = v[i];
            }
        }

        return minValue;
    }

    double max(const vector<double>& v)
    {
        if (v.empty()) {
            throw runtime_error("Vector is empty");
        }

        double maxValue = v[0];
        for (size_t i = 1; i < v.size(); ++i)
        {
            if (v[i] > maxValue) {
                maxValue = v[i];
            }
        }

        return maxValue;
    }

    double log(double x)
    {
        return log(x);
    }

    double pow(double x, double y)
    {
        return pow(x, y);
    }

    double abs(double x)
    {
        return abs(x);
    }

    double sgn(double x)
    {
        if (x > 0.0) {
            return 1.0;
        }
        else if (x < 0.0) {
            return -1.0;
        }
        else {
            return 0.0;
        }
    }

    int floor(double x)
    {
        return floor(x);
    }

    int ceil(double x)
    {
        return ceil(x);
    }

    double frac(double x)
    {
        return x - floor(x);
    }

    double sin(double x)
    {
        return sin(x);
    }

    double cos(double x)
    {
        return cos(x);
    }

    double atan(double x)
    {
        return atan(x);
    }

    double ln(double x)
    {
        return log(x);
    }

    double exp(double x)
    {
        return exp(x);
    }

}