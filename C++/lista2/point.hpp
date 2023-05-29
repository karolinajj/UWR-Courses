#ifndef POINT_HPP
#define POINT_HPP

#include <iostream>
#include <cmath>

#include "vector.hpp"

class Vector;

class Point
{
    private:
        double x;
        double y;
    public:
        Point();
        Point(double px, double py);
        Point(const Point& p);

        void translate(Vector v);
        void rotate(Point p, double alfa);
        void point_symetry(Point p);
        void axis_symetry(char option);

        double getX();
        double getY();
        void setX(double val);
        void setY(double val);

        friend std::ostream& operator<<(std::ostream& out, const Point& A);
        Point& operator=(const Point& A);
        bool operator==(const Point& A);
};
#endif