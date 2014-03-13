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
class ashbringer(Weapon):
	def weapon(self):
		self.name = "Ashbringer"
		self.classs = "Paladin"
		self.attack = 5
		self.health = 3
		self.cost = 5
		self.description = ""

class battle_axe(Weapon):
	def weapon(self):
		self.name = "Battle Axe"
		self.classs = "Warrior"
		self.attack = 2
		self.health = 2
		self.cost = 1
		self.description = ""

class blood_fury(Weapon):
	def weapon(self):
		self.name = "Blood Fury"
		self.classs = "Warlock"
		self.attack = 3
		self.health = 8
		self.cost = 3
		self.description = ""

class dual_warglaives(Weapon):
	def weapon(self):
		self.name = "Dual Warglaives"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 6
		self.description = ""

class heavy_axe(Weapon):
	def weapon(self):
		self.name = "Heavy Axe"
		self.classs = "Warrior"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.description = ""

class warglaive_of_azzinoth(Weapon):
	def weapon(self):
		self.name = "Warglaive of Azzinoth"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.description = ""

class wicked_knife(Weapon):
	def weapon(self):
		self.name = "Wicked Knife"
		self.classs = "Rogue"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.description = ""
