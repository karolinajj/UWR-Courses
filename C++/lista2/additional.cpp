#include "additional.hpp"

double distance(Point a, Point b)
{
    double dl1 = b.getX() - a.getX();
    double dl2 = b.getY() - a.getY();

    return sqrt(dl1 * dl1 + dl2 * dl2); //sqrt(a^2 + b^2)
}

bool parallel(LineSegment c, LineSegment d)
{
    if(c.getA().getX() == c.getB().getX() && d.getA().getX() == d.getB().getX()) return true;  //proste pionowe
    if(c.getA().getX() == c.getB().getX() || d.getA().getX() == d.getB().getX()) return false;
    
    // y = mx + i
    double m1 = (c.getA().getY() - c.getB().getY()) / (c.getA().getX() - c.getB().getX());
    double m2 = (d.getA().getY() - d.getB().getY()) / (d.getA().getX() - d.getB().getX());

    if (m1 == m2)
        return true;
    else
        return false;
}

bool perpendicular(LineSegment c, LineSegment d)
{
    if(c.getA().getX() == c.getB().getX() && d.getA().getX() == d.getB().getX()) return false;  //proste pionowe
    if(c.getA().getX() == c.getB().getX() && d.getA().getY() == d.getB().getY() //prostopadłe
        || c.getA().getY() == c.getB().getY() && d.getA().getX() == d.getB().getX()
    ) return true;

    double m1 = (c.getA().getY() - c.getB().getY()) / (c.getA().getX() - c.getB().getX());
    double m2 = (d.getA().getY() - d.getB().getY()) / (d.getA().getX() - d.getB().getX());

    if (m1 == (-1 / m2))
        return true;
    else
        return false;
}

int orientation(Point a, Point b, Point c) //jak ułożone są punkty na płaszczyźnie
{
    int value = (b.getY() - a.getY()) * (c.getX() - b.getX()) - (b.getX() - a.getX()) * (c.getY() - b.getY());

    if (value == 0)
        return 0; // współliniowe
    else if (value > 0)
        return 1; // zgodnie ze wskazówkami zegara
    else
        return 2; //przeciwnie
}

bool do_intersect(LineSegment c, LineSegment d)
{
    Point p1 = c.getA();
    Point q1 = c.getB();
    Point p2 = d.getA();
    Point q2 = d.getB();

    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);

    if ((o1 != o2 && o3 != o4) 
        || (o1 == 0 && c.belongs(p2)) 
        || (o2 == 0 && c.belongs(q2)) 
        || (o3 == 0 && d.belongs(p1)) 
        || (o4 == 0 && d.belongs(q1)))
        return true;
        
    return false;
}

bool triangle_inside(Triangle u, Triangle v)
{
    Point a1 = u.getA();
    Point b1 = u.getB();
    Point c1 = u.getC();
    Point a2 = v.getA();
    Point b2 = v.getB();
    Point c2 = v.getB();

    if (u.point_inside(a2) && u.point_inside(b2) && u.point_inside(c2))
        return true;
    else if (v.point_inside(a1) && v.point_inside(b1) && v.point_inside(c1))
        return true;
    else
        return false;
}

bool triangle_intersect(Triangle u, Triangle v)
{
    if (triangle_inside(u, v))
        return false;

    Point a1 = u.getA();
    Point b1 = u.getB();
    Point c1 = u.getC();

    Point a2 = v.getA();
    Point b2 = v.getB();
    Point c2 = v.getB();

    if ((a1 == b1) || (b1 == c1) || (a1 == c1)
        || (a2 == b2) || (b2 == c2) || (a2 == c2)) return false;

    LineSegment ls1(a1, b1);
    LineSegment ls2(b1, c1);
    LineSegment ls3(a1, c1);
    LineSegment ls4(a2, b2);
    LineSegment ls5(b2, c2);
    LineSegment ls6(a2, c2);

    if (do_intersect(ls1, ls4) || do_intersect(ls1, ls5) || do_intersect(ls1, ls6))
        return true;
    if (do_intersect(ls2, ls4) || do_intersect(ls2, ls5) || do_intersect(ls2, ls6))
        return true;
    if (do_intersect(ls3, ls4) || do_intersect(ls3, ls5) || do_intersect(ls3, ls6))
         return true;

    return false;

}


