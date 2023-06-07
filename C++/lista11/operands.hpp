#pragma once
#include "symbol.hpp"
#include <map>

namespace calculator
{
    class number : public symbol
    {
        double value;

        public:
            number()
                : value(0.0) {}

            number(double v)
                : value(v) {}

            void eval(std::stack<double> &stos) override;
    };

    class variable : public symbol
    {
        std::string name;
        double value;

        public:
            static std::map<std::string, double> var_list;

            variable()
                : name("x"), value(0.0) {}

            variable(std::string n, double v)
                : name(n), value(v) {}

            std::string getname() const {return name;}
            double getvalue() const {return value;}

            void eval(std::stack<double> &stos) override;
    };

    class constant : public symbol
    {
        double value;

        public:
            void eval(std::stack<double> &stos) override;
    };


    class e : public constant
    {
        double value = 2.718281828459;

        public:
            using constant::eval;
    };

    class fi : public constant
    {
        double value = 1.618033988750;

        public:
            using constant::eval;
    };

    class pi : public constant
    {
        double value = 3.141592653589;

        public:
            using constant::eval;
    };
}
