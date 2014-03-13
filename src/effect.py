"""
effect.py
Contains definitions for Effect Class

See effect functions for what attributes are included

author: chris @ sihrc
"""	

import hearth as H

class Effect:
	def __init__(self, owner = None, enemy = None, damage = 0):
		self.owner = owner
		self.enemy = enemy
		self.effect()

	def apply(self):
		if self.needTarget:
			self.target = H.getTarget()
		self.execute()


class Nothing(Effect):
	def __init__ (self):
		self.name = "do nothing"
		self.needTarget = False

	def apply(self):
		return 0


class SingleDamage(Effect):
	def effect(self):
		self.name = "deal damage"
		self.needTarget = True

	def execute(self):
		self.target.receiveDamage(self.damage)
		return 1

