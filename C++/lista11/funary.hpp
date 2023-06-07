#pragma once
#include "symbol.hpp"
#include <cmath>

namespace calculator
{
    class funary : public symbol //unary functions
    {
        protected:
            virtual double op(double x) = 0;

        public:
            void eval(std::stack<double> &stos) override;
    };

    class abs : public funary
    {
        double op(double x) override
        {return std::abs(x);}

    public:
        using funary::eval;
    };


    class sgn : public funary
    {
        double op(double x) override
        {return (x > 0) - (x < 0);}

    public:
        using funary::eval;
    };


    class frac : public funary
    {
        double op(double x) override
        {
            double temp;
            return std::modf(x, &temp);
        }

    public:
        using funary::eval;
    };


    class sin : public funary
    {
        double op(double x) override
        {return std::sin(x);}

    public:
        using funary::eval;
    };


    class cos : public funary
    {
        double op(double x) override
        {return std::cos(x);}

    public:
        using funary::eval;
    };


    class atan : public funary
    {
        double op(double x) override
        {return std::atan(x);}

    public:
        using funary::eval;
    };


    class acot : public funary
    {
        double op(double x) override
        {
            try
            {
                if (x == 0)
                    throw std::invalid_argument("+");
            }
            catch (std::invalid_argument e)
            {
                std::clog<< "ERROR! Division by zero\n";
                throw std::invalid_argument("+");
            }

            return std::atan(1/x);
        }

    public:
        using funary::eval;
    };


    class ln : public funary
    {

        double op(double x) override
        {
            try
            {
                if (x == 0)
                    throw std::invalid_argument("+");
            }
            catch (std::invalid_argument e)
            {
                std::clog<< "ERROR! Division by zero\n";
                throw std::invalid_argument("+");
            }

            return std::log(x);
        }

    public:
        using funary::eval;
    };


    class exp : public funary
    {
        double op(double x) override
        {return std::exp(x);}

    public:
        using funary::eval;
    };
}
