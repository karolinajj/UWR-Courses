import Rational.Rational

class Point(val x: Rational, val y: Rational){
    //auxiliary constructor to create a point with int coordinates
    def this(x: Int, y: Int) = this(new Rational(x, 1), new Rational(y, 1))
    
    def this() = this(0, 0)
}

object Point {
  def apply(x: (Int, Int)): Point = new Point(new Rational(x._1, 1), new Rational(x._2, 1))
}

abstract class Figures {
  def area: Double
  val description: String = "Figure"
}

class Triangle(p1: Point, p2: Point, p3: Point) extends Figures{
    require(p1 != p2 && p1 != p3 && p2 != p3, "Points have to be different")
    require(isTriangle(p1, p2, p3), "Points must form a traingle")
    override val description = "Triangle"
    override def area: Double = {
        val x1 = p1.x.toDouble
        val y1 = p1.y.toDouble
        val x2 = p2.x.toDouble
        val y2 = p2.y.toDouble
        val x3 = p3.x.toDouble
        val y3 = p3.y.toDouble
        
        0.5 * Math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    }

    //lazy val to use are function in isTriangle
    private def isTriangle(p1: Point, p2: Point, p3: Point): Boolean = {
    val x1 = p1.x.toDouble
    val y1 = p1.y.toDouble
    val x2 = p2.x.toDouble
    val y2 = p2.y.toDouble
    val x3 = p3.x.toDouble
    val y3 = p3.y.toDouble

    val triangleArea = 0.5 * Math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    triangleArea > 0
  }
}

object Triangle {
    def apply(p1: (Int, Int), p2: (Int, Int), p3: (Int, Int)): Triangle = {
        new Triangle(Point(p1), Point(p2), Point(p3))
    }

    def egiptian: Triangle = Triangle((0,0),(0,3),(4,0))
}

class Rectangle(p1: Point, p2: Point, p3: Point, p4: Point) extends Figures{
    require(Set(p1, p2, p3, p4).size == 4, "Points have to be different")
    require(isRectangle(p1, p2, p3, p4), "Points must form a rectangle")

    override val description: String = "Rectangle"

    override def area: Double = {

        val distances = List(   distance(p1, p2), 
                                distance(p2, p3),
                                distance(p3, p4),
                                distance(p4, p1),
                                distance(p1, p3),
                                distance(p2, p4)).sorted
        val a = distances(0)
        val b = distances(2)
        a * b
    }

    private def distance(a: Point, b: Point): Double = {
        Math.sqrt(Math.pow(a.x.toDouble - b.x.toDouble, 2) + Math.pow(a.y.toDouble - b.y.toDouble, 2))
    }

    private def isRectangle(p1: Point, p2: Point, p3: Point, p4: Point): Boolean = {
        val distances = List(   distance(p1, p2), 
                                distance(p2, p3),
                                distance(p3, p4),
                                distance(p4, p1),
                                distance(p1, p3),
                                distance(p2, p4)).sorted

        distances(0) == distances(1) && distances(2) == distances(3) && distances(4) == distances(5)
    }
}

object Rectangle {
    def apply(p1: (Int, Int), p2: (Int, Int), p3: (Int, Int), p4: (Int, Int)): Rectangle = {
        new Rectangle(Point(p1), Point(p2), Point(p3), Point(p4))
    }
}

class Square(p1: Point, p2: Point, p3: Point, p4: Point) extends Figures {
    require(Set(p1, p2, p3, p4).size == 4, "Points must be distinct")
    require(isSquare(p1, p2, p3, p4), "Points must form a square")

    override val description: String = "Square"

    override val area: Double = {
        val distances = List(   distance(p1, p2),
                        distance(p2, p3),
                        distance(p3, p4),
                        distance(p4, p1),
                        distance(p1, p3),
                        distance(p2, p4)).sorted
        val a = distances(0)
        a * a
    }

    private def distance(a: Point, b: Point): Double = {
        Math.sqrt((a.x.toDouble - b.x.toDouble)*(a.x.toDouble - b.x.toDouble) + (a.y.toDouble - b.y.toDouble)*(a.y.toDouble - b.y.toDouble))
    }

    private def isSquare(p1: Point, p2: Point, p3: Point, p4: Point): Boolean = {
        val distances = List(   distance(p1, p2),
                                distance(p2, p3),
                                distance(p3, p4),
                                distance(p4, p1),
                                distance(p1, p3),
                                distance(p2, p4)).sorted

        distances(0) == distances(1) && distances(1) == distances(2) && distances(2) == distances(3) &&
        distances(4) == distances(5) && distances(4) == Math.sqrt(2) * distances(0)
    }
}

object Square {
    def apply(p1: (Int, Int), p2: (Int, Int), p3: (Int, Int), p4: (Int, Int)): Square = {
        new Square(Point(p1), Point(p2), Point(p3), Point(p4))
    }
}