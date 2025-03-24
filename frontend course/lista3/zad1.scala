import Utils._

object Utils {
    //checks if as is sorted according to ordering
    def isSorted(as: List[Int], ordering: (Int, Int) => Boolean) = {
        as.zip(as.tail).forall { case (a, b) => ordering(a, b) }
    }

    //checks if as is sorted in ascending order
    def isAscSorted(as: List[Int]) = {
        isSorted(as, (a: Int, b: Int) => a <= b)
    }

    //checks if as is sorted in descending order
    def isDescSorted(as: List[Int]) = {
        isSorted(as, (a: Int, b: Int) => a >= b)
    }

    def foldLeft[A, B](l: List[A], z: B)(f: (B, A) => B): B = 
        l match {
        case Nil => z
        case head :: tail => foldLeft(tail, f(z, head))(f)
    }

    def sum(l: List[Int]) = {
        foldLeft(l, 0)((a: Int, b: Int) => a + b)
    }

    def lenght(l: List[Int]) = {
        foldLeft(l,0)((a: Int, b: Int) => a + 1)
    }

    def compose[A, B, C](f: B => C, g: A => B): A => C = {
        x => f(g(x))
    }

    def repeated[A, B](f: A => A, n: Int) : A => A = {
        try {
            if (n == 1) f
            else compose(f, repeated(f, n - 1))
        } catch {
            case e: Exception => 
            println("N must be greater than 0")
            throw e
        }
    }

    def curry[A, B, C](f: (A, B) => C) = {
        (a: A) => f(a,_)
    }

    def uncurry[A, B, C](f: A => B => C) = {
        (a: A, b : B) => f(a)(b)
    }

    def unSafe[T](ex: Exception)(block: => T): T = {
        try {
            block
        } catch {
            case e: Exception =>
            println(s"An error occurred: ${e.getMessage}")
            throw ex
        }
    }
    
}

@main
def main(): Unit =
    println(isSorted(List(1, 2, 4), (a: Int, b: Int) => 2 * a == b))
    println(isAscSorted(List(1,2,3)))
    println(foldLeft(List(1,2,3), 0)((a: Int, b: Int) => a - b))
    println(sum(List(1,2,3)))
    println(lenght(List(1,2,3)))
    println(lenght(List()))
    println(compose((a: Int) => 2 * a, (a: Int) => a * a)(2))
    println(repeated((x: Int) => x*x, 2)(2))
    println(curry((a: Int, b: Int) => a + b)(1)(2))
    val curried_fun = curry((a: Int, b: Int) => a + b)
    println(uncurry(curried_fun)(1, 2))

    val result = unSafe(new Exception("My exception")) {
        1 / 0
    }


