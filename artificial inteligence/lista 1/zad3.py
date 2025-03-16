# Idea: For every game we count the score (for two players) based on the Poker rules

import random

def count_score(hand, numbers):
    hand.sort()

    # straight flush (only for numbers)
    if hand[0][0] in numbers and int(hand[0][0])+1 == int(hand[1][0]) and int(hand[1][0])+1 == int(hand[2][0]) and int(hand[2][0])+1 == int(hand[3][0]) and int(hand[3][0])+1 == int(hand[4][0]) and hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        return 8

    # four of a kind
    for i in range(2):
        if hand[i][0] == hand[i+1][0] and hand[i+1][0] == hand[i+2][0] and hand[i+2][0] == hand[i+3][0]:
            return 7
    
    # full house
    if (hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]) or (hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]):
        return 6

    # flush
    if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        return 5
    
    # straight (only for numbers)
    if hand[0][0] in numbers and int(hand[0][0])+1 == int(hand[1][0]) and int(hand[1][0])+1 == int(hand[2][0]) and int(hand[2][0])+1 == int(hand[3][0]) and int(hand[3][0])+1 == int(hand[4][0]):
        return 4

    #three of a kind
    for i in range(3):
        if hand[i][0] == hand[i+1][0] and hand[i+1][0] == hand[i+2][0]:
            return 3
    
    #three of a kind
    for i in range(2):
        for j in range(i+2, 4):
            if hand[i][0] == hand[i+1][0] and hand[j][0] == hand[j+1][0]:
                return 2
     #pair
    for i in range(4):
            if hand[i][0] == hand[i+1][0]:
                return 1
    return 0

def play():
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    faces  = ['Jack', 'Qeen', 'King', 'Ass']
    numbers  = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    deckF = [(v, s) for s in suits for v in faces]
    # deckB = [(v, s) for s in suits for v in numbers]
    deckB = [(v, s) for v in ['8', '9', '10'] for s in suits] # winning deck

    random.seed()
    handF, handB = [], []
    handF = random.sample(deckF, 5)
    handB = random.sample(deckB, 5)

    return count_score(handF,numbers) < count_score(handB,numbers)

def main():
    rounds, score = 1000, 0
    for i in range(rounds):
        if play(): score += 1

    print(f"Player's B win rate: {100 * score / rounds} %")

main()