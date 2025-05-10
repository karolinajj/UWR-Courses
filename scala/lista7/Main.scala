import money._
import money.DSL._

object Main extends App {

  val test1 = 100(`€`) as PLN
  println(test1)

  val sum1 = 100.01(USD) + 200(EUR)
  println(s"sum1 = $sum1") // in USD

  val sum2: Money = 100.01(zl) + 200(`$`)
  println(s"sum2 = $sum2") // in PLN

  val sum3 = 5(PLN) + 3(PLN) + 20.5(USD)
  println(s"sum3 = $sum3") // in PLN

  val sub = 300.01(USD) - 200(EUR)
  println(s"sub = $sub") // in USD

  val mult1 = 30(PLN) * 20
  println(s"mult1 = $mult1") // in PLN

  val mult2 = 20(USD) * 11
  println(s"mult2 = $mult2") // in USD

  val conv1 = 150.01(USD) as PLN
  println(s"conv1 = $conv1")

  val conv2 = 120.01(USD) as EUR
  println(s"conv2 = $conv2")

  val compare1 = 300.30(USD) > 200(EUR)
  println(s"compare1 = $compare1")

  val compare2 = 300.30(USD) < 200(EUR)
  println(s"compare2 = $compare2")
}
