#include "segment.hpp"

LineSegment::LineSegment()
{
    a = Point(0,0);
    b = Point(1,1);

}

LineSegment::LineSegment(Point c, Point d) 
{
    try{
        if (c.getX() == d.getX() && c.getY() == d.getY())
            throw invalid_argument("");

        else
        {
            a = c;
            b = d;
        }
    }
    catch(invalid_argument)
    {
        clog<<"You cannot create a triangle from given points.\n";
    }
}

LineSegment::LineSegment(const LineSegment& line)
{
    a = line.a;
    b = line.b;
}

//-----------------------------------------------------------------------------

void LineSegment::translate(Vector v) //translacja
{
    double dx = v.getX();
    double dy = v.getY();
    a.setX( a.getX() + dx );
    a.setY( a.getY() + dy );
    b.setX( b.getX() + dx );
    b.setY( b.getY() + dy );
}

void LineSegment::rotate(Point c, double theta) //obrót
{
    a.setX((a.getX() - c.getX()) * cos(theta) - (a.getY() - c.getY()) * sin(theta) + c.getX());
    a.setY((a.getX() - c.getX()) * sin(theta) + (a.getY() - c.getY()) * cos(theta) + c.getY());
    b.setX((b.getX() - c.getX()) * cos(theta) - (b.getY() - c.getY()) * sin(theta) + c.getX());
    b.setY((b.getX() - c.getX()) * sin(theta) + (b.getY() - c.getY()) * cos(theta) + c.getY());
}

double LineSegment::length()
{
    return 1;
    //return distance(a,b);
}

void LineSegment::point_symetry(Point p) //symetry by point
{
    double px = p.getX();
    double py = p.getY();

    a.point_symetry(p);
    b.point_symetry(p);
}

void LineSegment::axis_symetry(char option) //symetry by axis
{
    if(option == 'x')
    {
        a.axis_symetry('x');
        b.axis_symetry('x');
    }

    if(option == 'y')
    {
        a.axis_symetry('y');
        b.axis_symetry('y');
    }
}

bool LineSegment::belongs(Point c)
{

    if ((c.getX() <= b.getX() && c.getY() <= b.getY() && c.getX() >= a.getX() && c.getY() >= a.getY())
        || (c.getX() >= b.getX() && c.getY() >= b.getY() && c.getX() <= a.getX() && c.getY() <= a.getY()))
    {
        double m = (a.getY() - b.getY()) / (a.getX() - b.getX());
        double i = a.getY() - (a.getY() - b.getY()) / (a.getX() - b.getX()) * a.getX();

        if (abs(c.getY() - (m * c.getX() + i)) <= 1e-10)
            return true;
        else
            return false;
    }
    else
        return false;
}

//-----------------------------------------------------------------------------

Point LineSegment::getA()
{
    return a;
}

Point LineSegment::getB()
{
    return b;
}

void LineSegment::setA(Point val)
{
    a = val;
}

void LineSegment::setB(Point val)
{
    b = val;
}

//-----------------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, const LineSegment& A)
{
    return out << "A = " << A.a << ", B = " << A.b;
}

LineSegment& LineSegment::operator=(const LineSegment& A)
{
    a = A.a;
    b = A.b;
    return *this;
}