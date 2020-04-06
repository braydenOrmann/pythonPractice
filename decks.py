import random
from cards import *

#class for a standard deck of cards (no jokers)
class standardDeck:
    def __init__(self):
        self.deck = [
            card("ace", "spades"),
            card("two", "spades"),
            card("three", "spades"),
            card("four", "spades"),
            card("five", "spades"),
            card("six", "spades"),
            card("seven", "spades"),
            card("eight", "spades"),
            card("nine", "spades"),
            card("ten", "spades"),
            card("jack", "spades"),
            card("queen", "spades"),
            card("king", "spades"),
            card("ace", "hearts"),
            card("two", "hearts"),
            card("three", "hearts"),
            card("four", "hearts"),
            card("five", "hearts"),
            card("six", "hearts"),
            card("seven", "hearts"),
            card("eight", "hearts"),
            card("nine", "hearts"),
            card("ten", "hearts"),
            card("jack", "hearts"),
            card("queen", "hearts"),
            card("king", "hearts"),
            card("ace", "diamonds"),
            card("two", "diamonds"),
            card("three", "diamonds"),
            card("four", "diamonds"),
            card("five", "diamonds"),
            card("six", "diamonds"),
            card("seven", "diamonds"),
            card("eight", "diamonds"),
            card("nine", "diamonds"),
            card("ten", "diamonds"),
            card("jack", "diamonds"),
            card("queen", "diamonds"),
            card("king", "diamonds"),
            card("ace", "clubs"),
            card("two", "clubs"),
            card("three", "clubs"),
            card("four", "clubs"),
            card("five", "clubs"),
            card("six", "clubs"),
            card("seven", "clubs"),
            card("eight", "clubs"),
            card("nine", "clubs"),
            card("ten", "clubs"),
            card("jack", "clubs"),
            card("queen", "clubs"),
            card("king", "clubs"),
            ]
    def shuffleDeck(self):
        random.shuffle(self.deck)
        print("Deck shuffled.")

newDeck = standardDeck()
for i in range (52):
    print(newDeck.deck[i].value)

newDeck.shuffleDeck()
for i in range (52):
    print(newDeck.deck[i].value)
