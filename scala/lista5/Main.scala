import plugins._
import actions._
import actions.Actions._

object Main extends App {
  
  val text = "Ala  Ma  Kota"
  println(actionA.plugin(text))
  println(actionB.plugin(text))
  println(actionC.plugin(text))
  println(actionD.plugin(text))
  println(actionE.plugin(text))
  println(actionF.plugin(text))
  println(actionG.plugin(text))
}