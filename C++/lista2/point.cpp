#include "point.hpp"

Point::Point()
{
    x = 0;
    y = 0;
}

Point::Point(double px, double py)
{
    x = px;
    y = py;
}

Point::Point(const Point& p) //copy
{
    x = p.x;
    y = p.y;
}

//-----------------------------------------------------------------------------

void Point::translate(Vector v)
{
    x = x + v.getX();
    y = y + v.getY();
}

void Point::rotate(Point p, double alfa) //alfa w radianach
{
    double px = p.getX();
    double py = p.getY();

    x = (x - px) * cos(alfa) - (y - py) * sin(alfa) + px;
    y = (x - px) * sin(alfa) + (y - py) * cos(alfa) + py;
}


void Point::point_symetry(Point p) //symetry by point
{
    double px = p.getX();
    double py = p.getY();

    x = 2*px - x;
    y = 2*py - y;
}

void Point::axis_symetry(char option) //symetry by axis
{
    if(option == 'x')
    {
        y = -y;
    }

    if(option == 'y')
    {
        x = -x;
    }
}

//-----------------------------------------------------------------------------

void Point::setX(double val)
{
    x = val;
}

void Point::setY(double val)
{
    y = val;
}

double Point::getX()
{
    return x;
}

double Point::getY()
{
    return y;
}

//-----------------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, const Point& A)
{
    return out << "(" << A.x << ", " << A.y << ")";
}
bool Point::operator==(const Point& A)
{
    if(A.x == x && A.y == y) return true;
    return false;
}

Point& Point::operator=(const Point& A)
{
    x = A.x;
    y = A.y;
    return *this;
}





