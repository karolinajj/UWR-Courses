package plugins

abstract class Pluginable { 
  def plugin(s: String): String = s
}

trait Reverting extends Pluginable {
  abstract override def plugin(text: String): String = super.plugin(text.reverse)
}

trait LowerCasing extends Pluginable {
  abstract override def plugin(text: String): String = super.plugin(text.toLowerCase)
}

trait SingleSpacing extends Pluginable{
  abstract override def plugin(text: String): String = super.plugin(text.replaceAll("\\s+", " "))
}

trait NoSpacing extends Pluginable {
  abstract override def plugin(text: String): String = super.plugin(text.replaceAll(" ", ""))
}

trait DuplicateRemoval extends Pluginable {
  abstract override def plugin(s: String): String = super.plugin(s.filter(c => s.indexOf(c) == s.lastIndexOf(c)))
}


trait Rotating extends Pluginable {
  abstract override def plugin(text: String): String =
    if (text.isEmpty) super.plugin(text)
    else super.plugin(s"${text.last}${text.init}")
}

trait Doubling extends Pluginable { 
  abstract override def plugin(text: String): String = super.plugin(text.zipWithIndex.map {
    case (char, i) if i % 2 == 1 => s"$char$char"
    case (char, i) if i % 2 == 0 => char.toString
  }.mkString)
}

//collect - filters and maps
trait Shortening extends Pluginable {
  abstract override def plugin(text: String): String = super.plugin(text.zipWithIndex.collect {
    case (char, index) if index % 2 == 0 => char
  }.mkString)
}



