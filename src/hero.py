"""
hero.py
Contains definitions for Hero Class - Inherits Hearth

Hero:
	Holds information on everything on one side of the field
Specific Heroes:
	Holds name and power information

See init functions for what attributes are included

author: chris @ sihrc
"""	

#Local Modules
import minion
import weapon

from cards import Deck
from general import Hearth

#Python Modules
import random

class Hero(Hearth):
	def init(self, health = 30, shield = 0, mana = 0, weapon = None, secrets = [], hand = [], field = [], deck = Deck()):
		self.health = health
		self.maxHealth = health
		self.maxMana = 10
		self.shield = shield
		self.mana = mana
		self.weapon = weapon
		self.attack = attack
		self.attacked = attacked
		self.secrets = secrets
		self.hand = hand
		self.field = field
		self.deck = deck
		self.usedPower = False
		self.hero()

	def heroPower(self, target):
		if self.mana > 2 and not self.usedPower:
			return self.power()
		else:
			return 0

	def playCard(self, target):
		self.hand.remove(target)
		return target.action()

	def summon(self,target, position):
		#TODO - max minions on field is 7
		if len(self.field) < 7:
			self.field.insert(position, target)
			target.applyEffect(target.effects.battlecry)

	def attack(self, target):
		self.canAttack -= 1
		target.receiveDamge(self.weapon)

	def receiveDamage(self, damage):
		self.shield -= damage
		if self.shield < 0:
			self.health += self.shield
			self.shield = 0

	def drawCards(self, num_cards):
		#TODO - max cards is 10 in hand
		if self.deck.isEmpty():
			self.health -= self.deck.overDrawn
			self.deck.overDrawn += 1
		else:
			self.hand.append(self.deck.getCard())

	def toString(self):
		return "\n".join([self.name, "Health:\t%d" % self.health, "Shield:\t%d" % self.shield, "Mana:\t%d" % self.mana, "Weapon:\t%s" % self.weapon, "Secret:\n\t%s" % "\t\n".join([str(secret) for secret in self.secrets]), "Hand:\n\t%s" % "\t\n".join([str(card) for card in self.hand]), "Field:\n\t%s" % "\t\n".join([str(card) for card in self.field]), "Deck:\t%d cards" % len(self.deck)])

class Druid(Hero):
	def hero(self):
		self.name = "Malfurion Stormrage"

	def power(self):
		self.shield += 1
		self.attack = 1
		return 1

class Hunter(Hero):
	def hero(self):
		self.name = "Rexxar"

	def power(self, target):
		target.receiveDamage(2)
		return 1

class Mage(Hero):
	def hero(self):
		self.name = "Jaina Proudmoore"

	def power(self, target):
		target.receiveDamage(1)
		return 1

class Paladin(Hero):
	def hero(self):
		self.name = "Uther Lightbringer"

	def power(self,target):
		return self.summon(minion.silver_hand_recruit, -1)

class Priest(Hero):
	def hero(self):
		self.name = "Anduin Wrynn"

	def power(self,target):
		target.heal(self)
		return 1

class Rogue(Hero):
	def hero(self):
		self.name = "Valeera Sanguinar"

	def power(self,target):
		self.equip(weapon.dagger)
		return 1

class Shaman(Hero):
	def hero(self):
		self.name = "Thrall"

	def power(self, target):
		minions = [card for card in [minion.healing_totem, minion.searing_totem, minion.wrath_of_air_totem, minion.stoneclaw_totem]if card not in self.field]
		if minions:
			return self.summon(random.choice(minions), -1)
		return 0

class Warlock(Hero):
	def hero(self):
		self.name = "Gul'dan"

	def power(self,target):
		self.health -= 2
		self.drawCards(1)
		return 1

class Warrior(Hero):
	def hero(self):
		self.name = "Garrosh Hellscream"

	def power(self,target):
		self.shield += 2
		return 1