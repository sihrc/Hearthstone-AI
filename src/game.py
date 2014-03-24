#Local Modules
from hearth import *
from wrappers import *

import hero as H
import minion as M
import weapon as W
import effect as E
import spell as S
import game as G
import spell as S
import deck as D
import decks

#Python Modules
import sys, random

class Game:
	def __init__(self, playerA, playerB):
		self.playing = playerA()
		self.waiting = playerB()
		self.turn = 0
		self.start()

	@shutup
	def start(self):
		self.playing.enemy = self.waiting
		self.waiting.enemy = self.playing

		decksA = []
		decksB = []
		for mod in sys.modules:
			if self.playing.__class__.__name__ in mod:
				decksA.append(sys.modules[mod].deck)
			if self.waiting.__class__.__name__ in mod:
				decksB.append(sys.modules[mod].deck)
		self.playing.deck = random.choice(decksA)
		self.waiting.deck = random.choice(decksB)

		self.playing.drawCards(3)
		self.waiting.drawCards(4)
		self.waiting.hand.append(S.the_coin(self.waiting))

	def next(self):
		self.turn += 1
		self.playing.startTurn()
		print game
		print "\n%s's turn" % self.playing.name
		self.getActions()
		self.playing.endTurn()
		print game
		self.switch()

	def switch(self):
		self.playing, self.waiting = self.waiting, self.playing

	def getActions(self):
		action = "invalid"
		while action != "end":
			while action not in ["end", "P", "C", "A"]:
				action = raw_input("P - hero power \t C - play card \t A - attack")
			if action == "P":
				self.playing.power()
			if action == "C":
				index = int(raw_input("Which card?"))
				self.playing.playCard(self.playing.hand[index])
			if action == "A":
				index = int(raw_input("Who?"))
				if index == 0:
					attacker = self.playing
				else:
					attacker = self.playing.field[index - 1]
				index = int(raw_input("Attack Who?"))
				if index == 0:
					target = self.waiting
				else:
					target = self.waiting.field[index - 1]
				attacker.attack(target)
			if action == "end":
				break

	def __str__(self):
		return "==============================\nTurn #%d\n==============================\n%s\n==============================\n%s\n==============================" % (self.turn, self.waiting, self.playing)

if __name__ == "__main__":
	game = Game(H.Druid, H.Hunter)
	game.next()

