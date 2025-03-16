from itertools import combinations

countF = [0] * 9 #[0, 1536, 1728, 768, 0, 0, 288, 48, 0] 
countB = [0] * 9 #[123420, 193536, 36288, 16128, 5100, 484, 1728, 288, 20]
allF = 4368
allB = 376992

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
    faces  = ['jack', 'qeen', 'king', 'as']
    numbers  = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    cardsF = [(v, s) for s in suits for v in faces]
    cardsB = [(v, s) for s in suits for v in numbers]
    cardsB = [(v, s) for s in suits for v in [8,9,10]]
    # cardsB = [(v, s) for v in [8, 9, 10] for s in suits] # winning deck

    decksF = [list(hand) for hand in combinations(cardsF, 5)]
    global allF 
    allF = len(decksF)
    decksB = [list(hand) for hand in combinations(cardsB, 5)]
    global allB
    allB = len(decksB)

    for deck in decksB:
        countB[count_score(deck, numbers)] += 1
    
    for deck in decksF:
        countF[count_score(deck, numbers)] += 1
    
play()
strongerF = 0
strongerB = 0

for i in range(8,0,-1):
    strongerF += countF[i]
    strongerB += countB[i] * (allF - strongerF)

print(strongerB / (allF * allB))
