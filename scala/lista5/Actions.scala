package actions
import plugins._

object Actions {

    // val actionA: Pluginable = new Pluginable with Shortening with Doubling with SingleSpacing
    val actionA: Pluginable = new Pluginable with Doubling with Shortening with SingleSpacing
    val actionB: Pluginable = new Pluginable with Doubling with Shortening with NoSpacing
    val actionC: Pluginable = new Pluginable with LowerCasing with Doubling
    val actionD: Pluginable = new Pluginable with Rotating with DuplicateRemoval
    val actionE: Pluginable = new Pluginable with Reverting with Doubling with Shortening with NoSpacing
    //Function.chain 
    val actionF: Pluginable = new Pluginable {
        override def plugin(s: String): String = (1 to 5).foldLeft(s)((acc, curr_elem) => new Pluginable with Rotating().plugin(acc))
    }
    val actionG: Pluginable = new Pluginable {
        override def plugin(s: String): String = actionB.plugin(actionA.plugin(s))
    }
}