#include "vector.hpp"

Vector::Vector()
{
    x = 0;
    y = 0;
}

Vector::Vector(double px, double py)
{
    x = px;
    y = py;
}

Vector::Vector(const Vector& p) //copy
{
    x = p.x;
    y = p.y;
}

//-----------------------------------------------------------------------------

void Vector::setX(double val)
{
    x = val;
}

void Vector::setY(double val)
{
    y = val;
}

double Vector::getX()
{
    return x;
}

double Vector::getY()
{
    return y;
}

//-----------------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, const Vector& A)
{
    return out << "[" << A.x << ", " << A.y << "]";
}

Vector& Vector::operator=(const Vector& A)
{
    x = A.x;
    y = A.y;
    return *this;
}