#ifndef VECTOR_HPP
#define VECTOR_HPP

#include <iostream>
#include <cmath>
#include "point.hpp"
class Point;

class Vector
{
    private:
        double x;
        double y;
    public:
        Vector();
        Vector(double px, double py);
        Vector(const Vector& p);

        double getX();
        double getY();
        void setX(double val);
        void setY(double val);
        
        friend std::ostream& operator<<(std::ostream& out, const Vector& A);
        Vector& operator=(const Vector& A);
};


#endif