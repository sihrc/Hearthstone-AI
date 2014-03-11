class Hearth:
	def __init__(self, health = 0, attack = 0, canAttack = 1):
		self.health = health
		self.attack = attack
		self.canAttack = canAttack
		self.init()

	def heal(self, amount):
		self.health += amount
		if self.health > self.maxHealth:
			self.health = self.maxHealth

	def __str__(self):
		return self.toString()