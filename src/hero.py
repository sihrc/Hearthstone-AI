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
from general import Hearth
from wrappers import *

import minion as M
import weapon as W
import deck as D

#Python Modules
import random

class Hero(Hearth):
	def init(self):
		self.health = 30
		self.maxHealth = 30
		self.maxMana = 1
		self.shield = 0
		self.mana = 1
		self.weapon = W.NoWeapon()
		self.attack = 0
		self.attacked = 1
		self.secrets = []
		self.hand = []
		self.field = []
		self.deck = D.Deck()
		self.usedPower = False
		self.hero()

	@action
	def heroPower(self, target):
		if self.mana >= 2 and not self.usedPower:
			(success, res) = self.power(target)
			if success:
				self.mana -= 2
				self.usedPower = True
				return res
		else:
			return "%s hero power on %s failed" % (self.name, target.name)

	def playCard(self, target):
		self.hand.remove(target)
		return target.action()
	
	@action	
	def summon(self,target, position):
		#TODO - max minions on field is 7
		if len(self.field) < 7:
			self.field.insert(position, target)
			target.applyEffect(target.effects.battlecry)
		return "%s has summoned %s at position %d" % (self.name, target.name, position)

	def receiveDamage(self, damage):
		self.shield -= damage
		if self.shield < 0:
			self.health += self.shield
			self.shield = 0

	def getDamage(self):
		return self.attack + self.weapon.attack

	@action
	def drawCards(self, num_cards):
		retString = ""
		if num_cards > 1:
			retString = self.drawCards(num_cards - 1) + "\n" 
		if self.deck.isEmpty():
			self.health -= self.deck.overDrawn
			self.deck.overDrawn += 1
			return "%s is out of cards and loses %d health" % (self.name, self.deck.overDrawn - 1)
		elif len(self.hand) >= 10:
			card = self.deck.getCard(self)
			card.discard(self)
			return "%s has a full hand. %s is discarded" % (self.name, card.name)
		else:
			card = self.deck.getCard(self)
			self.hand.append(card)
			return "%s has drawn %s" % (self.name, card.name)

	def turnUpdate(self):
		self.drawCards(1)
		self.maxMana = self.maxMana + 1 if self.maxMana < 10 else self.maxMana
		self.mana = self.maxMana
		self.canAttack = 1
		self.usedPower = False

	def toString(self):
		return "\n".join([self.name, "Health:\t%d" % self.health,\
		 "Shield:\t%d" % self.shield,\
		 "Mana:\t%d" % self.mana,\
		 "Max Mana:\t%d" % self.maxMana,\
		 "Weapon:\t%s" % self.weapon,\
		 "Secret:\n\t%s" % "\t\n".join([str(secret) for secret in self.secrets]),\
		 "Hand:\n\t%s" % "\t\n".join([str(card) for card in self.hand]),\
		 "Field:\n\t%s" % "\t\n".join([str(card) for card in self.field]),\
		 "Deck:\t%d cards" % len(self.deck)])

class Druid(Hero):
	def hero(self):
		self.name = "Malfurion Stormrage"

	def power(self, target):
		self.shield += 1
		self.attack += 1
		return 1, "%s used hero power and gained +1/+1" % (self.name)

class Hunter(Hero):
	def hero(self):
		self.name = "Rexxar"

	def power(self, target):
		target.receiveDamage(2)
		return 1, "%s used hero power on %s and dealt 2 damage" % (self.name, target.name)

class Mage(Hero):
	def hero(self):
		self.name = "Jaina Proudmoore"

	def power(self, target):
		if target.name == "Faerie Dragon":
			return 0, "%s tried to use hero power on %s and failed" % (self.name, target.name)
		target.receiveDamage(1)
		return 1, "%s used hero power on %s and dealt 1 damage" % (self.name, target.name)

class Paladin(Hero):
	def hero(self):
		self.name = "Uther Lightbringer"

	def power(self,target):
		self.summon(M.silver_hand_recruit, -1)
		return 1, "%s used hero power" % (self.name)

class Priest(Hero):
	def hero(self):
		self.name = "Anduin Wrynn"

	def power(self,target):
		target.heal(self)
		return 1, "%s used hero power and healed %s by 2" % (self.name, target.name)

class Rogue(Hero):
	def hero(self):
		self.name = "Valeera Sanguinar"

	def power(self,target):
		self.equip(weapon.dagger)
		return 1, "%s used hero power and equiped a 1/2 weapon" % (self.name)

class Shaman(Hero):
	def hero(self):
		self.name = "Thrall"

	def power(self, target):
		minions = [card for card in [M.healing_totem, M.searing_totem, M.wrath_of_air_totem, M.stoneclaw_totem] if card not in self.field]
		if minions:
			self.summon(random.choice(minions), -1)
			return 1, "%s used hero power" % (self.name)
		return 0, "%s used hero power and failed"

class Warlock(Hero):
	def hero(self):
		self.name = "Gul'dan"

	def power(self,target):
		self.health -= 2
		self.drawCards(1)
		return 1, "%s used hero power and drew a card" % (self.name)

class Warrior(Hero):
	def hero(self):
		self.name = "Garrosh Hellscream"

	def power(self,target):
		self.shield += 2
		return 1, "%s used hero power and gained 2 shield" % (self.name)