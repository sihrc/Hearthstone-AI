"""
minion.py
Contains definitions for Minion Class - Inherits Hearth

See init functions for what attributes are included

author: zach @ zhomans
"""	
#Local Modules
from hearth import *
import effect as E


class Minion(Hearth):
	def init (self, health = 1, attack = 0, cost = 0, statuses = []):
		self.health = health
		self.taunt = False
		self.attack = attack
		self.cost = cost
		self.statuses = statuses
		self.minion()
		
	def action(self):
		for effect in self.effects["battlecry"]:
			effect.apply()

	def attack(self, target):
		target.receiveDamage(self.attack)
		self.receiveDamage(target.attack)

	def receiveDamage(self, damage):
		self.effects["receive_damage"].apply()
		self.effects["receive_damage"].apply() # TO-DO Add more
		self.health -= damage
		if self.health <= 0:
			self.die()

	def die(self):
		self.effects["deathrattle"].apply()
		self.removeFromField()

	def removeFromField(self):
		self.owner.field.remove(self)

	def toString(self):
		return "\n".join([self.name, "Health:\t%d" % self.health, "Attack:\t%d" % self.attack, "Mana Cost:\t%d" % self.cost, "%s" % self.statuses])

class avatar_of_the_coin(Minion):
	def minion(self):
		self.name = "Avatar of the Coin"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "normal"
		self.description = "You lost the coin flip, but gained a friend."

class baine_bloodhoof(Minion):
	def minion(self):
		self.name = "Baine Bloodhoof"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = ""

class barrel(Minion):
	def minion(self):
		self.name = "Barrel"
		self.classs = "normal"
		self.attack = 0
		self.health = 2
		self.cost = 0
		self.race = "normal"
		self.description = "Is something in this barrel?"

class boar(Minion):
	def minion(self):
		self.name = "Boar"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = ""

class brewmaster(Minion):
	def minion(self):
		self.name = "Brewmaster"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = ""

class chicken(Minion):
	def minion(self):
		self.name = "Chicken"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "beast"
		self.description = "Hey Chicken!"

class crazed_hunter(Minion):
	def minion(self):
		self.name = "Crazed Hunter"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class crazy_monkey(Minion):
	def minion(self):
		self.name = "Crazy Monkey"
		self.classs = "normal"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = "Battlecry: Throw Bananas."

class damaged_golem(Minion):
	def minion(self):
		self.name = "Damaged Golem"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class defender(Minion):
	def minion(self):
		self.name = "Defender"
		self.classs = "Paladin"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class defias_bandit(Minion):
	def minion(self):
		self.name = "Defias Bandit"
		self.classs = "Rogue"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class devilsaur(Minion):
	def minion(self):
		self.name = "Devilsaur"
		self.classs = "normal"
		self.attack = 5
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = ""

class druid_of_the_claw(Minion):
	def minion(self):
		self.name = "Druid of the Claw"
		self.classs = "Druid"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Charge"

class emboldener_3000(Minion):
	def minion(self):
		self.name = "Emboldener 3000"
		self.classs = "normal"
		self.attack = 0
		self.health = 4
		self.cost = 1
		self.race = "normal"
		self.description = "At the end of your turn, give a random minion +1\/+1."

class emerald_drake(Minion):
	def minion(self):
		self.name = "Emerald Drake"
		self.classs = "normal"
		self.attack = 7
		self.health = 6
		self.cost = 4
		self.race = "dragon"
		self.description = ""

class finkle_einhorn(Minion):
	def minion(self):
		self.name = "Finkle Einhorn"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = ""

class flame_of_azzinoth(Minion):
	def minion(self):
		self.name = "Flame of Azzinoth"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class frog(Minion):
	def minion(self):
		self.name = "Frog"
		self.classs = "normal"
		self.attack = 0
		self.health = 1
		self.cost = 0
		self.race = "beast"
		self.description = "Taunt"

class gnoll(Minion):
	def minion(self):
		self.name = "Gnoll"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Taunt"

class healing_totem(Minion):
	def minion(self):
		self.name = "Healing Totem"
		self.classs = "Shaman"
		self.attack = 0
		self.health = 2
		self.cost = 1
		self.race = "totem"
		self.description = "At the end of your turn, restore 1 Health to all friendly minions."

class hidden_gnome(Minion):
	def minion(self):
		self.name = "Hidden Gnome"
		self.classs = "normal"
		self.attack = 1
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Was hiding in a barrel!"

class homing_chicken(Minion):
	def minion(self):
		self.name = "Homing Chicken"
		self.classs = "normal"
		self.attack = 0
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "At the start of your turn, destroy this minion and draw 3 cards."

class hound(Minion):
	def minion(self):
		self.name = "Hound"
		self.classs = "Hunter"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Charge"

class huffer(Minion):
	def minion(self):
		self.name = "Huffer"
		self.classs = "Hunter"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "beast"
		self.description = "Charge"

class hyena(Minion):
	def minion(self):
		self.name = "Hyena"
		self.classs = "Hunter"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = ""

class imp(Minion):
	def minion(self):
		self.name = "Imp"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "demon"
		self.description = ""

class infernal(Minion):
	def minion(self):
		self.name = "Infernal"
		self.classs = "Warlock"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "demon"
		self.description = ""

