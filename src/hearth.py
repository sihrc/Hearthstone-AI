"""
hearth Classes for all Objects
author: chris @ sihrc
"""
#Local Modules
import effect as E
from wrappers import *


class Hearth:
	def __init__(self, owner = None , enemy = None, health = 0, attack = 0, canAttack = 1):
		self.health = health
		self.attack = attack
		self.canAttack = canAttack
		self.owner = owner
		self.enemy = enemy
		self.effects = E.Effects()
		self.init()

	@action
	def heal(self, amount):
		self.health += amount
		if self.health > self.maxHealth:
			self.health = self.maxHealth
		return "%d health has been restored to %s" % (amount, self.name)

	def update(self):
		if self.health == 0:
			self.die() # TO-DO implement on all classes
		self.update_()

	def update_(self):
		pass

	@action
	def attack_(self, target):
		damage = self.getDamage()
		if damage > 0:
			self.canAttack -= 1
			target.receiveDamage(damage) 
			self.receiveDamage(target.getDamage())
			return "%s attacked %s dealing %d damage and taking %d damage" % (self.name, target.name, damage, target.getDamage())
		return "%s tried to attack %s but failed" % (self.name, target.name)

	def applyEffects(self):
		for effect in self.effects["once"]:
			effect.apply()

	def __str__(self):
		return self.toString()

def getTarget(hero):
	def printChoices(choices):
		for x,choice in enumerate(choices):
			print "%d\t%s" % (x, choice.name)

	choices = [hero, hero.enemy]
	choices.extend(hero.field)
	choices.extend(hero.enemy.field)

	while (True):
		printChoices(choices)
		try:
			a = int(raw_input("Pick a target"))
		except:
			print "Integer please"
			continue
		if int(a) not in xrange(len(choices)):
			print "Invalid"
			continue
		break
	return choices[int(a)]
