#pragma once
#include "symbol.hpp"
#include <cmath>

namespace calculator
{
    class binfun : public symbol
    {
    protected:
        virtual double op(double a, double b) = 0;

    public:
        void eval(std::stack<double> &stos) override;
    };

    class modulo : public binfun
    {
        double op(double a, double b) override
        {
            try
            {
                if (a == 0)
                    throw std::invalid_argument("+");
            }
            catch(std::invalid_argument e)
            {
                std::clog<< "ERROR! Division by zero\n";
                throw std::invalid_argument("+");
            }

            return std::fmod(b, a);
        }

    public:
        using binfun::eval;
    };


    class min : public binfun
    {
        double op(double a, double b) override
        {return std::min(a, b);}

    public:
        using binfun::eval;
    };


    class max : public binfun
    {
        double op(double a, double b) override
        {return std::max(a, b);}

    public:
        using binfun::eval;
    };


    class log : public binfun
    {
        double op(double a, double b) override
        {
            try
            {
                if (b == 0 || a == 0 || std::log(a) == 0)
                {
                    throw std::invalid_argument("+");
                }
            }
            catch(std::invalid_argument e)
            {
                std::clog<< "ERROR! Division by zero\n";
                throw std::invalid_argument("+");
            }

            return (std::log(b)/std::log(a));
        }

    public:
        using binfun::eval;
    };

    class pow : public binfun
    {
        double op(double a, double b) override
        {return std::pow(b, a);}

    public:
        using binfun::eval;
    };
}
