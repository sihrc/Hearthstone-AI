from decks import *
from hero import *

import spell as S
import sys

class Game:
	def __init__(self, playerA, playerB):
		self.playerA = playerA()
		self.playerB = playerB()
		self.setupBoard()

	def setupBoard(self):
		self.playerA.enemy = self.playerB
		self.playerB.enemy = self.playerA
		self.getRandomDecks(self.playerA.__class__.__name__, self.playerB.__class__.__name__)
		self.playerA.drawCards(3)
		self.playerB.drawCards(3)
		self.playerB.hand.append(S.the_coin)

	def addTurn(self, turn):
		turn(self.playerA, self.playerB)

	def getRandomDecks(self, A, B):
		decksA = []
		decksB = []
		for mod in sys.modules:
			if A in mod:
				decksA.append(sys.modules[mod].deck)
			if B in mod:
				decksB.append(sys.modules[mod].deck)
		self.playerA.deck = random.choice(decksA)
		self.playerB.deck = random.choice(decksA)


if __name__ == "__main__":
	a = Game(Druid, Hunter)
