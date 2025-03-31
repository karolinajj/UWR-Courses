import cards._
import deck._
import games._
import javax.smartcardio.CardNotPresentException
import scala.util.Random

object Tests {
  def testNumericalRankInRange(): Unit = {
    val validCard = Card(Clubs, Numerical(5))
    try {
      val invalidCard = Card(Clubs, Numerical(1))
    } catch {
      case e: IllegalArgumentException => println("Invalid numerical card.")
    }
  }

  def testCardComparison(): Unit = {
    val card1 = Card(Clubs, Ace)
    val card2 = Card(Clubs, Ace)
    assert(card1 == card2)
  }

  def testPull(): Unit = {
    val card = Card(Clubs, Ace)
    val deck = new Deck(List(card))
    val newDeck = deck.pull()
    assert(newDeck.cards.isEmpty)
  }

  def testPush(): Unit = {
    val card = Card(Clubs, Ace)
    val deck = new Deck(List.empty)
    val newDeck = deck.push(card)
    assert(newDeck.cards == List(card))
  }

  def testIsStandard(): Unit = {
    val standardDeck = Deck.standardDeck
    val deck = new Deck(standardDeck)
    assert(deck.isStandard)
  }

  def testDuplicatesOfCard(): Unit = {
    val card = Card(Clubs, Ace)
    val deck = new Deck(List(card, card, card))
    assert(deck.duplicatesOfCard(card) == 2)
  }

  def testAmountOfColor(): Unit = {
    val cards = List(Card(Clubs, Ace), Card(Clubs, Queen), Card(Diamonds, Jack))
    val deck = new Deck(cards)
    assert(deck.amountOfColor(Clubs) == 2)
    assert(deck.amountOfColor(Diamonds) == 1)
    assert(deck.amountOfColor(Spades) == 0)
  }

  def testAmountOfNumerical(): Unit = {
    val cards = List(Card(Clubs, Numerical(5)), Card(Clubs, Numerical(8)), Card(Diamonds, Ace))
    val deck = new Deck(cards)
    assert(deck.amountOfNumerical(Numerical(5)) == 1)
    assert(deck.amountOfNumerical(Numerical(8)) == 1)
    assert(deck.amountOfNumerical(Numerical(10)) == 0)
  }

  def testAmountWithNumerical(): Unit = {
    val cards = List(Card(Clubs, Numerical(5)), Card(Clubs, Numerical(8)), Card(Diamonds, Ace))
    val deck = new Deck(cards)
    assert(deck.amountWithNumerical == 2)
  }

  def testAmountOfFace(): Unit = {
    val cards = List(Card(Clubs, Jack), Card(Clubs, Queen), Card(Diamonds, Numerical(7)))
    val deck = new Deck(cards)
    assert(deck.amountOfFace(Jack) == 1)
    assert(deck.amountOfFace(Queen) == 1)
    assert(deck.amountOfFace(King) == 0)
  }

  def testAmountWithFace(): Unit = {
    val cards = List(Card(Clubs, Jack), Card(Clubs, Queen), Card(Diamonds, Numerical(7)))
    val deck = new Deck(cards)
    assert(deck.amountWithFace == 2)
  }

  def testPlay(): Unit = {
    val deck = List(
      Card(Clubs, Numerical(2)),
      Card(Clubs, Numerical(9)),
      Card(Clubs, Numerical(8)),
      Card(Diamonds, Numerical(3)),
      Card(Diamonds, Numerical(4))
    )
    val blackjack = new Blackjack(new Deck(deck))
    blackjack.play(3)
  }

  def testCalculatePoints(): Unit = {
    val deck = Deck.standardDeck
    val blackjack = new Blackjack(new Deck(deck))
    val ace = Card(Clubs, Ace)
    val numericalCard = Card(Clubs, Numerical(7))
    val faceCard = Card(Clubs, Jack)

    println(blackjack.calculatePoints(ace, 0))
    println(blackjack.calculatePoints(ace, 10))
    println(blackjack.calculatePoints(numericalCard, 0))
    println(blackjack.calculatePoints(faceCard, 0))
  }

  def testAll21(): Unit = {
    val deck = List(Card(Clubs, Ace), Card(Clubs, Numerical(9)), Card(Clubs, Numerical(8)),
                    Card(Diamonds, Numerical(2)), Card(Diamonds, Numerical(4)))
    val blackjack = new Blackjack(new Deck(deck))
    val all21 = blackjack.all21
    println(all21)
    val firstSequence = all21.head.map(_.rank).toSet
  }

  def testFirst21(): Unit = {
    val deck = List(Card(Clubs, Numerical(2)), Card(Clubs, Numerical(9)), Card(Clubs, Numerical(8)),
                    Card(Diamonds, Numerical(3)), Card(Diamonds, Numerical(4)))
    val blackjack = new Blackjack(new Deck(deck))
    blackjack.first21()
  }

  def main(args: Array[String]): Unit = {
    println("Tests:")
    testNumericalRankInRange()
    testCardComparison()
    testPull()
    testPush()
    testIsStandard()
    testDuplicatesOfCard()
    testAmountOfColor()
    testAmountOfNumerical()
    testAmountWithNumerical()
    testAmountOfFace()
    testAmountWithFace()
    testCalculatePoints()
    testAll21()
    testFirst21()
    testPlay()
  }
}
