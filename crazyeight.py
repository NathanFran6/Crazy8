import random as r

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit= suit
 
suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

deck = []

for val in range(1,14):
    for su in suits:
        x=Card(val, su)
        deck.append(vars(x))

hand= []
for i in range(1,3):
    hand.append(r.sample(deck, 8))

print(hand)


        