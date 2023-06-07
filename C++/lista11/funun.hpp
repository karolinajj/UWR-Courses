#pragma once
#include "symbol.hpp"
#include <cmath>

namespace calculator
{
    class unfun : public symbol
    {
    protected:
        virtual double op(double a) = 0;

    public:
        void eval(std::stack<double> &stos) override;
    };

    class abs : public unfun
    {
        double op(double a) override
        {return std::abs(a);}

    public:
        using unfun::eval;
    };

    class sgn : public unfun
    {
        double op(double a) override
        {return (a > 0) - (a < 0);}

    public:
        using unfun::eval;
    };

    class floor : public unfun
    {
        double op(double a) override
        {return std::floor(a);}

    public:
        using unfun::eval;
    };


    class ceil : public unfun
    {
        double op(double a) override
        {return std::ceil(a);}

    public:
        using unfun::eval;
    };


    class frac : public unfun
    {
        double op(double a) override
        {
            double temp;
            return std::modf(a, &temp);
        }

    public:
        using unfun::eval;
    };


    class sin : public unfun
    {
        double op(double a) override
        {return std::sin(a);}

    public:
        using unfun::eval;
    };


    class cos : public unfun
    {
        double op(double a) override
        {return std::cos(a);}

    public:
        using unfun::eval;
    };


    class atan : public unfun
    {
        double op(double a) override
        {return std::atan(a);}

    public:
        using unfun::eval;
    };


    class acot : public unfun
    {
        double op(double a) override
        {
            try
            {
                if (a == 0)
                    throw std::invalid_argument("+");
            }
            catch (std::invalid_argument e)
            {
                std::clog<< "ERROR! Division by zero\n";
                throw std::invalid_argument("+");
            }

            return std::atan(1/a);
        }

    public:
        using unfun::eval;
    };


    class ln : public unfun
    {

        double op(double a) override
        {
            try
            {
                if (a == 0)
                    throw std::invalid_argument("+");
            }
            catch (std::invalid_argument e)
            {
                std::clog<< "ERROR! Division by zero\n";
                throw std::invalid_argument("+");
            }

            return std::log(a);
        }

    public:
        using unfun::eval;
    };


    class exp : public unfun
    {
        double op(double a) override
        {return std::exp(a);}

    public:
        using unfun::eval;
    };
}
