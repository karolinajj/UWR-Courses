import pizzeria._
import orders._

object Main extends App {
    val pizza1 = Pizza(Peperoni, Small, Thin, extraMeat=Option(Salami), extraTopping=Option(Garlic))
    println(s"Pizza 1:\n $pizza1")

    val pizza2 = Pizza(Funghi, Large, Thick)
    println(s"Pizza 2:\n $pizza2")

    val order1 = new Order("John", "ul. Main 1", "+48692109632", List(pizza1), Map(Lemonade -> 2), Option(Student), Option("Ring does not work"))
    val order2 = new Order("Alice", "ul. Main 2", "+48522139431", List(pizza2), Map())
    //val order3 = new Order("Alice", "ul. Main 2", "+1", List(pizza2), Map())
    println(order1)
    println(order2)
}