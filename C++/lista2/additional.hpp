#ifndef ADDITIONAL_HPP
#define ADDITIONAL_HPP

#include <iostream>
#include <cmath>
#include "point.hpp"
#include "segment.hpp"
#include "vector.hpp"
#include "triangle.hpp"
//#include "axis.hpp"

using namespace std;

class Point;
class Vector;
//class Axis;
class Triangle;
class LineSegment;

double distance(Point a, Point b);
bool parallel(LineSegment c, LineSegment d);
bool perpendicular(LineSegment c, LineSegment d);
int orientation(Point a, Point b, Point c);
bool do_intersect(LineSegment c, LineSegment d);
bool triangle_inside(Triangle u, Triangle v);
bool triangle_intersect(Triangle u, Triangle v);

#endif 