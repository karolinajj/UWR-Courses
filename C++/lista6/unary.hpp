#pragma once

#include "expressions.hpp"

class UnaryOperation : public Expr //Has the same priority as Binary
{
    public:
        Expr *arg1;
        UnaryOperation(Expr *arg1);
};

class Opposite : public UnaryOperation
{
    public:
        string description();
        double eval();
        Opposite(Expr *arg1);
};

class Reciprocal : public UnaryOperation
{
    public:
        string description();
        double eval();
        Reciprocal(Expr *arg1);
};

class Abs : public UnaryOperation // |x|
{
    public:
        string description();
        double eval();
        Abs(Expr *arg1);
};

class Exp : public UnaryOperation
{
    public:
        string description();
        double eval();
        Exp(Expr *arg1);
};

class Ln : public UnaryOperation
{
    public:
        string description();
        double eval();
        Ln(Expr *arg1);
};

class Sin : public UnaryOperation
{
    public:
        string description();
        double eval();
        Sin(Expr *arg1);
};

class Cos : public UnaryOperation
{
    public:
        string description();
        double eval();
        Cos(Expr *arg1);
};