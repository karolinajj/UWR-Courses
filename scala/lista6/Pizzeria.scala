package pizzeria

abstract class Type {
  val cost : Double
}

case object Margherita extends Type{
  val cost = 5.0
}
case object Peperoni extends Type{
  val cost = 6.5
}
case object Funghi extends Type{
  val cost = 7.0
}

abstract class Size
case object Small extends Size
case object Medium extends Size
case object Large extends Size

abstract class Crust
case object Thin extends Crust
case object Thick extends Crust

abstract class Topping {
  val cost : Double
}

case object Ketchup extends Topping {
  val cost = 0.5
}

case object Garlic extends Topping {
  val cost = 0.5
}

abstract class Meat {
  val cost : Double
}
case object Salami extends Meat {
  val cost = 1.0
}

abstract class Drink {
  val cost : Double
}
case object Lemonade extends Drink{
  val cost = 2.0
}

abstract class Discount
case object Student extends Discount
case object Senior extends Discount

case class Pizza(
  pizzaType: Type,
  size: Size,
  crust: Crust,
  extraTopping: Option[Topping] = None,
  extraMeat: Option[Meat] = None,
) {
  override def toString() = {
      val toppingStr = extraTopping.map(t => s", extra topping: $t").getOrElse("")
      val meatStr = extraMeat.map(m => s", extra meat: $m").getOrElse("")
      s"type: $pizzaType, size: $size, crust: $crust$toppingStr$meatStr" 
  }

  val price: Double = {
      val cost = pizzaType.cost + extraTopping.map(_.cost).getOrElse(0.0) + extraMeat.map(_.cost).getOrElse(0.0)
      
      if (size == Large) cost * 1.5
      else if (size == Small) cost * 0.9
      else cost
  }
}