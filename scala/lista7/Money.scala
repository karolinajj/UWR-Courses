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

implicit val conversion : Currencyconversion = Currencyconversion(Map(
  (EUR, USD) -> 1.08,
  (EUR, PLN) -> 4.30,
  (USD, PLN) -> 4.00,
))

case class Currencyconversion(conversion: Map[(Currency, Currency), BigDecimal]) {
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

case class Money(amount: BigDecimal, currency: Currency)(implicit conversion: Currencyconversion) {
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

// Implicit Conversions for DSL Syntax
object DSL {
  implicit class RichNumber[A](val n: BigDecimal) extends AnyVal {
    def apply(currency: Currency)(implicit conversion: Currencyconversion): Money =
      Money(n, currency)
  }

  implicit def doubleToBigDecimal(d: Double): BigDecimal = BigDecimal(d)
  implicit def intToBigDecimal(i: Int): BigDecimal = BigDecimal(i)
}
