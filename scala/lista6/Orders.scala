package orders
import pizzeria._
import scala.util.matching.Regex


class Order(
    name: String,
    address: String,
    phone: String,
    pizzas: List[Pizza],
    drinks: Map[Drink, Int],
    discount: Option[Discount] = None,
    specialInfo: Option[String] = None
){
    private val validPhone: Regex = "^(\\+\\d{2})?\\d{9}$".r
    //Optionally "+" followed by two digits and exactly 9 digits after
    // ^ - start of the string
    // (\+\d{2})? - optionally
    // \d{9} - exactly 9 digits
    // $ - end of the string
    require(validPhone.matches(phone),s"Error! Invalid phone number!")

    def extraMeatPrice: Double = pizzas.flatMap(_.extraMeat.map(_.cost)).sum
    def pizzasPrice: Double = pizzas.map(_.price).sum
    def drinksPrice: Double = drinks.keys.map(key => key.cost * drinks(key)).sum
    def priceByType(pizzaType: Type): Double = pizzas.filter(_.pizzaType == pizzaType).map(_.price).sum

    val price: Double = {
        val cost = pizzasPrice + drinksPrice
        if (discount == Option(Senior)) cost * 0.93
        else if (discount == Option(Student)) cost * 0.95
        else cost
    }

    override def toString(): String = {
        val pizzasStr = pizzas match {
            case Nil => "-"
            case _   => pizzas.mkString("\n")
        }

        val drinksStr = {
            if (drinks.isEmpty) "-"
            else drinks.map { case (drink, count) => s"$drink x$count" }.mkString("\n")
        }

        val totalBeforeDiscount = pizzasPrice + drinksPrice
        val discountStr = discount.map(d => s"$d").getOrElse("-")
        val specialInfoStr = specialInfo.getOrElse("-")

        s"""Order:
        Name: $name
        Address: $address
        Phone number: $phone
        Pizzas:
        $pizzasStr
        Pizzas price:
        $pizzasPrice
        Extra Drinks:
        $drinksStr
        Drinks price:
        $drinksPrice
        Total before discount: $totalBeforeDiscount
        Discount: $discountStr
        Total: ${BigDecimal(price).setScale(2, BigDecimal.RoundingMode.HALF_UP).toDouble}
        Additional info: $specialInfoStr
        """
    }

    
}
    