class laughing_sister(Minion):
	def minion(self):
		self.name = "Laughing Sister"
		self.classs = "normal"
		self.attack = 3
		self.health = 5
		self.cost = 3
		self.race = "normal"
		self.description = "Can't be targeted by Spells or Hero Powers."

class leokk(Minion):
	def minion(self):
		self.name = "Leokk"
		self.classs = "Hunter"
		self.attack = 2
		self.health = 4
		self.cost = 3
		self.race = "beast"
		self.description = "Other friendly minions have +1 Attack."

class massive_gnoll(Minion):
	def minion(self):
		self.name = "Massive Gnoll"
		self.classs = "normal"
		self.attack = 5
		self.health = 2
		self.cost = 4
		self.race = "normal"
		self.description = ""

class mechanical_dragonling(Minion):
	def minion(self):
		self.name = "Mechanical Dragonling"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class mirror_image(Minion):
	def minion(self):
		self.name = "Mirror Image"
		self.classs = "Mage"
		self.attack = 0
		self.health = 2
		self.cost = 0
		self.race = "normal"
		self.description = "Taunt"

class misha(Minion):
	def minion(self):
		self.name = "Misha"
		self.classs = "Hunter"
		self.attack = 4
		self.health = 4
		self.cost = 3
		self.race = "beast"
		self.description = "Taunt"

class muklas_big_brother(Minion):
	def minion(self):
		self.name = "Mukla's Big Brother"
		self.classs = "normal"
		self.attack = 10
		self.health = 10
		self.cost = 6
		self.race = "normal"
		self.description = "So strong! And only 6 Mana?!"

class murloc(Minion):
	def minion(self):
		self.name = "Murloc"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "murloc"
		self.description = ""

class murloc_scout(Minion):
	def minion(self):
		self.name = "Murloc Scout"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "murloc"
		self.description = ""

class naga_myrmidon(Minion):
	def minion(self):
		self.name = "Naga Myrmidon"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = " "

class pandaren_scout(Minion):
	def minion(self):
		self.name = "Pandaren Scout"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class panther(Minion):
	def minion(self):
		self.name = "Panther"
		self.classs = "Druid"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = ""

class poultryizer(Minion):
	def minion(self):
		self.name = "Poultryizer"
		self.classs = "normal"
		self.attack = 0
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "At the start of your turn, transform a random minion into a 1\/1 Chicken."

class repair_bot(Minion):
	def minion(self):
		self.name = "Repair Bot"
		self.classs = "normal"
		self.attack = 0
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "At the end of your turn, restore 6 Health to a damaged character."

class riverpaw_gnoll(Minion):
	def minion(self):
		self.name = "Riverpaw Gnoll"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class searing_totem(Minion):
	def minion(self):
		self.name = "Searing Totem"
		self.classs = "Shaman"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "totem"
		self.description = ""

class shadopan_monk(Minion):
	def minion(self):
		self.name = "Shado-Pan Monk"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = ""

class shadow_of_nothing(Minion):
	def minion(self):
		self.name = "Shadow of Nothing"
		self.classs = "Priest"
		self.attack = 0
		self.health = 1
		self.cost = 0
		self.race = "normal"
		self.description = "Mindgames whiffed! Your opponent had no minions!"

class sheep(Minion):
	def minion(self):
		self.name = "Sheep"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "beast"
		self.description = ""

class silver_hand_recruit(Minion):
	def minion(self):
		self.name = "Silver Hand Recruit"
		self.classs = "Paladin"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class skeleton(Minion):
	def minion(self):
		self.name = "Skeleton"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = " "

class snake(Minion):
	def minion(self):
		self.name = "Snake"
		self.classs = "Hunter"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "beast"
		self.description = ""

class spellbender(Minion):
	def minion(self):
		self.name = "Spellbender"
		self.classs = "Mage"
		self.attack = 1
		self.health = 3
		self.cost = 0
		self.race = "normal"
		self.description = ""

class spirit_wolf(Minion):
	def minion(self):
		self.name = "Spirit Wolf"
		self.classs = "Shaman"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Taunt"

class squire(Minion):
	def minion(self):
		self.name = "Squire"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = ""

class squirrel(Minion):
	def minion(self):
		self.name = "Squirrel"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = ""

class stoneclaw_totem(Minion):
	def minion(self):
		self.name = "Stoneclaw Totem"
		self.classs = "Shaman"
		self.attack = 0
		self.health = 2
		self.cost = 1
		self.race = "totem"
		self.description = "Taunt"

class treant(Minion):
	def minion(self):
		self.name = "Treant"
		self.classs = "Druid"
		self.attack = 2
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = ""

class violet_apprentice(Minion):
	def minion(self):
		self.name = "Violet Apprentice"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "normal"
		self.description = ""

class whelp(Minion):
	def minion(self):
		self.name = "Whelp"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "dragon"
		self.description = ""

class worthless_imp(Minion):
	def minion(self):
		self.name = "Worthless Imp"
		self.classs = "Warlock"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "demon"
		self.description = "You are out of demons! At least there are always imps..."

class wrath_of_air_totem(Minion):
	def minion(self):
		self.name = "Wrath of Air Totem"
		self.classs = "Shaman"
		self.attack = 0
		self.health = 2
		self.cost = 1
		self.race = "totem"
		self.description = "Spell Damage +1"

