#ifndef LINESEGMENT_HPP
#define LINESEGMENT_HPP

#include <iostream>
#include <cmath>
#include <exception>

#include "point.hpp"
#include "vector.hpp"
#include "additional.hpp"
#include "segment.hpp"
//#include "axis.hpp"


class Vector;
class Point;
//class Axis;

class LineSegment
{
    private:
        Point a;
        Point b;

    public:
        LineSegment();
        LineSegment(Point c, Point d);
        LineSegment(const LineSegment& l);

        Point getA();
        Point getB();
        void setA(Point p);
        void setB(Point p);

        void translate(Vector v);
        void rotate(Point c, double theta);
        void point_symetry(Point p);
        void axis_symetry(char option);

        double length();
        bool belongs(Point c);

        friend std::ostream& operator<<(std::ostream& out, const LineSegment& A);
        LineSegment& operator=(const LineSegment& A);
};

#endif 
