"""
effect.py
Contains definitions for Effect Class

See effect functions for what attributes are included

author: chris @ sihrc
"""	
import hearth as H

class Effects:
	def __init__(self, effects = {}):
		self.effects = effects

	def add(self, name, effect):
		if name not in self.effects:
			self.effects[name] = []
		self.effects[name].append(effect)

	def get(self, name):
		if name in self.effects[name]:
			return self.effects[name]
		else:
			return [Nothing]


class Effect:
	def __init__(self, owner = None, amount = 0, target = None):
		self.owner = owner
		self.enemy = owner.enemy
		self.amount = amount
		self.target = target
		self.effect()	

	def apply(self):
		self.execute()


class Nothing(Effect):
	def __init__ (self):
		self.name = "do nothing"
		self.needTarget = F
	def apply(self):
		return 0


class SingleDamage(Effect):
	def effect(self):
		self.name = "deal damage"

	def execute(self):
		self.target.receiveDamage(self.amount)
		return 1

class Taunt(Effect):
	def effect(self):
		self.name = "Taunt"
		self.needTarget = True

	def execute(self):
		self.origin.taunt = True

class Silence(Effect):
	def effect(self):
		self.name = "Silence"

	def execute(self):
		self.target.effects = H.ddict([E.Nothing])

class Health(Effect):
	def effect(self):
		self.name =  "Grant Health"

	def execute(self):
		self.target.maxHealth += self.amount

class Heal(Effect):
	def effect(self):
		self.name = "Restore Heal"

	def execute(self):
		self.target.heal(self.amount)