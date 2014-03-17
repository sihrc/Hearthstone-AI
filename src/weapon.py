"""
weapon.py
Contains definitions for Weapon Class - Inherits Hearth

See init functions for what attributes are included

author: chris @ sihrc
"""	
from hearth import *
from wrappers import *

class Weapon(Hearth):
	def init(self):
		self.weapon()

	def receiveDamage(self, damage):
		self.health -= 1

	@action
	def attack_(self, target):
		damage = self.getDamage()
		if damage > 0:
			self.canAttack -= 1
			target.receiveDamage(damage) 
			self.receiveDamage(target.getDamage())
			return "%s attacked %s dealing %d damage and loses 1 durability" % (self.owner.name, target.name, self.attack)
		return "%s tried to attack %s but failed" % (self.owner, target.name)

	def toString(self):
		return "%s\n\tattack:%d\n\tdurability:%d\n\tcost:%d\n\tdescription:%s" % (self.name, self.attack, self.health, self.cost, self.description)

class NoWeapon(Weapon):
	def __init__(self):
		self.name = "No Weapon"
		self.attack = 0
		self.health = 1
		self.cost = 0
		self.classs = "Normal"
		self.description = ""

class arcanite_reaper(Weapon):
	def weapon(self):
		self.name = "Arcanite Reaper"
		self.classs = "Warrior"
		self.attack = 5
		self.health = 2
		self.cost = 5
		self.description = ""

class ashbringer(Weapon):
	def weapon(self):
		self.name = "Ashbringer"
		self.classs = "Paladin"
		self.attack = 5
		self.health = 3
		self.cost = 5
		self.description = ""

class assassins_blade(Weapon):
	def weapon(self):
		self.name = "Assassin's Blade"
		self.classs = "Rogue"
		self.attack = 3
		self.health = 4
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

class doomhammer(Weapon):
	def weapon(self):
		self.name = "Doomhammer"
		self.classs = "Shaman"
		self.attack = 2
		self.health = 8
		self.cost = 5
		self.description = "Windfury, Overload: (2)"

class dual_warglaives(Weapon):
	def weapon(self):
		self.name = "Dual Warglaives"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 6
		self.description = ""

class eaglehorn_bow(Weapon):
	def weapon(self):
		self.name = "Eaglehorn Bow"
		self.classs = "Hunter"
		self.attack = 3
		self.health = 2
		self.cost = 3
		self.description = "Whenever a Secret is revealed, gain +1 Durability."

class fiery_war_axe(Weapon):
	def weapon(self):
		self.name = "Fiery War Axe"
		self.classs = "Warrior"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.description = ""

class gladiators_longbow(Weapon):
	def weapon(self):
		self.name = "Gladiator's Longbow"
		self.classs = "Hunter"
		self.attack = 5
		self.health = 2
		self.cost = 7
		self.description = "Your hero is Immune while attacking."

class gorehowl(Weapon):
	def weapon(self):
		self.name = "Gorehowl"
		self.classs = "Warrior"
		self.attack = 7
		self.health = 1
		self.cost = 7
		self.description = "Attacking a minion costs 1 Attack instead of 1 Durability."

class heavy_axe(Weapon):
	def weapon(self):
		self.name = "Heavy Axe"
		self.classs = "Warrior"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.description = ""

class lights_justice(Weapon):
	def weapon(self):
		self.name = "Light's Justice"
		self.classs = "Paladin"
		self.attack = 1
		self.health = 4
		self.cost = 1
		self.description = ""

class perditions_blade(Weapon):
	def weapon(self):
		self.name = "Perdition's Blade"
		self.classs = "Rogue"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.description = "Battlecry: Deal 1 damage. Combo: Deal 2 instead."

class stormforged_axe(Weapon):
	def weapon(self):
		self.name = "Stormforged Axe"
		self.classs = "Shaman"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.description = "Overload: (1)"

class sword_of_justice(Weapon):
	def weapon(self):
		self.name = "Sword of Justice"
		self.classs = "Paladin"
		self.attack = 1
		self.health = 5
		self.cost = 3
		self.description = "Whenever you summon a minion, give it +1\/+1 and this loses 1 Durability."

class truesilver_champion(Weapon):
	def weapon(self):
		self.name = "Truesilver Champion"
		self.classs = "Paladin"
		self.attack = 4
		self.health = 2
		self.cost = 4
		self.description = "Whenever your hero attacks, restore 2 Health to it."

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

