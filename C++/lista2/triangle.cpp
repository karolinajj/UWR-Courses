#include "triangle.hpp"

Triangle::Triangle()
{
    a = Point(0.0,0.0);
    b = Point(1.0,0.0);
    c = Point(0.0,1.0);
}

Triangle::Triangle(Point d, Point e, Point f)
{
    double x1 = d.getX();
    double y1 = d.getY();
    double x2 = e.getX();
    double y2 = e.getY();
    double x3 = f.getX();
    double y3 = f.getY();

    double D_E = LineSegment(d,e).length();
    double E_F = LineSegment(e,f).length();
    double D_F = LineSegment(d,f).length();

    
    try{
    if((y3 - y1)*(x2 - x1) - (y2 - y1)*(x3 - x1) == 0 //współliniowość
    ||  D_E + E_F + D_F - max(D_F, max(D_E, E_F)) <= max(D_F, max(D_E, E_F))) //nierówność trójkąta
        {
            throw invalid_argument("");
        }
        else
        {
            a = d;
            b = e;
            c = f;
        }
        
    }
    catch(invalid_argument)
    {
        clog<<"You cannot create a triangle from given points.\n";
    }
}

Triangle::Triangle(const Triangle& trian)
{
    a = trian.a;
    b = trian.b;
    c = trian.c;
}

//-----------------------------------------------------------------------------

void Triangle::translate(Vector v)
{
    double dx = v.getX();
    double dy = v.getY();
    a.setX( a.getX() + dx );
    a.setY( a.getY() + dy );
    b.setX( b.getX() + dx );
    b.setY( b.getY() + dy );
    c.setX( c.getX() + dx );
    c.setY( c.getY() + dy );
}

void Triangle::rotate(Point p, double theta)
{
    a.rotate(p, theta);
    b.rotate(p, theta);
    c.rotate(p, theta);

}

void Triangle::point_symetry(Point p)
{
    a.point_symetry(p);
    b.point_symetry(p);
    c.point_symetry(p);
}

void Triangle::axis_symetry(char option)
{
    if(option == 'x')
    {
        a.axis_symetry('x');
        b.axis_symetry('x');
        c.axis_symetry('x');
    }

    if(option == 'y')
    {
        a.axis_symetry('y');
        b.axis_symetry('y');
        c.axis_symetry('x');
    }
}

//-----------------------------------------------------------------------------

double Triangle::perimeter()
{

    double D_E = LineSegment(a,b).length();
    double E_F = LineSegment(a,c).length();
    double D_F = LineSegment(b,c).length();
    
    return D_E + E_F + D_F;
}

double Triangle::surface()
{
    double x = perimeter() / 2;
    double A = distance(a, b);
    double B = distance(b, c);
    double C = distance(a, c);

    return sqrt(x * (x - A) * (x - B) * (x - C));
}

bool Triangle::point_inside(Point p)
{
    Triangle t1(a,b,p);
    Triangle t2(a,c,p);
    Triangle t3(b,c,p);

    double A = surface();
    double A1 = t1.surface();
    double A2 = t2.surface();
    double A3 = t3.surface();

    if (abs(A - (A1 + A2 + A3)) < 1e-10)
        return true;
    else
        return false;
}

//-----------------------------------------------------------------------------

Point Triangle::getA()
{
    return a;
}

Point Triangle::getB()
{
    return b;
}

Point Triangle::getC()
{
    return c;
}

void Triangle::setA(Point val)
{
    a = val;
}

void Triangle::setB(Point val)
{
    b = val;
}

void Triangle::setC(Point val)
{
    c = val;
}

//-----------------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, const Triangle& A)
{
    return out << "A = " << A.a << ", B = " << A.b << ", C = " << A.c;
}

Triangle& Triangle::operator=(const Triangle& A)
{
    a = A.a;
    b = A.b;
    c = A.c;
    return *this;
}







