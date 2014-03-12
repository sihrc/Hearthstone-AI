class Effect:
	def __init__(self, owner, enemy):
		self.effect()
		self.owner = owner
		self.enemy = enemy

	def apply(self, target):
		return self.execute(heroA, heroB)

class Nothing(Effect):
	def __init__ (self):
		self.name = "do nothing"

	def execute(self):
		return 1

class Damage(Effect):
	def effect(self):
		self.name = "deal damage"

	def execute(self, target):
		return 1

