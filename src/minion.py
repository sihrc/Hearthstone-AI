"""
minion.py
Contains definitions for Minion Class - Inherits Hearth

See init functions for what attributes are included

author: chris @ sihrc
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

class abomination(Minion):
	def minion(self):
		self.name = "Abomination"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt. Deathrattle: Deal 2 damage to ALL characters."

class abusive_sergeant(Minion):
	def minion(self):
		self.name = "Abusive Sergeant"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Battlecry: Give a minion +2 Attack this turn."

class acidic_swamp_ooze(Minion):
	def minion(self):
		self.name = "Acidic Swamp Ooze"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Destroy your opponent's weapon."

class acolyte_of_pain(Minion):
	def minion(self):
		self.name = "Acolyte of Pain"
		self.classs = "normal"
		self.attack = 1
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever this minion takes damage, draw a card."

class alakir_the_windlord(Minion):
	def minion(self):
		self.name = "Al'Akir the Windlord"
		self.classs = "Shaman"
		self.attack = 3
		self.health = 5
		self.cost = 8
		self.race = "normal"
		self.description = "Windfury, Charge, Divine Shield, Taunt"

class alarmobot(Minion):
	def minion(self):
		self.name = "Alarm-o-Bot"
		self.classs = "normal"
		self.attack = 0
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "At the start of your turn, swap this minion with a random one in your hand."

class aldor_peacekeeper(Minion):
	def minion(self):
		self.name = "Aldor Peacekeeper"
		self.classs = "Paladin"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Change an enemy minion's Attack to 1."

class alexstrasza(Minion):
	def minion(self):
		self.name = "Alexstrasza"
		self.classs = "normal"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "dragon"
		self.description = "Battlecry: Set a hero's remaining Health to 15."

class amani_berserker(Minion):
	def minion(self):
		self.name = "Amani Berserker"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Enrage: +3 Attack"

class ancient_brewmaster(Minion):
	def minion(self):
		self.name = "Ancient Brewmaster"
		self.classs = "normal"
		self.attack = 5
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Return a friendly minion from the battlefield to your hand."

class ancient_mage(Minion):
	def minion(self):
		self.name = "Ancient Mage"
		self.classs = "normal"
		self.attack = 2
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give adjacent minions Spell Damage +1."

class ancient_watcher(Minion):
	def minion(self):
		self.name = "Ancient Watcher"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 2
		self.race = "normal"
		self.description = "Can't Attack."

class ancient_of_lore(Minion):
	def minion(self):
		self.name = "Ancient of Lore"
		self.classs = "Druid"
		self.attack = 5
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "Choose One - Draw 2 cards; or Restore 5 Health."

class ancient_of_war(Minion):
	def minion(self):
		self.name = "Ancient of War"
		self.classs = "Druid"
		self.attack = 5
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "Choose One - +5 Attack; or +5 Health and Taunt."

class angry_chicken(Minion):
	def minion(self):
		self.name = "Angry Chicken"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Enrage: +5 Attack."

class arathi_weaponsmith(Minion):
	def minion(self):
		self.name = "Arathi Weaponsmith"
		self.classs = "Warrior"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Equip a 2\/2 weapon."

class arcane_golem(Minion):
	def minion(self):
		self.name = "Arcane Golem"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Charge. Battlecry: Give your opponent a Mana Crystal."

class archmage(Minion):
	def minion(self):
		self.name = "Archmage"
		self.classs = "normal"
		self.attack = 4
		self.health = 7
		self.cost = 6
		self.race = "normal"
		self.description = "Spell Damage +1"

class archmage_antonidas(Minion):
	def minion(self):
		self.name = "Archmage Antonidas"
		self.classs = "Mage"
		self.attack = 5
		self.health = 7
		self.cost = 7
		self.race = "normal"
		self.description = "Whenever you cast a spell, put a 'Fireball' spell into your hand."

class argent_commander(Minion):
	def minion(self):
		self.name = "Argent Commander"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 6
		self.race = "normal"
		self.description = "Charge, Divine Shield"

class argent_protector(Minion):
	def minion(self):
		self.name = "Argent Protector"
		self.classs = "Paladin"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion Divine Shield."

class argent_squire(Minion):
	def minion(self):
		self.name = "Argent Squire"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Divine Shield"

class armorsmith(Minion):
	def minion(self):
		self.name = "Armorsmith"
		self.classs = "Warrior"
		self.attack = 1
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "Whenever a friendly minion takes damage, gain 1 Armor."

class auchenai_soulpriest(Minion):
	def minion(self):
		self.name = "Auchenai Soulpriest"
		self.classs = "Priest"
		self.attack = 3
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Your cards and powers that restore Health now deal damage instead."

class avatar_of_the_coin(Minion):
	def minion(self):
		self.name = "Avatar of the Coin"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "normal"
		self.description = "You lost the coin flip, but gained a friend."

class azure_drake(Minion):
	def minion(self):
		self.name = "Azure Drake"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "dragon"
		self.description = "Spell Damage +1. Battlecry: Draw a card."

class baine_bloodhoof(Minion):
	def minion(self):
		self.name = "Baine Bloodhoof"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = ""

class baron_geddon(Minion):
	def minion(self):
		self.name = "Baron Geddon"
		self.classs = "normal"
		self.attack = 7
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "At the end of your turn, deal 2 damage to ALL other characters."

class barrel(Minion):
	def minion(self):
		self.name = "Barrel"
		self.classs = "normal"
		self.attack = 0
		self.health = 2
		self.cost = 0
		self.race = "normal"
		self.description = "Is something in this barrel?"

class big_game_hunter(Minion):
	def minion(self):
		self.name = "Big Game Hunter"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Destroy a minion with an Attack of 7 or more."

class blood_imp(Minion):
	def minion(self):
		self.name = "Blood Imp"
		self.classs = "Warlock"
		self.attack = 0
		self.health = 1
		self.cost = 1
		self.race = "demon"
		self.description = "Stealth. At the end of your turn, give another random friendly minion +1 Health."

class blood_knight(Minion):
	def minion(self):
		self.name = "Blood Knight"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: All minions lose Divine Shield. Gain +3\/+3 for each Shield lost."

class bloodfen_raptor(Minion):
	def minion(self):
		self.name = "Bloodfen Raptor"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = ""

class bloodmage_thalnos(Minion):
	def minion(self):
		self.name = "Bloodmage Thalnos"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Spell Damage +1. Deathrattle: Draw a card."

class bloodsail_corsair(Minion):
	def minion(self):
		self.name = "Bloodsail Corsair"
		self.classs = "normal"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "pirate"
		self.description = "Battlecry: Remove 1 Durability from your opponent's weapon."

class bloodsail_raider(Minion):
	def minion(self):
		self.name = "Bloodsail Raider"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "pirate"
		self.description = "Battlecry: Gain Attack equal to the Attack of your weapon."

class bluegill_warrior(Minion):
	def minion(self):
		self.name = "Bluegill Warrior"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "murloc"
		self.description = "Charge"

class boar(Minion):
	def minion(self):
		self.name = "Boar"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = ""

class booty_bay_bodyguard(Minion):
	def minion(self):
		self.name = "Booty Bay Bodyguard"
		self.classs = "normal"
		self.attack = 5
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt"

class boulderfist_ogre(Minion):
	def minion(self):
		self.name = "Boulderfist Ogre"
		self.classs = "normal"
		self.attack = 6
		self.health = 7
		self.cost = 6
		self.race = "normal"
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

class cabal_shadow_priest(Minion):
	def minion(self):
		self.name = "Cabal Shadow Priest"
		self.classs = "Priest"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Take control of an enemy minion that has 2 or less Attack."

class cairne_bloodhoof(Minion):
	def minion(self):
		self.name = "Cairne Bloodhoof"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Deathrattle: Summon a 4\/5 Baine Bloodhoof."

class captain_greenskin(Minion):
	def minion(self):
		self.name = "Captain Greenskin"
		self.classs = "normal"
		self.attack = 5
		self.health = 4
		self.cost = 5
		self.race = "pirate"
		self.description = "Battlecry: Give your weapon +1\/+1."

class captains_parrot(Minion):
	def minion(self):
		self.name = "Captain's Parrot"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "beast"
		self.description = "Battlecry: Put a random Pirate from your deck into your hand."

class cenarius(Minion):
	def minion(self):
		self.name = "Cenarius"
		self.classs = "Druid"
		self.attack = 5
		self.health = 8
		self.cost = 9
		self.race = "normal"
		self.description = "Choose One - Give your other minions +2\/+2; or Summon two 2\/2 Treants with Taunt."

class chicken(Minion):
	def minion(self):
		self.name = "Chicken"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "beast"
		self.description = "Hey Chicken!"

class chillwind_yeti(Minion):
	def minion(self):
		self.name = "Chillwind Yeti"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = ""

class coldlight_oracle(Minion):
	def minion(self):
		self.name = "Coldlight Oracle"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "murloc"
		self.description = "Battlecry: Each player draws 2 cards."

class coldlight_seer(Minion):
	def minion(self):
		self.name = "Coldlight Seer"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "murloc"
		self.description = "Battlecry: Give ALL other Murlocs +2 Health."

class core_hound(Minion):
	def minion(self):
		self.name = "Core Hound"
		self.classs = "normal"
		self.attack = 9
		self.health = 5
		self.cost = 7
		self.race = "beast"
		self.description = ""

class crazed_alchemist(Minion):
	def minion(self):
		self.name = "Crazed Alchemist"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Swap the Attack and Health of a minion."

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

class cruel_taskmaster(Minion):
	def minion(self):
		self.name = "Cruel Taskmaster"
		self.classs = "Warrior"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Deal 1 damage to a minion and give it +2 Attack."

class cult_master(Minion):
	def minion(self):
		self.name = "Cult Master"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 4
		self.race = "normal"
		self.description = "Whenever one of your other minions dies, draw a card."

class dalaran_mage(Minion):
	def minion(self):
		self.name = "Dalaran Mage"
		self.classs = "normal"
		self.attack = 1
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "Spell Damage +1"

class damaged_golem(Minion):
	def minion(self):
		self.name = "Damaged Golem"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class dark_iron_dwarf(Minion):
	def minion(self):
		self.name = "Dark Iron Dwarf"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a minion +2 Attack this turn."

class darkscale_healer(Minion):
	def minion(self):
		self.name = "Darkscale Healer"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Restore 2 Health to all friendly characters."

class deathwing(Minion):
	def minion(self):
		self.name = "Deathwing"
		self.classs = "normal"
		self.attack = 12
		self.health = 12
		self.cost = 10
		self.race = "dragon"
		self.description = "Battlecry: Destroy all other minions and discard your hand."

class defender(Minion):
	def minion(self):
		self.name = "Defender"
		self.classs = "Paladin"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class defender_of_argus(Minion):
	def minion(self):
		self.name = "Defender of Argus"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give adjacent minions +1\/+1 and Taunt."

class defias_bandit(Minion):
	def minion(self):
		self.name = "Defias Bandit"
		self.classs = "Rogue"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class defias_ringleader(Minion):
	def minion(self):
		self.name = "Defias Ringleader"
		self.classs = "Rogue"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Combo: Summon a 2\/1 Defias Bandit."

class demolisher(Minion):
	def minion(self):
		self.name = "Demolisher"
		self.classs = "normal"
		self.attack = 1
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "At the start of your turn, deal 2 damage to a random enemy."

class devilsaur(Minion):
	def minion(self):
		self.name = "Devilsaur"
		self.classs = "normal"
		self.attack = 5
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = ""

class dire_wolf_alpha(Minion):
	def minion(self):
		self.name = "Dire Wolf Alpha"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = "Adjacent minions have +1 Attack."

class doomguard(Minion):
	def minion(self):
		self.name = "Doomguard"
		self.classs = "Warlock"
		self.attack = 5
		self.health = 7
		self.cost = 5
		self.race = "demon"
		self.description = "Charge. Battlecry: Discard two random cards."

class doomsayer(Minion):
	def minion(self):
		self.name = "Doomsayer"
		self.classs = "normal"
		self.attack = 0
		self.health = 7
		self.cost = 2
		self.race = "normal"
		self.description = "At the start of your turn, destroy ALL minions."

class dragonling_mechanic(Minion):
	def minion(self):
		self.name = "Dragonling Mechanic"
		self.classs = "normal"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Summon a 2\/1 Mechanical Dragonling."

class dread_corsair(Minion):
	def minion(self):
		self.name = "Dread Corsair"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "pirate"
		self.description = "Taunt. Costs (1) less per Attack of your weapon."

class dread_infernal(Minion):
	def minion(self):
		self.name = "Dread Infernal"
		self.classs = "Warlock"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "demon"
		self.description = "Battlecry: Deal 1 damage to ALL other characters."

class druid_of_the_claw(Minion):
	def minion(self):
		self.name = "Druid of the Claw"
		self.classs = "Druid"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Choose One - Charge; or +2 Health and Taunt."

class dust_devil(Minion):
	def minion(self):
		self.name = "Dust Devil"
		self.classs = "Shaman"
		self.attack = 3
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Windfury. Overload: (2)"

class earth_elemental(Minion):
	def minion(self):
		self.name = "Earth Elemental"
		self.classs = "Shaman"
		self.attack = 7
		self.health = 8
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt. Overload: (3)"

class earthen_ring_farseer(Minion):
	def minion(self):
		self.name = "Earthen Ring Farseer"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Restore 3 Health."

class edwin_vancleef(Minion):
	def minion(self):
		self.name = "Edwin VanCleef"
		self.classs = "Rogue"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Combo: Gain +2\/+2 for each card played earlier this turn."

class elite_tauren_chieftain(Minion):
	def minion(self):
		self.name = "Elite Tauren Chieftain"
		self.classs = "normal"
		self.attack = 5
		self.health = 5
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Give both players the power to ROCK! (with a Power Chord card)"

class elven_archer(Minion):
	def minion(self):
		self.name = "Elven Archer"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Battlecry: Deal 1 damage."

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

class emperor_cobra(Minion):
	def minion(self):
		self.name = "Emperor Cobra"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "beast"
		self.description = "Destroy any minion damaged by this minion."

class ethereal_arcanist(Minion):
	def minion(self):
		self.name = "Ethereal Arcanist"
		self.classs = "Mage"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "If you control a Secret at the end of your turn, gain +2\/+2."

class faceless_manipulator(Minion):
	def minion(self):
		self.name = "Faceless Manipulator"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Choose a minion and become a copy of it."

class faerie_dragon(Minion):
	def minion(self):
		self.name = "Faerie Dragon"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "dragon"
		self.description = "Can't be targeted by Spells or Hero Powers."

class felguard(Minion):
	def minion(self):
		self.name = "Felguard"
		self.classs = "Warlock"
		self.attack = 3
		self.health = 5
		self.cost = 3
		self.race = "demon"
		self.description = "Taunt. Battlecry: Destroy one of your Mana Crystals."

class fen_creeper(Minion):
	def minion(self):
		self.name = "Fen Creeper"
		self.classs = "normal"
		self.attack = 3
		self.health = 6
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt"

class finkle_einhorn(Minion):
	def minion(self):
		self.name = "Finkle Einhorn"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = ""

class fire_elemental(Minion):
	def minion(self):
		self.name = "Fire Elemental"
		self.classs = "Shaman"
		self.attack = 6
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Deal 3 damage."

class flame_imp(Minion):
	def minion(self):
		self.name = "Flame Imp"
		self.classs = "Warlock"
		self.attack = 3
		self.health = 2
		self.cost = 1
		self.race = "demon"
		self.description = "Battlecry: Deal 3 damage to your hero."

class flame_of_azzinoth(Minion):
	def minion(self):
		self.name = "Flame of Azzinoth"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class flametongue_totem(Minion):
	def minion(self):
		self.name = "Flametongue Totem"
		self.classs = "Shaman"
		self.attack = 0
		self.health = 3
		self.cost = 2
		self.race = "totem"
		self.description = "Adjacent minions have +2 Attack."

class flesheating_ghoul(Minion):
	def minion(self):
		self.name = "Flesheating Ghoul"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever a minion dies, gain +1 Attack."

class frog(Minion):
	def minion(self):
		self.name = "Frog"
		self.classs = "normal"
		self.attack = 0
		self.health = 1
		self.cost = 0
		self.race = "beast"
		self.description = "Taunt"

class frost_elemental(Minion):
	def minion(self):
		self.name = "Frost Elemental"
		self.classs = "normal"
		self.attack = 5
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Freeze a character."

class frostwolf_grunt(Minion):
	def minion(self):
		self.name = "Frostwolf Grunt"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Taunt"

class frostwolf_warlord(Minion):
	def minion(self):
		self.name = "Frostwolf Warlord"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Gain +1\/+1 for each other friendly minion on the battlefield."

class frothing_berserker(Minion):
	def minion(self):
		self.name = "Frothing Berserker"
		self.classs = "Warrior"
		self.attack = 2
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever a minion takes damage, gain +1 Attack."

class gadgetzan_auctioneer(Minion):
	def minion(self):
		self.name = "Gadgetzan Auctioneer"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Whenever you cast a spell, draw a card."

class gelbin_mekkatorque(Minion):
	def minion(self):
		self.name = "Gelbin Mekkatorque"
		self.classs = "normal"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Summon an AWESOME invention."

class gnoll(Minion):
	def minion(self):
		self.name = "Gnoll"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Taunt"

class gnomish_inventor(Minion):
	def minion(self):
		self.name = "Gnomish Inventor"
		self.classs = "normal"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Draw a card."

class goldshire_footman(Minion):
	def minion(self):
		self.name = "Goldshire Footman"
		self.classs = "normal"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = "Taunt"

class grimscale_oracle(Minion):
	def minion(self):
		self.name = "Grimscale Oracle"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "murloc"
		self.description = "ALL other Murlocs have +1 Attack."

class grommash_hellscream(Minion):
	def minion(self):
		self.name = "Grommash Hellscream"
		self.classs = "Warrior"
		self.attack = 4
		self.health = 9
		self.cost = 8
		self.race = "normal"
		self.description = "Charge.  Enrage: +6 Attack"

class gruul(Minion):
	def minion(self):
		self.name = "Gruul"
		self.classs = "normal"
		self.attack = 7
		self.health = 7
		self.cost = 8
		self.race = "normal"
		self.description = "At the end of each turn, gain +1\/+1 ."

class guardian_of_kings(Minion):
	def minion(self):
		self.name = "Guardian of Kings"
		self.classs = "Paladin"
		self.attack = 5
		self.health = 6
		self.cost = 7
		self.race = "normal"
		self.description = "Battlecry: Restore 6 Health to your hero."

class gurubashi_berserker(Minion):
	def minion(self):
		self.name = "Gurubashi Berserker"
		self.classs = "normal"
		self.attack = 2
		self.health = 7
		self.cost = 5
		self.race = "normal"
		self.description = "Whenever this minion takes damage, gain +3 Attack."

class harrison_jones(Minion):
	def minion(self):
		self.name = "Harrison Jones"
		self.classs = "normal"
		self.attack = 5
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Destroy your opponent's weapon and draw cards equal to its Durability."

class harvest_golem(Minion):
	def minion(self):
		self.name = "Harvest Golem"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Deathrattle: Summon a 2\/1 Damaged Golem."

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

class hogger(Minion):
	def minion(self):
		self.name = "Hogger"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 6
		self.race = "normal"
		self.description = "At the end of your turn, summon a 2\/2 Gnoll with Taunt."

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

class houndmaster(Minion):
	def minion(self):
		self.name = "Houndmaster"
		self.classs = "Hunter"
		self.attack = 4
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a friendly Beast +2\/+2 and Taunt."

class huffer(Minion):
	def minion(self):
		self.name = "Huffer"
		self.classs = "Hunter"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "beast"
		self.description = "Charge"

class hungry_crab(Minion):
	def minion(self):
		self.name = "Hungry Crab"
		self.classs = "normal"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "beast"
		self.description = "Battlecry: Destroy a Murloc and gain +2\/+2."

class hyena(Minion):
	def minion(self):
		self.name = "Hyena"
		self.classs = "Hunter"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = ""

class illidan_stormrage(Minion):
	def minion(self):
		self.name = "Illidan Stormrage"
		self.classs = "normal"
		self.attack = 7
		self.health = 5
		self.cost = 6
		self.race = "demon"
		self.description = "Whenever you play a card, summon a 2\/1 Flame of Azzinoth."

class imp(Minion):
	def minion(self):
		self.name = "Imp"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "demon"
		self.description = ""

class imp_master(Minion):
	def minion(self):
		self.name = "Imp Master"
		self.classs = "normal"
		self.attack = 1
		self.health = 5
		self.cost = 3
		self.race = "normal"
		self.description = "At the end of your turn, deal 1 damage to this minion and summon a 1\/1 Imp."

class infernal(Minion):
	def minion(self):
		self.name = "Infernal"
		self.classs = "Warlock"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "demon"
		self.description = ""

class injured_blademaster(Minion):
	def minion(self):
		self.name = "Injured Blademaster"
		self.classs = "normal"
		self.attack = 4
		self.health = 7
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Deal 4 damage to HIMSELF."

class ironbark_protector(Minion):
	def minion(self):
		self.name = "Ironbark Protector"
		self.classs = "Druid"
		self.attack = 8
		self.health = 8
		self.cost = 8
		self.race = "normal"
		self.description = "Taunt"

class ironbeak_owl(Minion):
	def minion(self):
		self.name = "Ironbeak Owl"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "beast"
		self.description = "Battlecry: Silence a minion."

class ironforge_rifleman(Minion):
	def minion(self):
		self.name = "Ironforge Rifleman"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Deal 1 damage."

class ironfur_grizzly(Minion):
	def minion(self):
		self.name = "Ironfur Grizzly"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "beast"
		self.description = "Taunt"

class jungle_panther(Minion):
	def minion(self):
		self.name = "Jungle Panther"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "beast"
		self.description = "Stealth"

class keeper_of_the_grove(Minion):
	def minion(self):
		self.name = "Keeper of the Grove"
		self.classs = "Druid"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Choose One - Deal 2 damage; or Silence a minion."

class kidnapper(Minion):
	def minion(self):
		self.name = "Kidnapper"
		self.classs = "Rogue"
		self.attack = 5
		self.health = 3
		self.cost = 6
		self.race = "normal"
		self.description = "Combo: Return a minion to its owner's hand."

class king_krush(Minion):
	def minion(self):
		self.name = "King Krush"
		self.classs = "Hunter"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "beast"
		self.description = "Charge"

class king_mukla(Minion):
	def minion(self):
		self.name = "King Mukla"
		self.classs = "normal"
		self.attack = 5
		self.health = 5
		self.cost = 3
		self.race = "beast"
		self.description = "Battlecry: Give your opponent 2 Bananas."

class kirin_tor_mage(Minion):
	def minion(self):
		self.name = "Kirin Tor Mage"
		self.classs = "Mage"
		self.attack = 4
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: The next Secret you play this turn costs (0)."

class knife_juggler(Minion):
	def minion(self):
		self.name = "Knife Juggler"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "After you summon a minion, deal 1 damage to a random enemy."

class kobold_geomancer(Minion):
	def minion(self):
		self.name = "Kobold Geomancer"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Spell Damage +1"

class korkron_elite(Minion):
	def minion(self):
		self.name = "Kor'kron Elite"
		self.classs = "Warrior"
		self.attack = 4
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Charge"

class laughing_sister(Minion):
	def minion(self):
		self.name = "Laughing Sister"
		self.classs = "normal"
		self.attack = 3
		self.health = 5
		self.cost = 3
		self.race = "normal"
		self.description = "Can't be targeted by Spells or Hero Powers."

class leeroy_jenkins(Minion):
	def minion(self):
		self.name = "Leeroy Jenkins"
		self.classs = "normal"
		self.attack = 6
		self.health = 2
		self.cost = 4
		self.race = "normal"
		self.description = "Charge. Battlecry: Summon two 1\/1 Whelps for your opponent."

class leokk(Minion):
	def minion(self):
		self.name = "Leokk"
		self.classs = "Hunter"
		self.attack = 2
		self.health = 4
		self.cost = 3
		self.race = "beast"
		self.description = "Other friendly minions have +1 Attack."

class leper_gnome(Minion):
	def minion(self):
		self.name = "Leper Gnome"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Deathrattle: Deal 2 damage to the enemy hero."

class lightspawn(Minion):
	def minion(self):
		self.name = "Lightspawn"
		self.classs = "Priest"
		self.attack = 0
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "This minion's Attack is always equal to its Health."

class lightwarden(Minion):
	def minion(self):
		self.name = "Lightwarden"
		self.classs = "normal"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever a character is healed, gain +2 Attack."

class lightwell(Minion):
	def minion(self):
		self.name = "Lightwell"
		self.classs = "Priest"
		self.attack = 0
		self.health = 5
		self.cost = 2
		self.race = "normal"
		self.description = "At the start of your turn, restore 3 Health to a damaged friendly character."

class loot_hoarder(Minion):
	def minion(self):
		self.name = "Loot Hoarder"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Deathrattle: Draw a card."

class lord_jaraxxus(Minion):
	def minion(self):
		self.name = "Lord Jaraxxus"
		self.classs = "Warlock"
		self.attack = 3
		self.health = 15
		self.cost = 9
		self.race = "demon"
		self.description = "Battlecry: Destroy your hero and replace him with Lord Jaraxxus."

class lord_of_the_arena(Minion):
	def minion(self):
		self.name = "Lord of the Arena"
		self.classs = "normal"
		self.attack = 6
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Taunt"

class lorewalker_cho(Minion):
	def minion(self):
		self.name = "Lorewalker Cho"
		self.classs = "normal"
		self.attack = 0
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "Whenever a player casts a spell, put a copy into the other player\u2019s hand."

class mad_bomber(Minion):
	def minion(self):
		self.name = "Mad Bomber"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Deal 3 damage randomly split between all other characters."

class magma_rager(Minion):
	def minion(self):
		self.name = "Magma Rager"
		self.classs = "normal"
		self.attack = 5
		self.health = 1
		self.cost = 3
		self.race = "normal"
		self.description = ""

class malygos(Minion):
	def minion(self):
		self.name = "Malygos"
		self.classs = "normal"
		self.attack = 4
		self.health = 12
		self.cost = 9
		self.race = "dragon"
		self.description = "Spell Damage +5"

class mana_addict(Minion):
	def minion(self):
		self.name = "Mana Addict"
		self.classs = "normal"
		self.attack = 1
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Whenever you cast a spell, gain +2 Attack this turn."

class mana_tide_totem(Minion):
	def minion(self):
		self.name = "Mana Tide Totem"
		self.classs = "Shaman"
		self.attack = 0
		self.health = 3
		self.cost = 3
		self.race = "totem"
		self.description = "At the end of your turn, draw a card."

class mana_wraith(Minion):
	def minion(self):
		self.name = "Mana Wraith"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "ALL minions cost (1) more."

class mana_wyrm(Minion):
	def minion(self):
		self.name = "Mana Wyrm"
		self.classs = "Mage"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever you cast a spell, gain +1 Attack."

class massive_gnoll(Minion):
	def minion(self):
		self.name = "Massive Gnoll"
		self.classs = "normal"
		self.attack = 5
		self.health = 2
		self.cost = 4
		self.race = "normal"
		self.description = ""

class master_swordsmith(Minion):
	def minion(self):
		self.name = "Master Swordsmith"
		self.classs = "normal"
		self.attack = 1
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "At the end of your turn, give another random friendly minion +1 Attack."

class master_of_disguise(Minion):
	def minion(self):
		self.name = "Master of Disguise"
		self.classs = "Rogue"
		self.attack = 4
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion Stealth."

class mechanical_dragonling(Minion):
	def minion(self):
		self.name = "Mechanical Dragonling"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class millhouse_manastorm(Minion):
	def minion(self):
		self.name = "Millhouse Manastorm"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Enemy spells cost (0) next turn."

class mind_control_tech(Minion):
	def minion(self):
		self.name = "Mind Control Tech"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: If your opponent has 4 or more minions, take control of one at random."

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

class mogushan_warden(Minion):
	def minion(self):
		self.name = "Mogu'shan Warden"
		self.classs = "normal"
		self.attack = 1
		self.health = 7
		self.cost = 4
		self.race = "normal"
		self.description = "Taunt"

class molten_giant(Minion):
	def minion(self):
		self.name = "Molten Giant"
		self.classs = "normal"
		self.attack = 8
		self.health = 8
		self.cost = 20
		self.race = "normal"
		self.description = "Costs (1) less for each damage your hero has taken."

class mountain_giant(Minion):
	def minion(self):
		self.name = "Mountain Giant"
		self.classs = "normal"
		self.attack = 8
		self.health = 8
		self.cost = 12
		self.race = "normal"
		self.description = "Costs (1) less for each other card in your hand."

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

class murloc_raider(Minion):
	def minion(self):
		self.name = "Murloc Raider"
		self.classs = "normal"
		self.attack = 2
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

class murloc_tidecaller(Minion):
	def minion(self):
		self.name = "Murloc Tidecaller"
		self.classs = "normal"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "murloc"
		self.description = "Whenever a Murloc is summoned, gain +1 Attack."

class murloc_tidehunter(Minion):
	def minion(self):
		self.name = "Murloc Tidehunter"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "murloc"
		self.description = "Battlecry: Summon a 1\/1 Murloc Scout."

class murloc_warleader(Minion):
	def minion(self):
		self.name = "Murloc Warleader"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "murloc"
		self.description = "ALL other Murlocs have +2\/+1."

class naga_myrmidon(Minion):
	def minion(self):
		self.name = "Naga Myrmidon"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = " "

class nat_pagle(Minion):
	def minion(self):
		self.name = "Nat Pagle"
		self.classs = "normal"
		self.attack = 0
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "At the start of your turn, you have a 50% chance to draw an extra card."

class nightblade(Minion):
	def minion(self):
		self.name = "Nightblade"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Deal 3 damage to the enemy hero."

class northshire_cleric(Minion):
	def minion(self):
		self.name = "Northshire Cleric"
		self.classs = "Priest"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever a minion is healed, draw a card."

class novice_engineer(Minion):
	def minion(self):
		self.name = "Novice Engineer"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Draw a card."

class nozdormu(Minion):
	def minion(self):
		self.name = "Nozdormu"
		self.classs = "normal"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "dragon"
		self.description = "Players only have 15 seconds to take their turns."

class oasis_snapjaw(Minion):
	def minion(self):
		self.name = "Oasis Snapjaw"
		self.classs = "normal"
		self.attack = 2
		self.health = 7
		self.cost = 4
		self.race = "beast"
		self.description = ""

class ogre_magi(Minion):
	def minion(self):
		self.name = "Ogre Magi"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Spell Damage +1"

class old_murkeye(Minion):
	def minion(self):
		self.name = "Old Murk-Eye"
		self.classs = "normal"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "murloc"
		self.description = "Charge. Has +1 Attack for each other Murloc on the battlefield."

class onyxia(Minion):
	def minion(self):
		self.name = "Onyxia"
		self.classs = "normal"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "dragon"
		self.description = "Battlecry: Summon 1\/1 Whelps until your side of the battlefield is full."

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

class patient_assassin(Minion):
	def minion(self):
		self.name = "Patient Assassin"
		self.classs = "Rogue"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Stealth. Destroy any minion damaged by this minion."

class pintsized_summoner(Minion):
	def minion(self):
		self.name = "Pint-Sized Summoner"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "The first minion you play each turn costs (1) less."

class pit_lord(Minion):
	def minion(self):
		self.name = "Pit Lord"
		self.classs = "Warlock"
		self.attack = 5
		self.health = 6
		self.cost = 4
		self.race = "demon"
		self.description = "Battlecry: Deal 5 damage to your hero."

class poultryizer(Minion):
	def minion(self):
		self.name = "Poultryizer"
		self.classs = "normal"
		self.attack = 0
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "At the start of your turn, transform a random minion into a 1\/1 Chicken."

class priestess_of_elune(Minion):
	def minion(self):
		self.name = "Priestess of Elune"
		self.classs = "normal"
		self.attack = 5
		self.health = 4
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Restore 4 Health to your hero."

class prophet_velen(Minion):
	def minion(self):
		self.name = "Prophet Velen"
		self.classs = "Priest"
		self.attack = 7
		self.health = 7
		self.cost = 7
		self.race = "normal"
		self.description = "Double the damage and healing of your spells and Hero Power."

class questing_adventurer(Minion):
	def minion(self):
		self.name = "Questing Adventurer"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever you play a card, gain +1\/+1."

class raging_worgen(Minion):
	def minion(self):
		self.name = "Raging Worgen"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Enrage: Windfury and +1 Attack"

class ragnaros_the_firelord(Minion):
	def minion(self):
		self.name = "Ragnaros the Firelord"
		self.classs = "normal"
		self.attack = 8
		self.health = 8
		self.cost = 8
		self.race = "normal"
		self.description = "Can't Attack.  At the end of your turn, deal 8 damage to a random enemy."

class raid_leader(Minion):
	def minion(self):
		self.name = "Raid Leader"
		self.classs = "normal"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Your other minions have +1 Attack."

class ravenholdt_assassin(Minion):
	def minion(self):
		self.name = "Ravenholdt Assassin"
		self.classs = "normal"
		self.attack = 7
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "Stealth"

class razorfen_hunter(Minion):
	def minion(self):
		self.name = "Razorfen Hunter"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Summon a 1\/1 Boar."

class reckless_rocketeer(Minion):
	def minion(self):
		self.name = "Reckless Rocketeer"
		self.classs = "normal"
		self.attack = 5
		self.health = 2
		self.cost = 6
		self.race = "normal"
		self.description = "Charge"

class repair_bot(Minion):
	def minion(self):
		self.name = "Repair Bot"
		self.classs = "normal"
		self.attack = 0
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "At the end of your turn, restore 6 Health to a damaged character."

class river_crocolisk(Minion):
	def minion(self):
		self.name = "River Crocolisk"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "beast"
		self.description = ""

class riverpaw_gnoll(Minion):
	def minion(self):
		self.name = "Riverpaw Gnoll"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class si7_agent(Minion):
	def minion(self):
		self.name = "SI:7 Agent"
		self.classs = "Rogue"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Combo: Deal 2 damage."

class savannah_highmane(Minion):
	def minion(self):
		self.name = "Savannah Highmane"
		self.classs = "Hunter"
		self.attack = 6
		self.health = 5
		self.cost = 6
		self.race = "beast"
		self.description = "Deathrattle: Summon two 2\/2 Hyenas."

class scarlet_crusader(Minion):
	def minion(self):
		self.name = "Scarlet Crusader"
		self.classs = "normal"
		self.attack = 3
		self.health = 1
		self.cost = 3
		self.race = "normal"
		self.description = "Divine Shield"

class scavenging_hyena(Minion):
	def minion(self):
		self.name = "Scavenging Hyena"
		self.classs = "Hunter"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = "Whenever a friendly Beast dies, gain +2\/+1."

class sea_giant(Minion):
	def minion(self):
		self.name = "Sea Giant"
		self.classs = "normal"
		self.attack = 8
		self.health = 8
		self.cost = 10
		self.race = "normal"
		self.description = "Costs (1) less for each other minion on the battlefield."

class searing_totem(Minion):
	def minion(self):
		self.name = "Searing Totem"
		self.classs = "Shaman"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "totem"
		self.description = ""

class secretkeeper(Minion):
	def minion(self):
		self.name = "Secretkeeper"
		self.classs = "normal"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever a Secret is played, gain +1\/+1."

class senjin_shieldmasta(Minion):
	def minion(self):
		self.name = "Sen'jin Shieldmasta"
		self.classs = "normal"
		self.attack = 3
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Taunt"

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

class shattered_sun_cleric(Minion):
	def minion(self):
		self.name = "Shattered Sun Cleric"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion +1\/+1."

class sheep(Minion):
	def minion(self):
		self.name = "Sheep"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "beast"
		self.description = ""

class shieldbearer(Minion):
	def minion(self):
		self.name = "Shieldbearer"
		self.classs = "normal"
		self.attack = 0
		self.health = 4
		self.cost = 1
		self.race = "normal"
		self.description = "Taunt"

class silver_hand_knight(Minion):
	def minion(self):
		self.name = "Silver Hand Knight"
		self.classs = "normal"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Summon a 2\/2 Squire."

class silver_hand_recruit(Minion):
	def minion(self):
		self.name = "Silver Hand Recruit"
		self.classs = "Paladin"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = ""

class silverback_patriarch(Minion):
	def minion(self):
		self.name = "Silverback Patriarch"
		self.classs = "normal"
		self.attack = 1
		self.health = 4
		self.cost = 3
		self.race = "beast"
		self.description = "Taunt"

class silvermoon_guardian(Minion):
	def minion(self):
		self.name = "Silvermoon Guardian"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Divine Shield"

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

class sorcerers_apprentice(Minion):
	def minion(self):
		self.name = "Sorcerer's Apprentice"
		self.classs = "Mage"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Your spells cost (1) less."

class southsea_captain(Minion):
	def minion(self):
		self.name = "Southsea Captain"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "pirate"
		self.description = "Your other Pirates have +1\/+1."

class southsea_deckhand(Minion):
	def minion(self):
		self.name = "Southsea Deckhand"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "pirate"
		self.description = "Has Charge while you have a weapon equipped."

class spellbender(Minion):
	def minion(self):
		self.name = "Spellbender"
		self.classs = "Mage"
		self.attack = 1
		self.health = 3
		self.cost = 0
		self.race = "normal"
		self.description = ""

class spellbreaker(Minion):
	def minion(self):
		self.name = "Spellbreaker"
		self.classs = "normal"
		self.attack = 4
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Silence a minion."

class spirit_wolf(Minion):
	def minion(self):
		self.name = "Spirit Wolf"
		self.classs = "Shaman"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Taunt"

class spiteful_smith(Minion):
	def minion(self):
		self.name = "Spiteful Smith"
		self.classs = "normal"
		self.attack = 4
		self.health = 6
		self.cost = 5
		self.race = "normal"
		self.description = "Enrage: Your weapon has +2 Attack."

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

class stampeding_kodo(Minion):
	def minion(self):
		self.name = "Stampeding Kodo"
		self.classs = "normal"
		self.attack = 3
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = "Battlecry: Destroy a random enemy minion with 2 or less Attack."

class starving_buzzard(Minion):
	def minion(self):
		self.name = "Starving Buzzard"
		self.classs = "Hunter"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "beast"
		self.description = "Whenever you summon a Beast, draw a card."

class stoneclaw_totem(Minion):
	def minion(self):
		self.name = "Stoneclaw Totem"
		self.classs = "Shaman"
		self.attack = 0
		self.health = 2
		self.cost = 1
		self.race = "totem"
		self.description = "Taunt"

class stonetusk_boar(Minion):
	def minion(self):
		self.name = "Stonetusk Boar"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Charge"

class stormpike_commando(Minion):
	def minion(self):
		self.name = "Stormpike Commando"
		self.classs = "normal"
		self.attack = 4
		self.health = 2
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Deal 2 damage."

class stormwind_champion(Minion):
	def minion(self):
		self.name = "Stormwind Champion"
		self.classs = "normal"
		self.attack = 6
		self.health = 6
		self.cost = 7
		self.race = "normal"
		self.description = "Your other minions have +1\/+1."

class stormwind_knight(Minion):
	def minion(self):
		self.name = "Stormwind Knight"
		self.classs = "normal"
		self.attack = 2
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Charge"

class stranglethorn_tiger(Minion):
	def minion(self):
		self.name = "Stranglethorn Tiger"
		self.classs = "normal"
		self.attack = 5
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = "Stealth"

class succubus(Minion):
	def minion(self):
		self.name = "Succubus"
		self.classs = "Warlock"
		self.attack = 4
		self.health = 3
		self.cost = 2
		self.race = "demon"
		self.description = "Battlecry: Discard a random card."

class summoning_portal(Minion):
	def minion(self):
		self.name = "Summoning Portal"
		self.classs = "Warlock"
		self.attack = 0
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Your minions cost (2) less, but not less than (1)."

class sunfury_protector(Minion):
	def minion(self):
		self.name = "Sunfury Protector"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Give adjacent minions Taunt."

class sunwalker(Minion):
	def minion(self):
		self.name = "Sunwalker"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Taunt. Divine Shield"

class sylvanas_windrunner(Minion):
	def minion(self):
		self.name = "Sylvanas Windrunner"
		self.classs = "normal"
		self.attack = 5
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Deathrattle: Take control of a random enemy minion."

class tauren_warrior(Minion):
	def minion(self):
		self.name = "Tauren Warrior"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Taunt. Enrage: +3 Attack"

class temple_enforcer(Minion):
	def minion(self):
		self.name = "Temple Enforcer"
		self.classs = "Priest"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion +3 Health."

class the_beast(Minion):
	def minion(self):
		self.name = "The Beast"
		self.classs = "normal"
		self.attack = 9
		self.health = 7
		self.cost = 6
		self.race = "beast"
		self.description = "Deathrattle: Summon a 3\/3 Finkle Einhorn for your opponent."

class the_black_knight(Minion):
	def minion(self):
		self.name = "The Black Knight"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Destroy an enemy minion with Taunt."

class thrallmar_farseer(Minion):
	def minion(self):
		self.name = "Thrallmar Farseer"
		self.classs = "normal"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Windfury"

class timber_wolf(Minion):
	def minion(self):
		self.name = "Timber Wolf"
		self.classs = "Hunter"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Your other Beasts have +1 Attack."

class tinkmaster_overspark(Minion):
	def minion(self):
		self.name = "Tinkmaster Overspark"
		self.classs = "normal"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Transform another random minion into a 5\/5 Devilsaur or a 1\/1 Squirrel."

class tirion_fordring(Minion):
	def minion(self):
		self.name = "Tirion Fordring"
		self.classs = "Paladin"
		self.attack = 6
		self.health = 6
		self.cost = 8
		self.race = "normal"
		self.description = "Divine Shield. Taunt. Deathrattle: Equip a 5\/3 Ashbringer."

class treant(Minion):
	def minion(self):
		self.name = "Treant"
		self.classs = "Druid"
		self.attack = 2
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = ""

class tundra_rhino(Minion):
	def minion(self):
		self.name = "Tundra Rhino"
		self.classs = "Hunter"
		self.attack = 2
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = "Your Beasts have Charge."

class twilight_drake(Minion):
	def minion(self):
		self.name = "Twilight Drake"
		self.classs = "normal"
		self.attack = 4
		self.health = 1
		self.cost = 4
		self.race = "dragon"
		self.description = "Battlecry: Gain +1 Health for each card in your hand."

class unbound_elemental(Minion):
	def minion(self):
		self.name = "Unbound Elemental"
		self.classs = "Shaman"
		self.attack = 2
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever you play a card with Overload, gain +1\/+1."

class venture_co_mercenary(Minion):
	def minion(self):
		self.name = "Venture Co. Mercenary"
		self.classs = "normal"
		self.attack = 7
		self.health = 6
		self.cost = 5
		self.race = "normal"
		self.description = "Your minions cost (3) more."

class violet_apprentice(Minion):
	def minion(self):
		self.name = "Violet Apprentice"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "normal"
		self.description = ""

class violet_teacher(Minion):
	def minion(self):
		self.name = "Violet Teacher"
		self.classs = "normal"
		self.attack = 3
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Whenever you cast a spell, summon a 1\/1 Violet Apprentice."

class void_terror(Minion):
	def minion(self):
		self.name = "Void Terror"
		self.classs = "Warlock"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "demon"
		self.description = "Battlecry: Destroy the minions on either side of this minion and gain their Attack and Health."

class voidwalker(Minion):
	def minion(self):
		self.name = "Voidwalker"
		self.classs = "Warlock"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.race = "demon"
		self.description = "Taunt"

class voodoo_doctor(Minion):
	def minion(self):
		self.name = "Voodoo Doctor"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Battlecry: Restore 2 Health."

class war_golem(Minion):
	def minion(self):
		self.name = "War Golem"
		self.classs = "normal"
		self.attack = 7
		self.health = 7
		self.cost = 7
		self.race = "normal"
		self.description = ""

class warsong_commander(Minion):
	def minion(self):
		self.name = "Warsong Commander"
		self.classs = "Warrior"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever you summon a minion with 3 or less Attack, give it Charge."

class water_elemental(Minion):
	def minion(self):
		self.name = "Water Elemental"
		self.classs = "Mage"
		self.attack = 3
		self.health = 6
		self.cost = 4
		self.race = "normal"
		self.description = "Freeze any character damaged by this minion."

class whelp(Minion):
	def minion(self):
		self.name = "Whelp"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "dragon"
		self.description = ""

class wild_pyromancer(Minion):
	def minion(self):
		self.name = "Wild Pyromancer"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "After you cast a spell, deal 1 damage to ALL minions."

class windfury_harpy(Minion):
	def minion(self):
		self.name = "Windfury Harpy"
		self.classs = "normal"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Windfury"

class windspeaker(Minion):
	def minion(self):
		self.name = "Windspeaker"
		self.classs = "Shaman"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion Windfury."

class wisp(Minion):
	def minion(self):
		self.name = "Wisp"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "normal"
		self.description = ""

class wolfrider(Minion):
	def minion(self):
		self.name = "Wolfrider"
		self.classs = "normal"
		self.attack = 3
		self.health = 1
		self.cost = 3
		self.race = "normal"
		self.description = "Charge"

class worgen_infiltrator(Minion):
	def minion(self):
		self.name = "Worgen Infiltrator"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Stealth"

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

class young_dragonhawk(Minion):
	def minion(self):
		self.name = "Young Dragonhawk"
		self.classs = "normal"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Windfury"

class young_priestess(Minion):
	def minion(self):
		self.name = "Young Priestess"
		self.classs = "normal"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "At the end of your turn, give another random friendly minion +1 Health."

class youthful_brewmaster(Minion):
	def minion(self):
		self.name = "Youthful Brewmaster"
		self.classs = "normal"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Return a friendly minion from the battlefield to your hand."

class ysera(Minion):
	def minion(self):
		self.name = "Ysera"
		self.classs = "normal"
		self.attack = 4
		self.health = 12
		self.cost = 9
		self.race = "dragon"
		self.description = "At the end of your turn, draw a Dream Card."

