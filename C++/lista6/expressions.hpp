#ifndef EXPRESSIONS_HPP
#define EXPRESSIONS_HPP

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//Priorytety:
//Expr 5
//Binary 1 or 2 (Add, Sub 1), (Mult, Div, Mod 2)
//Unary 3

class Expr
{
    public:
        virtual double eval() = 0;
        virtual string description() = 0;

        virtual int getPriority()
        {
            return 5;
        }

        virtual bool isLeftHanded()
        {
            cout << "Error: Executed isLeftHanded from Expr class.\n";
            return true;
        }

        virtual ~Expr(){};
};

//-----------------------------------------------------------------------

class Number : public Expr
{
    public:
        double value;

        Number (double value);

        string description();
        double eval();
};

//-----------------------------------------------------------------------

class Variable : public Expr
{
    private:
        static vector<pair<string, double>> variables;

    public:
        static void addVariable(string var, double val);
        static void removeVariable(string var);
        static void printVariables();

        string Variable_name;
        
        Variable(std::string var);

        string description();
        double eval();
};

//-----------------------------------------------------------------------

class Const : public Expr
{
    protected:
        double value;
};

class pi : public Const
{
    public:
        string description();
        double eval();
        pi();
};

class fi : public Const
{
    public:
        string description();
        double eval();
        fi();
};

class e : public Const
{
    public:
        string description();
        double eval();
        e();
};
#endif