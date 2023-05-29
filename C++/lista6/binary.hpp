#pragma once

#include "expressions.hpp"
#include "unary.hpp"

class BinaryOperation : public UnaryOperation
{
    public:
        int getPriority() override
        {
            return 1; //only for Add, Sub
        }

        Expr *arg2;
        BinaryOperation(Expr *arg1, Expr *arg2);
        virtual bool isLeftHanded() = 0;
};

class Add : public BinaryOperation
{
    public:
        std::string description();
        double eval();

        bool isLeftHanded() override
        {
            return true;
        }
        Add(Expr *arg1, Expr *arg2) : BinaryOperation(arg1, arg2) {}
};

class Sub : public BinaryOperation
{
    public:
        string description();
        double eval();

        bool isLeftHanded() override
        {
            return true;
        }
        Sub(Expr *arg1, Expr *arg2) : BinaryOperation(arg1, arg2) {}
};

class Mul : public BinaryOperation
{
    public:
        string description();
        double eval();

        int getPriority() override
        {
            return 2;
        }

        bool isLeftHanded() override
        {
            return true;
        }
        Mul(Expr *arg1, Expr *arg2) : BinaryOperation(arg1, arg2) {}
};

class Div : public BinaryOperation
{
    public:
        std::string description();
        double eval();

        int getPriority() override
        {
            return 2;
        }

        bool isLeftHanded() override
        {
            return true;
        }
        Div(Expr *arg1, Expr *arg2) : BinaryOperation(arg1, arg2) {}
};

class Mod : public BinaryOperation
{
    public:
        std::string description();
        double eval();

        int getPriority() override
        {
            return 2;
        }

        bool isLeftHanded() override
        {
            return true;
        }
        Mod(Expr *arg1, Expr *arg2) : BinaryOperation(arg1, arg2) {}
};

class Pow : public BinaryOperation
{
    public:
        string description();
        double eval();

        int getPriority() override
        {
            return 3;
        }

        bool isLeftHanded() override
        {
            return true;
        }
        Pow(Expr *arg1, Expr *arg2) : BinaryOperation(arg1, arg2) {}
};

class Log : public BinaryOperation
{
    public:
        std::string description();
        double eval();

        int getPriority() override
        {
            return 3;
        }

        bool isLeftHanded() override
        {
            return true;
        }
        Log(Expr *arg1, Expr *arg2) : BinaryOperation(arg1, arg2) {}
};
