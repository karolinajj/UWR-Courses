#ifndef AXIS_HPP
#define AXIS_HPP

#include "point.hpp"
#include "vector.hpp"
#include "segment.hpp"
#include "triangle.hpp"


class Vector;
class Point;
class Segment;
class Triangle;

class Axis
{
    private:
        double a;
        double b;
        double c;
    public:
        Axis();
        Axis(double a, double b, double c);
        Axis(const Axis& t);

        double getA();
        double getB();
        double getC();
        void setA(double p);
        void setB(double p);
        void setC(double p);

        friend std::ostream& operator<<(std::ostream& out, const Axis& A);
        Axis& operator=(const Axis& A);
};
#endif