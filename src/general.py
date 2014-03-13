"""
General Classes for all Objects
author: chris @ sihrc
"""
#Local Modules
import effects as E
from wrappers import *

#Python modules
from collections import defaultdict as ddict

class Hearth:
	def __init__(self, owner = None, enemy = None, health = 0, attack = 0, canAttack = 1, effects = ddict(E.Nothing)):
		self.health = health
		self.attack = attack
		self.canAttack = canAttack
		self.owner = owner
		self.enemy = enemy
		self.effects = effects
		self.init()

	def heal(self, amount):
		self.health += amount
		if self.health > self.maxHealth:
			self.health = self.maxHealth

	def getDamage(self):
		return self.attack

	@action
	def attack_(self, target):
		damage = self.getDamage()
		if damage > 0:
			self.canAttack -= 1
			target.receiveDamage(damage)
			self.receiveDamage(target.getDamage())
			return "%s attacked %s dealing %d damage and taking %d damage" % (self.name, target.name, damage, target.getDamage())
		return "%s tried to attack %s but failed" % (self.name, target.name)


	def __str__(self):
		return self.toString()