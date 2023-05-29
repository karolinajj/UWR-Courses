#include "expressions.hpp"
#include "unary.hpp"

using namespace std;

UnaryOperation::UnaryOperation(Expr *arg1)
{   
    this->arg1 = arg1;
}

Opposite::Opposite(Expr *arg1) : UnaryOperation(arg1) {}

string Opposite::description()
{
    return "-(" + arg1->description() + ")";
}

double Opposite::eval()
{
    return (-1) * arg1->eval();
}

//-----------------------------------------------------------------------

Reciprocal::Reciprocal(Expr *arg1) : UnaryOperation(arg1) {} //(1/x)

string Reciprocal::description()
{
    return "1 / " + arg1->description();
}

double Reciprocal::eval()
{
    return 1.0 / arg1->eval();
}

//-----------------------------------------------------------------------

Abs::Abs(Expr *arg1) : UnaryOperation(arg1) {}

string Abs::description()
{
    return "|" + arg1->description() + "|";
}

double Abs::eval()
{
    if (arg1->eval() < 0)
        return (-1) * arg1->eval();
    else
        return arg1->eval();
}

//-----------------------------------------------------------------------

Exp::Exp(Expr *arg1) : UnaryOperation(arg1) {} //wykładnicza

string Exp::description()
{
    return "exp(" + arg1->description() + ")";
}

double Exp::eval()
{
    return exp(arg1->eval());
}

//-----------------------------------------------------------------------

Ln::Ln(Expr *arg1) : UnaryOperation(arg1) {}

string Ln::description()
{
    return "ln(" + arg1->description() + ")";
}

double Ln::eval()
{
    return log(arg1->eval());
}

//-----------------------------------------------------------------------

Sin::Sin(Expr *arg1) : UnaryOperation(arg1) {}

string Sin::description()
{
    return "sin(" + arg1->description() + ")";
}

double Sin::eval()
{
    return sin(arg1->eval());
}

//-----------------------------------------------------------------------

Cos::Cos(Expr *arg1) : UnaryOperation(arg1) {}

string Cos::description()
{
    return "cos(" + arg1->description() + ")";
}

double Cos::eval()
{
    return cos(arg1->eval());
}