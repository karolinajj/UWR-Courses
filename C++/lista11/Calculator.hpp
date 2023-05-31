#pragma once
#include <bits/stdc++.h>
#include"Number.cpp"
#include"Constant.cpp"
#include"Variables.cpp"

namespace calculator
{
    class ExpONP
    {
        private:
            string Exp;
        public:
            ExpONP();
            void print();
            void set(ExpONP e);
            void clear();
            void exit();

    };

    class Operands
    {
        class Number
        {
            public:
                double value;
                Number();
                Number(double n);
        };

        class Constant
        {
            public:
                string name; 
                double value;
                Constant(string n);
        };

        class Variables
        {
            public:
                map<string, double> vars;
                Variables();
                void Add(string n, double v);
                double GetValue(string n);
        };

        class Function
        {
            public:
                double add(double a, double b);
                double sub(double a, double b);
                double mul(double a, double b);
                double div(double a, double b);
                int mod(int a, int b);
                double min(vector<double>v);
                double max(vector<double>v);
                double log();
                double pow();
                double abs();
                double sgn();
                int floor();
                int ceil();
                double frac();
                double sin();
                double cos();
                double atan();
                double acot();
                double ln();
                double exp();
        };
    };
}
