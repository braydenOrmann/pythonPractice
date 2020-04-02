#class for a card itself
class card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if (suit == "spades") or (suit == "clubs"):
            self.color = "black"
        elif (suit == "hearts") or (suit == "diamonds"):
            self.color = "red"
