package deck

import cards._
import scala.math.max
import scala.io.Source
import scala.util.Random.shuffle

class Deck(val cards: List[Card]) {
    //creates new deck without first card
    def pull(): Deck = {
        cards match {
            case Nil => throw new IllegalStateException("Deck is empty")
            case x::xs => new Deck(xs)
        }
    }

    //creates new deck with given card pushed on top
    def push(c: Card) : Deck = new Deck(c::cards)

    //creates new deck with new card(color, value) pushed on top
    def push(color: Color, value: Rank) = new Deck(Card(color, value)::cards)

    //checks if deck is a standard deck
    val isStandard: Boolean = {
        if(cards.size != 52) false
        cards.toSet == Deck.standardDeck.toSet
    }

    //amount of duplicates of the given card in the deck
    def duplicatesOfCard(card: Card): Int = {
        max(cards.count(_ == card) -1,0)
    }

    //amount of cards in the deck for the given color
    def amountOfColor(color: Color): Int = cards.count(_.color == color)

    //amount of cards in the deck for given numerical card (2, 3, 4, 5, 6, 7, 8, 9, 10)
    def amountOfNumerical(numerical: Numerical): Int = cards.count(_.rank == numerical)

    //amount of all numerical cards in the deck (2, 3, 4, 5, 6, 7, 8, 9, 10)
    val amountWithNumerical: Int = cards.count { card =>
        card.rank match {
            case _: Numerical => true
            case _ => false
        }
    }

    //amount of cards in the deck for the given face (Jack, Queen & King)
    def amountOfFace(face: Face) : Int = cards.count(_.rank == face)

    //amount of all cards in the deck with faces (Jack, Queen & King)
    val amountWithFace: Int = cards.count { card =>
        card.rank match {
            case _: Face => true
            case _ => false
        }
    }
}

object Deck {
    val standardDeck: List[Card] = {
        for {
            color <- List(Clubs, Diamonds, Hearts, Spades)
            rank <- (2 to 10).map(Numerical(_)) ++ List(Ace, Jack, Queen, King)
        } yield Card(color, rank)
    }

    //creates the standard deck with random order of cards
    def apply(): Deck = new Deck(shuffle(standardDeck))
}