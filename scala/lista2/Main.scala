import Rational._
import Triangle._

object Main extends App {
  println(Rational(50, 6))
  val z = Rational.zero
  println(z)
  val o = Rational.one
  println(o)
  println(Rational(5))

  val p1 = new Point()  // (0, 0)
  val p2 = new Point(4,0)  // (4, 0)
  val p3 = new Point(new Rational(0, 1), new Rational(3, 1))  // (0, 3)
  val p4 = new Point(new Rational(4, 1), new Rational(3, 1))  // (4, 3)
  val p5 = new Point(new Rational(4, 1), new Rational(4, 1))  // (4, 4)
  val p6 = new Point(new Rational(0, 1), new Rational(4, 1))  // (0, 4)

  val triangle = Triangle.egiptian
  println(s"${triangle.description} area: ${triangle.area}")

  val rectangle = new Rectangle(p1, p2, p3, p4)
  println(s"${rectangle.description} area: ${rectangle.area}")
  
  val square = Square((0,0), (4,0), (4,4), (0,4))
  println(s"${square.description} area: ${square.area}")

  val figures: List[Figures] = List(triangle, rectangle, square)
  println(s"Total area: ${FiguresUtils.areaSum(figures)}")
  println("Descriptions of figures:")
  FiguresUtils.printAll(figures)
}
