object FiguresUtils {
  
  def areaSum(figures: List[Figures]): Double = {
    figures.map(_.area).sum
  }

  def printAll(figures: List[Figures]): Unit = {
    figures.foreach(figure => println(figure.description))
  }
}
