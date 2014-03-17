"""
deck.py

Handles the cards in the deck

author: chris @ sihrc
"""
from random import shuffle

class Deck:
	def __init__(self, cards = []):
		self.cards = cards
		shuffle(self.cards)
		self.overDrawn = 1

	def __len__(self):
		return len(self.cards)

	def addCards(self, cards):
		self.cards = cards
		shuffle(self.cards)
	
	def drawCard(self):
		return self.cards.pop()

	def isEmpty(self):
		return len(self.cards) == 0

	def __len__(self):
		return len(self.cards)

