package money

trait Currency {
  def symbol: String
}
case object USD extends Currency { val symbol = "$" }
val `$`: Currency = USD
case object EUR extends Currency { val symbol = "€" }
val `€`: Currency = EUR
case object PLN extends Currency { val symbol = "zl" }
val zl: Currency = PLN

case class CurrencyConverter(conversion: Map[(Currency, Currency), BigDecimal]) {
  def convert(from: Currency, to: Currency): BigDecimal = {
    if (from == to) BigDecimal(1)
    else conversion.get((from, to)) match {
      case Some(rate) => rate
      case None =>
        conversion.get((to, from)) match {
          case Some(rate) => BigDecimal(1) / rate
          case None => throw new Exception(s"No conversion from $from to $to")
        }
    }
  }
}
// CurrencyConverter instance can be automatically passed to functions and classes
// that require an implicit CurrencyConverter as a parameter
implicit val conversion : CurrencyConverter = CurrencyConverter(Map(
  (EUR, USD) -> 1.12,
  (EUR, PLN) -> 4.23,
  (USD, PLN) -> 3.77,
))

// automatically looking for an implicit CurrencyConverter
case class Money(amount: BigDecimal, currency: Currency)(implicit conversion: CurrencyConverter) {
  def round(value: BigDecimal): BigDecimal = value.setScale(2, BigDecimal.RoundingMode.HALF_UP)

  def +(other: Money): Money = {
    val convertedAmount = conversion.convert(other.currency, this.currency) * other.amount
    Money(this.amount + round(convertedAmount), this.currency)
  }

  def -(other: Money): Money = {
    val convertedAmount = conversion.convert(other.currency, this.currency) * other.amount
    Money(this.amount - round(convertedAmount), this.currency)
  }

  def *(factor: BigDecimal): Money = Money(round(this.amount * factor), this.currency)

  def as(target: Currency): Money = {
    val convertedAmount = conversion.convert(this.currency, target) * this.amount
    Money(round(convertedAmount), target)
  }

  def >(other: Money): Boolean = {
    val convertedAmount = conversion.convert(other.currency, this.currency) * other.amount
    this.amount > round(convertedAmount)
  }

  def <(other: Money): Boolean = {
    val convertedAmount = conversion.convert(other.currency, this.currency) * other.amount
    this.amount < round(convertedAmount)
  }

  override def toString: String = s"$amount ${currency.symbol}"
}

object DSL {
  implicit class RichNumber[A](val n: BigDecimal){
    //allows this syntax: BigDecimal(10)(EUR)
    def apply(currency: Currency)(implicit conversion: CurrencyConverter): Money =
      Money(n, currency)
  }

  //Implicit Conversions
  //helper functions because apply only works on BigDecimal values
  //allow this syntax: 10(EUR)
  implicit def doubleToBigDecimal(d: Double): BigDecimal = BigDecimal(d)
  implicit def intToBigDecimal(i: Int): BigDecimal = BigDecimal(i)
}

// Steps:
// 10 -> BigDecimal(10) by intToBigDecimal (implicit conversion)
// wraps BigDecimal(10) into RichNumber
// calls .apply(EUR) (implicit class) with converter found implicitly (implicit parameter)
// result: Money(10, EUR)(converter)
