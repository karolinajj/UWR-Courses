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

    def compose[A, B, C](f: B => C, g: A => B)(x : A) = {
        f(g(x))
    }

    // def repeated[A, B](f: A => A, n: Int) = {
    // }

    def curry[A, B, C](f: (A, B) => C)(a: A) = {
        f(a,_)
    }

    // def uncurry[A, B, C](f: A => B)(a: A, b: B)(c: C) = {
    //     f(a)(b)
    // }

    
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
    println(curry((a: Int, b: Int) => a + b)(1)(2))


