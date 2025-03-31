package games
import cards._
import deck._
import scala.util.Random.shuffle

class Blackjack(deck: Deck) {
    // Points calculation:
    // Numerical cards as their numerical value = 2 - 10.
    // Face cards (Jack, Queen, King) = 10
    // Ace = 1 or 11 (player could choose)
    
    def calculatePoints(card: Card, currentPoints: Int): Int = card.rank match { //we need currentPoints for ace
        case Numerical(value) => value
        case _: Face => 10
        case Ace => if (currentPoints + 11 <= 21) 11 else 1
    }
    
    // loop taking n cards from the deck, pretty-printing them with points & printing the sum of points on the end
    def play(n: Int): Unit = {
        println(s"Playing Blackjack with $n cards:")
        val (selectedCards, remainingDeck) = deck.cards.splitAt(n)
        var totalPoints = 0
        selectedCards.foreach { card =>
            val points = calculatePoints(card, totalPoints)
            totalPoints += points
            println(s"${card.color} ${card.rank} - Points: $points")
        }
        println(s"Total points: $totalPoints")
    }

    // finds all subsequences of cards which could give 21 points
    lazy val all21: List[List[Card]] = {
        def find21(cards: List[Card], remaining: List[Card], current: List[Card], result: List[List[Card]]): List[List[Card]] = {
            val currentPoints = current.map(c => calculatePoints(c, 0)).sum
            if (currentPoints == 21)
                result :+ current
            else if (currentPoints < 21 && remaining.nonEmpty)
                find21(cards, remaining.tail, remaining.head :: current, result) ++
                find21(cards, remaining.tail, current, result)                
            else
                result
        }
        find21(deck.cards, deck.cards, Nil, Nil)
    }

    // finds and pretty-prints the first subsequence of cards which could give 21 points
    def first21(): Unit = {
        println("First subsequence of cards:")
        all21.headOption match { //headOption selects the first 21 elements
            case Some(cards) =>
                cards.foreach(card => println(s"${card.color} ${card.rank}"))
                println("Total points: 21")
            case None => println("No subsequence of cards.")
        }
    }
}

object Blackjack {
    // creates Blackjack game having numOfDecks-amount of standard decs with random order of cards. For example, with Blackjack(3) deck would have 156 cards
    def apply(numOfDecks: Int): Blackjack = {
        val fullDeck = (for { _ <- 1 to numOfDecks; card <- Deck.standardDeck } yield card).toList
        new Blackjack(new Deck(shuffle(fullDeck)))
    }

}