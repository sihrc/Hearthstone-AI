"""
minion.py
Contains definitions for Minion Class - Inherits Hearth

Minion:
	Holds information on a minion effects, statuses, and triggers
Specific Minion:
	Holds name and power information

See init functions for what attributes are included

author: zach @ zhomans
"""	
#Local Modules
from general import Hearth

class Minion(Hearth):
	def init (self, health = 1, attack = 0, cost = 0, statuses = [], effects = [], owner = Hero()):
		self.health = health
		self.attack = attack
		self.cost = cost
		self.statuses = statuses
		self.effects = effects
		self.minion()

	def attack(self, target):
		target.receiveDamage(self.attack)
		self.receiveDamage(target.attack)

	def receiveDamage(self, damage):
		self.health -= damage
		if self.health <= 0:
			self.die()

	def die(self):
		self.applyEffect(self.effects.deathrattle)
		self.removeFromField()

	def applyEffect(self, effect):
		if effect != None:
			effect.apply()

	def removeFromField(self):
		owner.field.remove(self)

	def toString(self):
		return "\n".join([self.name, "Health:\t%d" % self.health, "Attack:\t%d" % self.attack, "Mana Cost:\t%d" % self.cost, "%s" % self.statuses])


class silver_hand_recruit(Minion):
	def minion(self):
		self.name = "Silver Hand Recruit"
		self.health = 1
		self.attack = 1
		self.cost = 1

if __name__ == "__main__":
	minion1 = silver_hand_recruit()
	print minion1