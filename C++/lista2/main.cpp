#include <iostream>
#include <cmath>

#include "point.hpp"
#include "vector.hpp"
#include "segment.hpp"
#include "triangle.hpp"
#include "additional.hpp"
#include "axis.hpp"

using namespace std;


int main()
{
    cout << "-------------POINT-------------\n";
    cout << "Let's create a point (2.0, 3.0)\n";
    Point x(2.0, 3.0);
    cout << "\nTranslation by vector [1,2]: \n";
    Vector v(1.0, 2.0);
    x.translate(v);
    cout << x << endl;
    cout << "\nPoint symetry by (0.0, 0.0):\n";
    Point u;
    x.point_symetry(u);
    cout << x << endl;
    cout << "\nAxis symetry by OX:\n";
    x.axis_symetry('x');
    cout << x << endl;
    cout << "\nAxis symetry by OY:\n";
    x.axis_symetry('y');
    cout << x << endl;
    cout << "\nRotation by (0.0 , 0.0) and theta = pi\n";
    x.rotate(u, M_1_PI);
    cout << x << endl;

    cout << "\n-------------LINE SEGMENT-------------\n";
    cout << "Let's create a line segment using points: (0.0, 0.0), (1.0, 1.0)\n";
    x = Point(0.0, 0.0);
    u = Point(1.0, 1.0);
    LineSegment l(x,u);
    cout << "\nTranslation by vector [1,2]: \n";
    v = Vector(1.0, 2.0);
    l.translate(v);
    cout << l << endl;
    cout << "\nPoint symetry by (0.0, 0.0):\n";
    l.point_symetry(u);
    cout << l << endl;
    cout << "\nAxis symetry by OX:\n";
    l.axis_symetry('x');
    cout << l << endl;
    cout << "\nAxis symetry by OY:\n";
    l.axis_symetry('y');
    cout << l << endl;
    cout << "\nRotation by (0.0 , 0.0) and theta = pi\n";
    u = Point(0.0, 0.0);
    l.rotate(u, M_1_PI);
    cout << "\n Are l1 and l2 parallel?\n";
    Point u1 = Point();
    Point u2 = Point(0.0, 1.0);
    Point v1 = Point(1.0, 0.0);
    Point v2 = Point(1.0, -2.0);
    LineSegment l1 = LineSegment(u1,u2);
    LineSegment l2 = LineSegment(v1,v2);
    cout <<"l1: " << l1 << ", l2: " << l2 << endl;
    cout << parallel(l1,l2) << endl;
    cout << "\n Are l1 and l2 perpendicular?\n";
    cout <<"l1: " << l1 << ", l2: " << l2 << endl;
    cout << perpendicular(l1,l2) << endl;


    cout << "\n-------------TRIANGLE-------------\n";
    cout << "Let's create a triangle\n";
    Triangle t = Triangle();
    cout << t;
    cout << "\nTranslation by vector [1,2]: \n";
    v = Vector(1.0, 2.0);
    t.translate(v);
    cout << t << endl;
    cout << "\nPoint symetry by (0.0, 0.0):\n";
    u = Point();
    t.point_symetry(u);
    cout << t << endl;
    cout << "\nAxis symetry by OX:\n";
    t.axis_symetry('x');
    cout << t << endl;
    cout << "\nAxis symetry by OY:\n";
    t.axis_symetry('y');
    cout << t << endl;
    cout << "\nTriangle's perimeter:\n";
    cout << t.perimeter();
    cout << "\nTriangle's surface:\n";
    cout << t.surface();
    cout << "\nDo triangle1 and traignle2 intersect? :\n";
    Triangle t1 = Triangle();
    v = Vector(1.0, 1.0);
    Triangle t2 = Triangle();
    t2.translate(v);
    Triangle t3 = t2;
    cout << triangle_inside(t1,t2) << endl;
    cout << "\nIs triangle2 inside traignle1? :\n";
    cout << triangle_intersect(t1,t2) << endl;
    cout << "\nRotation by (0.0 , 0.0) and theta = pi\n";
    cout << t << endl;
    t.rotate(u, M_1_PI);
}