package Rational
class Rational(val n: Int, val d: Int) {
    require(d != 0, "Denominator cannot be zero")

    private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
    private val g = gcd(n.abs, d.abs)

    val numer: Int = (n / g) % (d / g)
    val denom: Int = d / g
    val whole: Int = (n / g) / (d / g)

    def +(other: Rational): Rational = 
        new Rational(n * other.d + other.n * d, d * other.d)

    def -(other: Rational): Rational = 
        new Rational(n * other.d - other.n * d, d * other.d)

    def *(other: Rational): Rational = 
        new Rational(n * other.n, d * other.d)

    def /(other: Rational): Rational = {
        // require(other.n != 0, "Cannot divide by zero")
        new Rational(n * other.d, d * other.n)
    }

    override def toString: String = {
        if (whole == 0 && numer == 0) s"$numer"
        else if (whole == 0) s"$numer/$denom"
        else if (numer == 0) s"$whole"
        else s"$whole $numer/$denom"
    }

    def toDouble: Double = {
        n.toDouble / d.toDouble
    }
}

// companion object
object Rational {
    def zero: Rational = new Rational(0, 1)
    def one: Rational = new Rational(1, 1)
    
    def apply(n: Int, d: Int = 1): Rational = new Rational(n, d)
}
