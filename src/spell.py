"""
spell.py
Contains definitions for Spell Class - Inherits Hearth

See init functions for what attributes are included

author: chris @ sihrc
"""	

from hearth import *
from wrappers import *
import minion as M

class Spell(Hearth):
	def __init__(self, owner):
		self.health = 0
		self.owner = owner
		self.enemy = owner.enemy
		self.spell()
	
	def toString(self):
		return "%s\n\tcost:%d\n\tdescription:%s" % (self.name, self.cost, self.description)

	def action(self):
		self.cast()

class ancient_secrets(Spell):
	def spell(self):
		self.name = "Ancient Secrets"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Restore 5 Health."

	def cast(self):
		getTarget(self.owner).heal(5)


class ancient_teachings(Spell):
	def spell(self):
		self.name = "Ancient Teachings"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Draw 2 cards."

	def cast(self):
		self.owner.drawCards(2)

class bananas(Spell):
	def spell(self):
		self.name = "Bananas"
		self.classs = "normal"
		self.cost = 1
		self.description = "Give a minion +1\/+1."

	def cast(self):
		while True:
			target = getTarget(self.owner)
			if isinstance(target, M.Minion):
				target.attack += 1
				target.health += 1
				break

class barrel_toss(Spell):
	def spell(self):
		self.name = "Barrel Toss"
		self.classs = "normal"
		self.cost = 1
		self.description = "Deal 2 damage."

class bear_form(Spell):
	def spell(self):
		self.name = "Bear Form"
		self.classs = "Druid"
		self.cost = 0
		self.description = "+2 Health and Taunt."

class cat_form(Spell):
	def spell(self):
		self.name = "Cat Form"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Charge"

class demigods_favor(Spell):
	def spell(self):
		self.name = "Demigod's Favor"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Give your other minions +2\/+2."

class dispel(Spell):
	def spell(self):
		self.name = "Dispel"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Silence a minion."

class dream(Spell):
	def spell(self):
		self.name = "Dream"
		self.classs = "normal"
		self.cost = 0
		self.description = "Return a minion to its owner's hand."

class excess_mana(Spell):
	def spell(self):
		self.name = "Excess Mana"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Draw a card. (You can only have 10 Mana in your tray.)"

class flame_burst(Spell):
	def spell(self):
		self.name = "Flame Burst"
		self.classs = "normal"
		self.cost = 3
		self.description = "Shoot 5 missiles at random enemies for 1 damage each."

class hogger_smash(Spell):
	def spell(self):
		self.name = "Hogger SMASH!"
		self.classs = "normal"
		self.cost = 3
		self.description = "Deal 4 damage."

class i_am_murloc(Spell):
	def spell(self):
		self.name = "I Am Murloc"
		self.classs = "normal"
		self.cost = 4
		self.description = "Summon three, four, or five 1\/1 Murlocs."

class leader_of_the_pack(Spell):
	def spell(self):
		self.name = "Leader of the Pack"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Give your minions +1\/+1."

class legacy_of_the_emperor(Spell):
	def spell(self):
		self.name = "Legacy of the Emperor"
		self.classs = "normal"
		self.cost = 3
		self.description = "Give your minions +2\/+2. (+2 Attack\/+2 Health)"

class mark_of_nature(Spell):
	def spell(self):
		self.name = "Mark of Nature"
		self.classs = "Druid"
		self.cost = 0
		self.description = "+4 Health and Taunt."

class metamorphosis(Spell):
	def spell(self):
		self.name = "Metamorphosis"
		self.classs = "normal"
		self.cost = 6
		self.description = "Do something crazy."

class moonfire(Spell):
	def spell(self):
		self.name = "Moonfire"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Deal 2 damage."

class noooooooooooo(Spell):
	def spell(self):
		self.name = "NOOOOOOOOOOOO"
		self.classs = "normal"
		self.cost = 2
		self.description = "Somehow, the card you USED to have has been deleted.  Here, have this one instead!"

class nightmare(Spell):
	def spell(self):
		self.name = "Nightmare"
		self.classs = "normal"
		self.cost = 0
		self.description = "Give a minion +5\/+5.  At the start of your next turn, destroy it."

class nourish(Spell):
	def spell(self):
		self.name = "Nourish"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Gain 2 Mana Crystals."

class power_of_the_horde(Spell):
	def spell(self):
		self.name = "Power of the Horde"
		self.classs = "normal"
		self.cost = 4
		self.description = "Summon a random Horde Warrior."

class rogues_do_it(Spell):
	def spell(self):
		self.name = "Rogues Do It..."
		self.classs = "normal"
		self.cost = 4
		self.description = "Deal 4 damage. Draw a card."

class rooted(Spell):
	def spell(self):
		self.name = "Rooted"
		self.classs = "Druid"
		self.cost = 0
		self.description = "+5 Health and Taunt."

class shandos_lesson(Spell):
	def spell(self):
		self.name = "Shan'do's Lesson"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Summon two 2\/2 Treants with Taunt."

class starfall(Spell):
	def spell(self):
		self.name = "Starfall"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Deal 5 damage to a minion."

class stomp(Spell):
	def spell(self):
		self.name = "Stomp"
		self.classs = "normal"
		self.cost = 2
		self.description = "Deal 2 damage to all enemies."

class summon_a_panther(Spell):
	def spell(self):
		self.name = "Summon a Panther"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Summon a 3\/2 Panther."

class the_coin(Spell):
	def spell(self):
		self.name = "The Coin"
		self.classs = "normal"
		self.cost = 0
		self.description = "Gain 1 Mana Crystal this turn only."

class transcendence(Spell):
	def spell(self):
		self.name = "Transcendence"
		self.classs = "normal"
		self.cost = 1
		self.description = "Until you kill Cho's minions, he can't be attacked."

class uproot(Spell):
	def spell(self):
		self.name = "Uproot"
		self.classs = "Druid"
		self.cost = 0
		self.description = "+5 Attack."

class will_of_mukla(Spell):
	def spell(self):
		self.name = "Will of Mukla"
		self.classs = "normal"
		self.cost = 3
		self.description = "Restore 8 Health."

class wrath(Spell):
	def spell(self):
		self.name = "Wrath"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Deal 1 damage to a minion. Draw a card."

class ysera_awakens(Spell):
	def spell(self):
		self.name = "Ysera Awakens"
		self.classs = "normal"
		self.cost = 2
		self.description = "Deal 5 damage to all characters except Ysera."

