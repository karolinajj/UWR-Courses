#include "axis.hpp"

Axis::Axis() //postać ogólna ax + by + c = 0
{
    a = 1;
    b = 1;
    c = 1;
}

Axis::Axis(double d, double e, double f)
{
    a = d;
    b = e;
    c = f;
}

Axis::Axis(const Axis& p) //copy
{
    a = p.a;
    b = p.b;
    c = p.c;
}

//-----------------------------------------------------------------------------

void Axis::setA(double val)
{
    a = val;
}

void Axis::setB(double val)
{
    b = val;
}

void Axis::setC(double val)
{
    c = val;
}

double Axis::getA()
{
    return a;
}

double Axis::getB()
{
    return b;
}

double Axis::getC()
{
    return c;
}

//-----------------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, const Axis& A)
{
    return out << A.a << "x + " << A.b << "y + " << A.c << " = 0";
}

Axis& Axis::operator=(const Axis& A)
{
    a = A.a;
    b = A.b;
    c = A.c;
    return *this;
}