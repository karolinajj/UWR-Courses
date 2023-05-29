#ifndef TRIANGLE_HPP
#define TRIANGLE_HPP

#include <iostream>
#include <cmath>

#include "point.hpp"
#include "vector.hpp"
#include "additional.hpp"
#include "segment.hpp"
//#include "axis.hpp"

using namespace std;

class Vector;
class Point;
//class Axis;
class Segment;

class Triangle
{
    private:
        Point a;
        Point b;
        Point c;
    public:
        Triangle();
        Triangle(Point a, Point b, Point c);
        Triangle(const Triangle& t);

        void translate(Vector v);
        void rotate(Point p, double alfa);
        void point_symetry(Point p);
        void axis_symetry(char option);

        double perimeter();
        double surface();
        bool point_inside(Point p);

        Point getA();
        Point getB();
        Point getC();
        void setA(Point p);
        void setB(Point p);
        void setC(Point p);

        friend std::ostream& operator<<(std::ostream& out, const Triangle& A);
        Triangle& operator=(const Triangle& A);
};
#endif