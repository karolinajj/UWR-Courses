import scala.io.Source

//scalar product of two vectors xs and ys
def scalarUgly(xs: List[Int], ys: List[Int]): Int = {
  var sum = 0
  var i = 0
  
  while(i < xs.length && i < ys.length) {
    sum += xs(i) * ys(i)
    i += 1
  }
  
  sum
}

def scalar(xs: List[Int], ys: List[Int]): Int = {
  val sum = (for ((x, y) <- xs zip ys) yield x * y).sum //yield returns a vector
  sum
}

//checks if n is prime
def isPrimeUgly(n: Int): Boolean = {
    var i = 2
    while(i <= Math.sqrt(n)){
        if(n % i == 0) return false
        i+=1
    }
    true
}

def isPrime(n: Int): Boolean = {
  if (n <= 1) false
  else {
    val divisors = for (i <- 2 to Math.sqrt(n).toInt if n % i == 0) yield i
    divisors.isEmpty
  }
}

//for given positive integer n, 
//find all pairs of integers i and j, where 1 ≤ j < i < n such that i + j is prime

def primePairsUgly(n : Int): List[(Int, Int)] = {
    var i = 2
    var j = 1
    var k = 0
    var xs = List[(Int, Int)]()
    while(i < n){
        j = 1
        while(j < i){
            if(isPrimeUgly(i + j)) xs = xs :+ (i, j)
            j+=1
        }
        i += 1
    }
    xs
}

def primePairs(n: Int): List[(Int, Int)] = {
  val pairs = for { i <- 2 to n - 1; j <- 1 to i - 1 if isPrime(i + j)} yield (i, j)

  pairs.toList
}

//create a list with all lines from given file
def fileLinesUgly(file: java.io.File): List[String] = {
  var lines = List[String]()
  var source = Source.fromFile(file)
  var i = source.getLines()
  
  while (i.hasNext) {
    lines = lines :+ i.next() //:+ concatenates strings
  }
  
  source.close()
  lines
}

def fileLines(file: java.io.File): List[String] = {
    val source = Source.fromFile(file)
    val lines = (for (line <- source.getLines()) yield line).toList
    lines
}

//print names of all .scala files which are in filesHere & are non empty
def printNonEmptyUgly(pattern: String): Unit = {
    var filesHere = new java.io.File(".").listFiles
    var i = 0
    while ( i < filesHere.length ){
      var file = filesHere(i)
      if (file.isFile && fileLines(file).length > 0 && file.getName.endsWith(pattern)){
        println(file)
      }
      i += 1
    }
}

def printNonEmpty(pattern: String): Unit = {
    val filesHere = new java.io.File(".").listFiles
    for (fileName <- filesHere.filter(file => file.isFile && fileLines(file).length > 0 && file.getName.endsWith(pattern))) println(fileName)
}

// Quicksort algorithm

// list1::list2 returns
// List[Any] = List(List(1, 2), 3, 4)
def sortUgly(xs: List[Int]): List[Int] = {
  //rearranging the array elements based on the pivot
  def partition(arr: Array[Int], low: Int, high: Int): Int = {
    var pivot = arr(high)
    var i = low - 1
    var j = low

    while (j < high) {
      if (arr(j) < pivot) {
        i += 1
        var temp = arr(i)
        arr(i) = arr(j)
        arr(j) = temp
      }
      j += 1
    }

    var temp = arr(i + 1)
    arr(i + 1) = arr(high)
    arr(high) = temp
    i + 1
  }

  def quickSort(arr: Array[Int], low: Int, high: Int): Unit = {
    if (low < high) {
      var pivotIndex = partition(arr, low, high)
      quickSort(arr, low, pivotIndex - 1)  // sorting the left partition
      quickSort(arr, pivotIndex + 1, high) // sorting the right partition
    }
  }

  // Convert the input list to an array for easier manipulation
  var arr = xs.toArray
  quickSort(arr, 0, arr.length - 1)
  arr.toList
}

// list1:::list2 returns:
// List[Int] = List(1, 2, 3, 4)
def sort(xs: List[Int]): List[Int] = {
  if (xs.isEmpty) xs 
  else {
    val pivot = xs.head
    val left = for (x <- xs.tail if x < pivot) yield x
    val right = for (x <- xs.tail if x >= pivot) yield x
    sort(left) ::: pivot :: sort(right) 
  }
}

@main
def main(): Unit =
  println("ex1:")
  val xs = List(1, 2, 3)
  val ys = List(4, 5, 6)
  println(scalarUgly(xs, ys))
  println(scalar(xs, ys))

  println("\nex2:")
  val zs = List(3,5,1,4,2)
  println(sortUgly(zs))
  println(sort(zs))

  println("\nex3:")
  println(isPrimeUgly(7))
  println(isPrimeUgly(8))
  println(isPrime(7))
  println(isPrime(8))

  println("\nex4:")
  println(primePairsUgly(7))
  println(primePairs(7))

  println("\nex5:")
  // val filesHere = new java.io.File(".").listFiles
  // filesHere.filter(_.isFile).foreach {file => println(fileLinesUgly(file))}
  // filesHere.filter(_.isFile).foreach {file => println(fileLines(file))}
  
  println("\nex6:")
  printNonEmptyUgly(".scala")
  printNonEmpty(".scala")
