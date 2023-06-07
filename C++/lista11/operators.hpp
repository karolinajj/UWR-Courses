#pragma once
#include "symbol.hpp"

namespace calculator
{
    class operators : public symbol
    {
    protected:
        virtual double op(double a, double b) = 0;

    public:
        void eval(std::stack<double> &stos) override;
    };


    class addition : public operators
    {
        double op(double a, double b) override
        {return a + b;}

    public:
        using operators::eval;
    };


    class subtraction : public operators
    {
        double op(double a, double b) override
        {return b - a;}

    public:
        using operators::eval;
    };


    class multiplication : public operators
    {
        double op(double a, double b) override
        {return a * b;}

    public:
        using operators::eval;
    };


    class division : public operators
    {
        double op(double a, double b) override
        {
            try
            {
                if (a == 0)
                    throw std::invalid_argument("+");
            }
            catch (std::invalid_argument e)
            {
                std::clog<< "ERROR: division przez 0\n";
                throw std::invalid_argument("+");
            }

            return b / a;
        }

    public:
        using operators::eval;
    };
}
