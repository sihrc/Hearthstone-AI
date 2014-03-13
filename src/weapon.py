"""
weapon.py
Contains definitions for Weapon Class - Inherits Hearth

See init functions for what attributes are included

author: chris @ sihrc
"""	

from general import Hearth

class Weapon(Hearth):
	def init(self):
		self.weapon()

	def receiveDamage(self, damage):
		self.health -= 1

	def toString(self):
		return "%s\n\tattack:%d\n\tdurability:%d\n\tcost:%d\n\tdescription:%s" % (self.name, self.attack, self.health, self.cost, self.description)

class NoWeapon(Weapon):
	def weapon(self):
		self.name = "No Weapon"
		self.attack = 0
		self.health = 1
		self.cost = 0
		self.classs = "Normal"
		self.description = ""

class arcanite_reaper(Weapon):
	def weapon(self):
		self.name = "Arcanite Reaper"
		self.attack = 5
		self.health = 2
		self.cost = 5
		self.classs = "Warrior"
		self.description = ""

class assassins_blade(Weapon):
	def weapon(self):
		self.name = "Assassin's Blade"
		self.attack = 3
		self.health = 4
		self.cost = 5
		self.classs = "Rogue"
		self.description = ""

class doomhammer(Weapon):
	def weapon(self):
		self.name = "Doomhammer"
		self.attack = 2
		self.health = 8
		self.cost = 5
		self.classs = "Shaman"
		self.description = "Windfury, Overload: (2)"

class eaglehorn_bow(Weapon):
	def weapon(self):
		self.name = "Eaglehorn Bow"
		self.attack = 3
		self.health = 2
		self.cost = 3
		self.classs = "Hunter"
		self.description = "Whenever a Secret is revealed, gain +1 Durability."

class fiery_war_axe(Weapon):
	def weapon(self):
		self.name = "Fiery War Axe"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.classs = "Warrior"
		self.description = ""

class gladiators_longbow(Weapon):
	def weapon(self):
		self.name = "Gladiator's Longbow"
		self.attack = 5
		self.health = 2
		self.cost = 7
		self.classs = "Hunter"
		self.description = "Your hero is Immune while attacking."

class gorehowl(Weapon):
	def weapon(self):
		self.name = "Gorehowl"
		self.attack = 7
		self.health = 1
		self.cost = 7
		self.classs = "Warrior"
		self.description = "Attacking a minion costs 1 Attack instead of 1 Durability."

class lights_justice(Weapon):
	def weapon(self):
		self.name = "Light's Justice"
		self.attack = 1
		self.health = 4
		self.cost = 1
		self.classs = "Paladin"
		self.description = ""

class perditions_blade(Weapon):
	def weapon(self):
		self.name = "Perdition's Blade"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.classs = "Rogue"
		self.description = "Battlecry: Deal 1 damage. Combo: Deal 2 instead."

class stormforged_axe(Weapon):
	def weapon(self):
		self.name = "Stormforged Axe"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.classs = "Shaman"
		self.description = "Overload: (1)"

class sword_of_justice(Weapon):
	def weapon(self):
		self.name = "Sword of Justice"
		self.attack = 1
		self.health = 5
		self.cost = 3
		self.classs = "Paladin"
		self.description = "Whenever you summon a minion, give it +1\/+1 and this loses 1 Durability."

class truesilver_champion(Weapon):
	def weapon(self):
		self.name = "Truesilver Champion"
		self.attack = 4
		self.health = 2
		self.cost = 4
		self.classs = "Paladin"
		self.description = "Whenever your hero attacks, restore 2 Health to it."


if __name__ == "__main__":
	pass