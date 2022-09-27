
from random import randint


def buildDeck():
    d = []
    clothed = ["Jack", "Queen", "King", "Ace"]
    suit = ["hearts", "clubs", "spades", "diamonds"]

    for x in range(0, 4):
        for i in range(2, 11):
            d += [f"{i} of {suit[x]}"]
        for j in range(0, 4):
            d += [f"{clothed[j]} of {suit[x]}"]

    return d


def shuffleDeck(d):
    shuf = []

    for i in range(0, len(d)):
        rand = randint(0, len(d)-1)
        shuf.insert(i, d[rand])
        d.pop(rand)

    return shuf


def addToHand(deck, hand):
    for i in range(0, 5):
        hand.insert(i, deck[i])
        deck.pop(i)
        print(hand[i])


deck = buildDeck()
deck = shuffleDeck(deck)
hand = []
print("My hand: ")
addToHand(deck, hand)
