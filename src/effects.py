class Effect:
	def __init__(self):
		self.effect()

	def apply(self, heroA, heroB):
		return self.execute(heroA, heroB)

class Nothing(Effect):
	def effect(self):
		self.name = "no effect"

	def execute(heroA, heroB):
		return 1
