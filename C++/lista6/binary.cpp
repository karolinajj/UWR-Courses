#include "expressions.hpp"
#include "unary.hpp"
#include "binary.hpp"


BinaryOperation::BinaryOperation(Expr *arg1, Expr *arg2) : UnaryOperation(arg1)
{
    this->arg2 = arg2;
}

string Add::description()
{
    string left, right;

    if (arg1->getPriority() > getPriority())
        left = arg1->description();
    else if (arg1->getPriority() < getPriority())
        left = "(" + arg1->description() + ")";
    else if (arg1->isLeftHanded() == true)
        left = arg1->description();  
    else
        left = "(" + arg1->description() + ")";

    if (arg2->getPriority() > getPriority())
        right = arg2->description();
    else if (arg2->getPriority() <= getPriority())
        right = "(" + arg2->description() + ")";
    else if (arg2->isLeftHanded() == true)
        right = arg2->description();  
    else
        right = "(" + arg2->description() + ")";

    return left + " + " + right;
}

double Add::eval()
{
    return arg1->eval() + arg2->eval();
}

//-----------------------------------------------------------------------

string Sub::description()
{
    string left, right;

    if (arg1->getPriority() > getPriority())
        left = arg1->description();
    else if (arg1->getPriority() < getPriority())
        left = "(" + arg1->description() + ")";
    else if (arg1->isLeftHanded() == true)
        left = arg1->description();  
    else
        left = "(" + arg1->description() + ")";

    if (arg2->getPriority() > getPriority())
        right = arg2->description();
    else if (arg2->getPriority() <= getPriority())
        right = "(" + arg2->description() + ")";
    else if (arg2->isLeftHanded() == true)
        right = arg2->description();  
    else
        right = "(" + arg2->description() + ")";

    return left + " - " + right;
}

double Sub::eval()
{
    return arg1->eval() - arg2->eval();
}

//-----------------------------------------------------------------------

string Mul::description()
{
    string left, right;

    if (arg1->getPriority() > getPriority())
        left = arg1->description();
    else if (arg1->getPriority() < getPriority())
        left = "(" + arg1->description() + ")";
    else if (arg1->isLeftHanded() == true)
        left = arg1->description();  
    else
        left = "(" + arg1->description() + ")";

    if (arg2->getPriority() > getPriority())
        right = arg2->description();
    else if (arg2->getPriority() <= getPriority())
        right = "(" + arg2->description() + ")";
    else if (arg2->isLeftHanded() == true)
        right = arg2->description();  
    else
        right = "(" + arg2->description() + ")";

    return left + " * " + right;
}

double Mul::eval()
{
    return arg1->eval() * arg2->eval();
}

//-----------------------------------------------------------------------

string Div::description()
{
    string left, right;

    if (arg1->getPriority() > getPriority())
        left = arg1->description();
    else if (arg1->getPriority() < getPriority())
        left = "(" + arg1->description() + ")";
    else if (arg1->isLeftHanded() == true)
        left = arg1->description();  
    else
        left = "(" + arg1->description() + ")";

    if (arg2->getPriority() > getPriority())
        right = arg2->description();
    else if (arg2->getPriority() <= getPriority())
        right = "(" + arg2->description() + ")";
    else if (arg2->isLeftHanded() == true)
        right = arg2->description();  
    else
        right = "(" + arg2->description() + ")";

    return left + " / " + right;
}

double Div::eval()
{
    return arg1->eval() / arg2->eval();
}

//-----------------------------------------------------------------------

string Mod::description()
{
    string left, right;

    if (arg1->getPriority() > getPriority())
        left = arg1->description();
    else if (arg1->getPriority() < getPriority())
        left = "(" + arg1->description() + ")";
    else if (arg1->isLeftHanded() == true)
        left = arg1->description();  
    else
        left = "(" + arg1->description() + ")";

    if (arg2->getPriority() > getPriority())
        right = arg2->description();
    else if (arg2->getPriority() <= getPriority())
        right = "(" + arg2->description() + ")";
    else if (arg2->isLeftHanded() == true)
        right = arg2->description();  
    else
        right = "(" + arg2->description() + ")";

    return left + " % " + right;
}

double Mod::eval()
{
    return fmod(arg1->eval(), arg2->eval());
}

//-----------------------------------------------------------------------

string Pow::description()
{
    string left, right;

    if (arg1->getPriority() > getPriority())
        left = arg1->description();
    else if (arg1->getPriority() < getPriority())
        left = "(" + arg1->description() + ")";
    else if (arg1->isLeftHanded() == true)
        left = arg1->description();  
    else
        left = "(" + arg1->description() + ")";

    if (arg2->getPriority() > getPriority())
        right = arg2->description();
    else if (arg2->getPriority() <= getPriority())
        right = "(" + arg2->description() + ")";
    else if (arg2->isLeftHanded() == true)
        right = arg2->description();  
    else
        right = "(" + arg2->description() + ")";

    return left + " ^ " + right;
}

double Pow::eval()
{
    return pow(arg1->eval(), arg2->eval());
}

//-----------------------------------------------------------------------

string Log::description()
{
    return "log(" + arg1->description() + ", " + arg2->description() + ")";
}

double Log::eval()
{
    double e1, e2;
    e1 = log (arg1->eval());
    e2 = log (arg2->eval());

    return e2 / e1;
}