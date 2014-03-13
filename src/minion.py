"""
minion.py
Contains definitions for Minion Class - Inherits Hearth

See init functions for what attributes are included

author: zach @ zhomans
"""	
#Local Modules
from general import Hearth
import effects as E


class Minion(Hearth):
	def init (self, health = 1, attack = 0, cost = 0, statuses = []):
		self.health = health
		self.attack = attack
		self.cost = cost
		self.statuses = statuses
		self.effects = effects
		self.owner = owner
		self.enemy = enemy
		self.minion()
		self.effects["battlecry"].apply(self.owner, self.enemy)

	def attack(self, target):
		target.receiveDamage(self.attack)
		self.receiveDamage(target.attack)

	def receiveDamage(self, damage):
		self.effects["receive_damage"].apply(self.owner, self.enemy)
		self.effects["receive_damage"].apply(self.owner, self.enemy) # TO-DO Add more
		self.health -= damage
		if self.health <= 0:
			self.die()

	def die(self):
		self.applyEffect(self.effects["deathrattle"].apply(self.owner, self.enemy))
		self.removeFromField()

	def removeFromField(self):
		self.owner.field.remove(self)

	def toString(self):
		return "\n".join([self.name, "Health:\t%d" % self.health, "Attack:\t%d" % self.attack, "Mana Cost:\t%d" % self.cost, "%s" % self.statuses])

class abomination(Minion):
	def minion(self):
		self.name = "Abomination"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt. Deathrattle: Deal 2 damage to ALL characters."

class abusive_sergeant(Minion):
	def minion(self):
		self.name = "Abusive Sergeant"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Battlecry: Give a minion +2 Attack this turn."

class acidic_swamp_ooze(Minion):
	def minion(self):
		self.name = "Acidic Swamp Ooze"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Destroy your opponent's weapon."

class acolyte_of_pain(Minion):
	def minion(self):
		self.name = "Acolyte of Pain"
		self.attack = 1
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever this minion takes damage, draw a card."

class alakir_the_windlord(Minion):
	def minion(self):
		self.name = "Al'Akir the Windlord"
		self.attack = 3
		self.health = 5
		self.cost = 8
		self.race = "normal"
		self.description = "Windfury, Charge, Divine Shield, Taunt"

class alarmobot(Minion):
	def minion(self):
		self.name = "Alarm-o-Bot"
		self.attack = 0
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "At the start of your turn, swap this minion with a random one in your hand."

class aldor_peacekeeper(Minion):
	def minion(self):
		self.name = "Aldor Peacekeeper"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Change an enemy minion's Attack to 1."

class alexstrasza(Minion):
	def minion(self):
		self.name = "Alexstrasza"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "dragon"
		self.description = "Battlecry: Set a hero's remaining Health to 15."

class amani_berserker(Minion):
	def minion(self):
		self.name = "Amani Berserker"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Enrage: +3 Attack"

class ancient_brewmaster(Minion):
	def minion(self):
		self.name = "Ancient Brewmaster"
		self.attack = 5
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Return a friendly minion from the battlefield to your hand."

class ancient_mage(Minion):
	def minion(self):
		self.name = "Ancient Mage"
		self.attack = 2
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give adjacent minions Spell Damage +1."

class ancient_watcher(Minion):
	def minion(self):
		self.name = "Ancient Watcher"
		self.attack = 4
		self.health = 5
		self.cost = 2
		self.race = "normal"
		self.description = "Can't Attack."

class ancient_of_lore(Minion):
	def minion(self):
		self.name = "Ancient of Lore"
		self.attack = 5
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "Choose One - Draw 2 cards; or Restore 5 Health."

class ancient_of_war(Minion):
	def minion(self):
		self.name = "Ancient of War"
		self.attack = 5
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "Choose One - +5 Attack; or +5 Health and Taunt."

class angry_chicken(Minion):
	def minion(self):
		self.name = "Angry Chicken"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Enrage: +5 Attack."

class arathi_weaponsmith(Minion):
	def minion(self):
		self.name = "Arathi Weaponsmith"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Equip a 2\/2 weapon."

class arcane_golem(Minion):
	def minion(self):
		self.name = "Arcane Golem"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Charge. Battlecry: Give your opponent a Mana Crystal."

class archmage(Minion):
	def minion(self):
		self.name = "Archmage"
		self.attack = 4
		self.health = 7
		self.cost = 6
		self.race = "normal"
		self.description = "Spell Damage +1"

class archmage_antonidas(Minion):
	def minion(self):
		self.name = "Archmage Antonidas"
		self.attack = 5
		self.health = 7
		self.cost = 7
		self.race = "normal"
		self.description = "Whenever you cast a spell, put a 'Fireball' spell into your hand."

class argent_commander(Minion):
	def minion(self):
		self.name = "Argent Commander"
		self.attack = 4
		self.health = 2
		self.cost = 6
		self.race = "normal"
		self.description = "Charge, Divine Shield"

class argent_protector(Minion):
	def minion(self):
		self.name = "Argent Protector"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion Divine Shield."

class argent_squire(Minion):
	def minion(self):
		self.name = "Argent Squire"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Divine Shield"

class armorsmith(Minion):
	def minion(self):
		self.name = "Armorsmith"
		self.attack = 1
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "Whenever a friendly minion takes damage, gain 1 Armor."

class auchenai_soulpriest(Minion):
	def minion(self):
		self.name = "Auchenai Soulpriest"
		self.attack = 3
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Your cards and powers that restore Health now deal damage instead."

class azure_drake(Minion):
	def minion(self):
		self.name = "Azure Drake"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "dragon"
		self.description = "Spell Damage +1. Battlecry: Draw a card."

class baron_geddon(Minion):
	def minion(self):
		self.name = "Baron Geddon"
		self.attack = 7
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "At the end of your turn, deal 2 damage to ALL other characters."

class big_game_hunter(Minion):
	def minion(self):
		self.name = "Big Game Hunter"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Destroy a minion with an Attack of 7 or more."

class blood_imp(Minion):
	def minion(self):
		self.name = "Blood Imp"
		self.attack = 0
		self.health = 1
		self.cost = 1
		self.race = "demon"
		self.description = "Stealth. At the end of your turn, give another random friendly minion +1 Health."

class blood_knight(Minion):
	def minion(self):
		self.name = "Blood Knight"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: All minions lose Divine Shield. Gain +3\/+3 for each Shield lost."

class bloodfen_raptor(Minion):
	def minion(self):
		self.name = "Bloodfen Raptor"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = ""

class bloodmage_thalnos(Minion):
	def minion(self):
		self.name = "Bloodmage Thalnos"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Spell Damage +1. Deathrattle: Draw a card."

class bloodsail_corsair(Minion):
	def minion(self):
		self.name = "Bloodsail Corsair"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "pirate"
		self.description = "Battlecry: Remove 1 Durability from your opponent's weapon."

class bloodsail_raider(Minion):
	def minion(self):
		self.name = "Bloodsail Raider"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "pirate"
		self.description = "Battlecry: Gain Attack equal to the Attack of your weapon."

class bluegill_warrior(Minion):
	def minion(self):
		self.name = "Bluegill Warrior"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "murloc"
		self.description = "Charge"

class booty_bay_bodyguard(Minion):
	def minion(self):
		self.name = "Booty Bay Bodyguard"
		self.attack = 5
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt"

class boulderfist_ogre(Minion):
	def minion(self):
		self.name = "Boulderfist Ogre"
		self.attack = 6
		self.health = 7
		self.cost = 6
		self.race = "normal"
		self.description = ""

class cabal_shadow_priest(Minion):
	def minion(self):
		self.name = "Cabal Shadow Priest"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Take control of an enemy minion that has 2 or less Attack."

class cairne_bloodhoof(Minion):
	def minion(self):
		self.name = "Cairne Bloodhoof"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Deathrattle: Summon a 4\/5 Baine Bloodhoof."

class captain_greenskin(Minion):
	def minion(self):
		self.name = "Captain Greenskin"
		self.attack = 5
		self.health = 4
		self.cost = 5
		self.race = "pirate"
		self.description = "Battlecry: Give your weapon +1\/+1."

class captains_parrot(Minion):
	def minion(self):
		self.name = "Captain's Parrot"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "beast"
		self.description = "Battlecry: Put a random Pirate from your deck into your hand."

class cenarius(Minion):
	def minion(self):
		self.name = "Cenarius"
		self.attack = 5
		self.health = 8
		self.cost = 9
		self.race = "normal"
		self.description = "Choose One - Give your other minions +2\/+2; or Summon two 2\/2 Treants with Taunt."

class chillwind_yeti(Minion):
	def minion(self):
		self.name = "Chillwind Yeti"
		self.attack = 4
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = ""

class coldlight_oracle(Minion):
	def minion(self):
		self.name = "Coldlight Oracle"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "murloc"
		self.description = "Battlecry: Each player draws 2 cards."

class coldlight_seer(Minion):
	def minion(self):
		self.name = "Coldlight Seer"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "murloc"
		self.description = "Battlecry: Give ALL other Murlocs +2 Health."

class core_hound(Minion):
	def minion(self):
		self.name = "Core Hound"
		self.attack = 9
		self.health = 5
		self.cost = 7
		self.race = "beast"
		self.description = ""

class crazed_alchemist(Minion):
	def minion(self):
		self.name = "Crazed Alchemist"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Swap the Attack and Health of a minion."

class cruel_taskmaster(Minion):
	def minion(self):
		self.name = "Cruel Taskmaster"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Deal 1 damage to a minion and give it +2 Attack."

class cult_master(Minion):
	def minion(self):
		self.name = "Cult Master"
		self.attack = 4
		self.health = 2
		self.cost = 4
		self.race = "normal"
		self.description = "Whenever one of your other minions dies, draw a card."

class dalaran_mage(Minion):
	def minion(self):
		self.name = "Dalaran Mage"
		self.attack = 1
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "Spell Damage +1"

class dark_iron_dwarf(Minion):
	def minion(self):
		self.name = "Dark Iron Dwarf"
		self.attack = 4
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a minion +2 Attack this turn."

class darkscale_healer(Minion):
	def minion(self):
		self.name = "Darkscale Healer"
		self.attack = 4
		self.health = 5
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Restore 2 Health to all friendly characters."

class deathwing(Minion):
	def minion(self):
		self.name = "Deathwing"
		self.attack = 12
		self.health = 12
		self.cost = 10
		self.race = "dragon"
		self.description = "Battlecry: Destroy all other minions and discard your hand."

class defender_of_argus(Minion):
	def minion(self):
		self.name = "Defender of Argus"
		self.attack = 2
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give adjacent minions +1\/+1 and Taunt."

class defias_ringleader(Minion):
	def minion(self):
		self.name = "Defias Ringleader"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Combo: Summon a 2\/1 Defias Bandit."

class demolisher(Minion):
	def minion(self):
		self.name = "Demolisher"
		self.attack = 1
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "At the start of your turn, deal 2 damage to a random enemy."

class dire_wolf_alpha(Minion):
	def minion(self):
		self.name = "Dire Wolf Alpha"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = "Adjacent minions have +1 Attack."

class doomguard(Minion):
	def minion(self):
		self.name = "Doomguard"
		self.attack = 5
		self.health = 7
		self.cost = 5
		self.race = "demon"
		self.description = "Charge. Battlecry: Discard two random cards."

class doomsayer(Minion):
	def minion(self):
		self.name = "Doomsayer"
		self.attack = 0
		self.health = 7
		self.cost = 2
		self.race = "normal"
		self.description = "At the start of your turn, destroy ALL minions."

class dragonling_mechanic(Minion):
	def minion(self):
		self.name = "Dragonling Mechanic"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Summon a 2\/1 Mechanical Dragonling."

class dread_corsair(Minion):
	def minion(self):
		self.name = "Dread Corsair"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "pirate"
		self.description = "Taunt. Costs (1) less per Attack of your weapon."

class dread_infernal(Minion):
	def minion(self):
		self.name = "Dread Infernal"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "demon"
		self.description = "Battlecry: Deal 1 damage to ALL other characters."

class druid_of_the_claw(Minion):
	def minion(self):
		self.name = "Druid of the Claw"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Choose One - Charge; or +2 Health and Taunt."

class dust_devil(Minion):
	def minion(self):
		self.name = "Dust Devil"
		self.attack = 3
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Windfury. Overload: (2)"

class earth_elemental(Minion):
	def minion(self):
		self.name = "Earth Elemental"
		self.attack = 7
		self.health = 8
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt. Overload: (3)"

class earthen_ring_farseer(Minion):
	def minion(self):
		self.name = "Earthen Ring Farseer"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Restore 3 Health."

class edwin_vancleef(Minion):
	def minion(self):
		self.name = "Edwin VanCleef"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Combo: Gain +2\/+2 for each card played earlier this turn."

class elite_tauren_chieftain(Minion):
	def minion(self):
		self.name = "Elite Tauren Chieftain"
		self.attack = 5
		self.health = 5
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Give both players the power to ROCK! (with a Power Chord card)"

class elven_archer(Minion):
	def minion(self):
		self.name = "Elven Archer"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Battlecry: Deal 1 damage."

class emperor_cobra(Minion):
	def minion(self):
		self.name = "Emperor Cobra"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "beast"
		self.description = "Destroy any minion damaged by this minion."

class ethereal_arcanist(Minion):
	def minion(self):
		self.name = "Ethereal Arcanist"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "If you control a Secret at the end of your turn, gain +2\/+2."

class faceless_manipulator(Minion):
	def minion(self):
		self.name = "Faceless Manipulator"
		self.attack = 3
		self.health = 3
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Choose a minion and become a copy of it."

class faerie_dragon(Minion):
	def minion(self):
		self.name = "Faerie Dragon"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "dragon"
		self.description = "Can't be targeted by Spells or Hero Powers."

class felguard(Minion):
	def minion(self):
		self.name = "Felguard"
		self.attack = 3
		self.health = 5
		self.cost = 3
		self.race = "demon"
		self.description = "Taunt. Battlecry: Destroy one of your Mana Crystals."

class fen_creeper(Minion):
	def minion(self):
		self.name = "Fen Creeper"
		self.attack = 3
		self.health = 6
		self.cost = 5
		self.race = "normal"
		self.description = "Taunt"

class fire_elemental(Minion):
	def minion(self):
		self.name = "Fire Elemental"
		self.attack = 6
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Deal 3 damage."

class flame_imp(Minion):
	def minion(self):
		self.name = "Flame Imp"
		self.attack = 3
		self.health = 2
		self.cost = 1
		self.race = "demon"
		self.description = "Battlecry: Deal 3 damage to your hero."

class flametongue_totem(Minion):
	def minion(self):
		self.name = "Flametongue Totem"
		self.attack = 0
		self.health = 3
		self.cost = 2
		self.race = "totem"
		self.description = "Adjacent minions have +2 Attack."

class flesheating_ghoul(Minion):
	def minion(self):
		self.name = "Flesheating Ghoul"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever a minion dies, gain +1 Attack."

class frost_elemental(Minion):
	def minion(self):
		self.name = "Frost Elemental"
		self.attack = 5
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Freeze a character."

class frostwolf_grunt(Minion):
	def minion(self):
		self.name = "Frostwolf Grunt"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Taunt"

class frostwolf_warlord(Minion):
	def minion(self):
		self.name = "Frostwolf Warlord"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Gain +1\/+1 for each other friendly minion on the battlefield."

class frothing_berserker(Minion):
	def minion(self):
		self.name = "Frothing Berserker"
		self.attack = 2
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever a minion takes damage, gain +1 Attack."

class gadgetzan_auctioneer(Minion):
	def minion(self):
		self.name = "Gadgetzan Auctioneer"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Whenever you cast a spell, draw a card."

class gelbin_mekkatorque(Minion):
	def minion(self):
		self.name = "Gelbin Mekkatorque"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Summon an AWESOME invention."

class gnomish_inventor(Minion):
	def minion(self):
		self.name = "Gnomish Inventor"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Draw a card."

class goldshire_footman(Minion):
	def minion(self):
		self.name = "Goldshire Footman"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = "Taunt"

class grimscale_oracle(Minion):
	def minion(self):
		self.name = "Grimscale Oracle"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "murloc"
		self.description = "ALL other Murlocs have +1 Attack."

class grommash_hellscream(Minion):
	def minion(self):
		self.name = "Grommash Hellscream"
		self.attack = 4
		self.health = 9
		self.cost = 8
		self.race = "normal"
		self.description = "Charge.  Enrage: +6 Attack"

class gruul(Minion):
	def minion(self):
		self.name = "Gruul"
		self.attack = 7
		self.health = 7
		self.cost = 8
		self.race = "normal"
		self.description = "At the end of each turn, gain +1\/+1 ."

class guardian_of_kings(Minion):
	def minion(self):
		self.name = "Guardian of Kings"
		self.attack = 5
		self.health = 6
		self.cost = 7
		self.race = "normal"
		self.description = "Battlecry: Restore 6 Health to your hero."

class gurubashi_berserker(Minion):
	def minion(self):
		self.name = "Gurubashi Berserker"
		self.attack = 2
		self.health = 7
		self.cost = 5
		self.race = "normal"
		self.description = "Whenever this minion takes damage, gain +3 Attack."

class harrison_jones(Minion):
	def minion(self):
		self.name = "Harrison Jones"
		self.attack = 5
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Destroy your opponent's weapon and draw cards equal to its Durability."

class harvest_golem(Minion):
	def minion(self):
		self.name = "Harvest Golem"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Deathrattle: Summon a 2\/1 Damaged Golem."

class hogger(Minion):
	def minion(self):
		self.name = "Hogger"
		self.attack = 4
		self.health = 4
		self.cost = 6
		self.race = "normal"
		self.description = "At the end of your turn, summon a 2\/2 Gnoll with Taunt."

class houndmaster(Minion):
	def minion(self):
		self.name = "Houndmaster"
		self.attack = 4
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a friendly Beast +2\/+2 and Taunt."

class hungry_crab(Minion):
	def minion(self):
		self.name = "Hungry Crab"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "beast"
		self.description = "Battlecry: Destroy a Murloc and gain +2\/+2."

class illidan_stormrage(Minion):
	def minion(self):
		self.name = "Illidan Stormrage"
		self.attack = 7
		self.health = 5
		self.cost = 6
		self.race = "demon"
		self.description = "Whenever you play a card, summon a 2\/1 Flame of Azzinoth."

class imp_master(Minion):
	def minion(self):
		self.name = "Imp Master"
		self.attack = 1
		self.health = 5
		self.cost = 3
		self.race = "normal"
		self.description = "At the end of your turn, deal 1 damage to this minion and summon a 1\/1 Imp."

class injured_blademaster(Minion):
	def minion(self):
		self.name = "Injured Blademaster"
		self.attack = 4
		self.health = 7
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Deal 4 damage to HIMSELF."

class ironbark_protector(Minion):
	def minion(self):
		self.name = "Ironbark Protector"
		self.attack = 8
		self.health = 8
		self.cost = 8
		self.race = "normal"
		self.description = "Taunt"

class ironbeak_owl(Minion):
	def minion(self):
		self.name = "Ironbeak Owl"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "beast"
		self.description = "Battlecry: Silence a minion."

class ironforge_rifleman(Minion):
	def minion(self):
		self.name = "Ironforge Rifleman"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Deal 1 damage."

class ironfur_grizzly(Minion):
	def minion(self):
		self.name = "Ironfur Grizzly"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "beast"
		self.description = "Taunt"

class jungle_panther(Minion):
	def minion(self):
		self.name = "Jungle Panther"
		self.attack = 4
		self.health = 2
		self.cost = 3
		self.race = "beast"
		self.description = "Stealth"

class keeper_of_the_grove(Minion):
	def minion(self):
		self.name = "Keeper of the Grove"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Choose One - Deal 2 damage; or Silence a minion."

class kidnapper(Minion):
	def minion(self):
		self.name = "Kidnapper"
		self.attack = 5
		self.health = 3
		self.cost = 6
		self.race = "normal"
		self.description = "Combo: Return a minion to its owner's hand."

class king_krush(Minion):
	def minion(self):
		self.name = "King Krush"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "beast"
		self.description = "Charge"

class king_mukla(Minion):
	def minion(self):
		self.name = "King Mukla"
		self.attack = 5
		self.health = 5
		self.cost = 3
		self.race = "beast"
		self.description = "Battlecry: Give your opponent 2 Bananas."

class kirin_tor_mage(Minion):
	def minion(self):
		self.name = "Kirin Tor Mage"
		self.attack = 4
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: The next Secret you play this turn costs (0)."

class knife_juggler(Minion):
	def minion(self):
		self.name = "Knife Juggler"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "After you summon a minion, deal 1 damage to a random enemy."

class kobold_geomancer(Minion):
	def minion(self):
		self.name = "Kobold Geomancer"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Spell Damage +1"

class korkron_elite(Minion):
	def minion(self):
		self.name = "Kor'kron Elite"
		self.attack = 4
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Charge"

class leeroy_jenkins(Minion):
	def minion(self):
		self.name = "Leeroy Jenkins"
		self.attack = 6
		self.health = 2
		self.cost = 4
		self.race = "normal"
		self.description = "Charge. Battlecry: Summon two 1\/1 Whelps for your opponent."

class leper_gnome(Minion):
	def minion(self):
		self.name = "Leper Gnome"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Deathrattle: Deal 2 damage to the enemy hero."

class lightspawn(Minion):
	def minion(self):
		self.name = "Lightspawn"
		self.attack = 0
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "This minion's Attack is always equal to its Health."

class lightwarden(Minion):
	def minion(self):
		self.name = "Lightwarden"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever a character is healed, gain +2 Attack."

class lightwell(Minion):
	def minion(self):
		self.name = "Lightwell"
		self.attack = 0
		self.health = 5
		self.cost = 2
		self.race = "normal"
		self.description = "At the start of your turn, restore 3 Health to a damaged friendly character."

class loot_hoarder(Minion):
	def minion(self):
		self.name = "Loot Hoarder"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Deathrattle: Draw a card."

class lord_jaraxxus(Minion):
	def minion(self):
		self.name = "Lord Jaraxxus"
		self.attack = 3
		self.health = 15
		self.cost = 9
		self.race = "demon"
		self.description = "Battlecry: Destroy your hero and replace him with Lord Jaraxxus."

class lord_of_the_arena(Minion):
	def minion(self):
		self.name = "Lord of the Arena"
		self.attack = 6
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Taunt"

class lorewalker_cho(Minion):
	def minion(self):
		self.name = "Lorewalker Cho"
		self.attack = 0
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "Whenever a player casts a spell, put a copy into the other player\u2019s hand."

class mad_bomber(Minion):
	def minion(self):
		self.name = "Mad Bomber"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Deal 3 damage randomly split between all other characters."

class magma_rager(Minion):
	def minion(self):
		self.name = "Magma Rager"
		self.attack = 5
		self.health = 1
		self.cost = 3
		self.race = "normal"
		self.description = ""

class malygos(Minion):
	def minion(self):
		self.name = "Malygos"
		self.attack = 4
		self.health = 12
		self.cost = 9
		self.race = "dragon"
		self.description = "Spell Damage +5"

class mana_addict(Minion):
	def minion(self):
		self.name = "Mana Addict"
		self.attack = 1
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Whenever you cast a spell, gain +2 Attack this turn."

class mana_tide_totem(Minion):
	def minion(self):
		self.name = "Mana Tide Totem"
		self.attack = 0
		self.health = 3
		self.cost = 3
		self.race = "totem"
		self.description = "At the end of your turn, draw a card."

class mana_wraith(Minion):
	def minion(self):
		self.name = "Mana Wraith"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "ALL minions cost (1) more."

class mana_wyrm(Minion):
	def minion(self):
		self.name = "Mana Wyrm"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever you cast a spell, gain +1 Attack."

class master_swordsmith(Minion):
	def minion(self):
		self.name = "Master Swordsmith"
		self.attack = 1
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "At the end of your turn, give another random friendly minion +1 Attack."

class master_of_disguise(Minion):
	def minion(self):
		self.name = "Master of Disguise"
		self.attack = 4
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion Stealth."

class millhouse_manastorm(Minion):
	def minion(self):
		self.name = "Millhouse Manastorm"
		self.attack = 4
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Enemy spells cost (0) next turn."

class mind_control_tech(Minion):
	def minion(self):
		self.name = "Mind Control Tech"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: If your opponent has 4 or more minions, take control of one at random."

class mogushan_warden(Minion):
	def minion(self):
		self.name = "Mogu'shan Warden"
		self.attack = 1
		self.health = 7
		self.cost = 4
		self.race = "normal"
		self.description = "Taunt"

class molten_giant(Minion):
	def minion(self):
		self.name = "Molten Giant"
		self.attack = 8
		self.health = 8
		self.cost = 20
		self.race = "normal"
		self.description = "Costs (1) less for each damage your hero has taken."

class mountain_giant(Minion):
	def minion(self):
		self.name = "Mountain Giant"
		self.attack = 8
		self.health = 8
		self.cost = 12
		self.race = "normal"
		self.description = "Costs (1) less for each other card in your hand."

class murloc_raider(Minion):
	def minion(self):
		self.name = "Murloc Raider"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "murloc"
		self.description = ""

class murloc_tidecaller(Minion):
	def minion(self):
		self.name = "Murloc Tidecaller"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "murloc"
		self.description = "Whenever a Murloc is summoned, gain +1 Attack."

class murloc_tidehunter(Minion):
	def minion(self):
		self.name = "Murloc Tidehunter"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "murloc"
		self.description = "Battlecry: Summon a 1\/1 Murloc Scout."

class murloc_warleader(Minion):
	def minion(self):
		self.name = "Murloc Warleader"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "murloc"
		self.description = "ALL other Murlocs have +2\/+1."

class nat_pagle(Minion):
	def minion(self):
		self.name = "Nat Pagle"
		self.attack = 0
		self.health = 4
		self.cost = 2
		self.race = "normal"
		self.description = "At the start of your turn, you have a 50% chance to draw an extra card."

class nightblade(Minion):
	def minion(self):
		self.name = "Nightblade"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Deal 3 damage to the enemy hero."

class northshire_cleric(Minion):
	def minion(self):
		self.name = "Northshire Cleric"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever a minion is healed, draw a card."

class novice_engineer(Minion):
	def minion(self):
		self.name = "Novice Engineer"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Draw a card."

class nozdormu(Minion):
	def minion(self):
		self.name = "Nozdormu"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "dragon"
		self.description = "Players only have 15 seconds to take their turns."

class oasis_snapjaw(Minion):
	def minion(self):
		self.name = "Oasis Snapjaw"
		self.attack = 2
		self.health = 7
		self.cost = 4
		self.race = "beast"
		self.description = ""

class ogre_magi(Minion):
	def minion(self):
		self.name = "Ogre Magi"
		self.attack = 4
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Spell Damage +1"

class old_murkeye(Minion):
	def minion(self):
		self.name = "Old Murk-Eye"
		self.attack = 2
		self.health = 4
		self.cost = 4
		self.race = "murloc"
		self.description = "Charge. Has +1 Attack for each other Murloc on the battlefield."

class onyxia(Minion):
	def minion(self):
		self.name = "Onyxia"
		self.attack = 8
		self.health = 8
		self.cost = 9
		self.race = "dragon"
		self.description = "Battlecry: Summon 1\/1 Whelps until your side of the battlefield is full."

class patient_assassin(Minion):
	def minion(self):
		self.name = "Patient Assassin"
		self.attack = 1
		self.health = 1
		self.cost = 2
		self.race = "normal"
		self.description = "Stealth. Destroy any minion damaged by this minion."

class pintsized_summoner(Minion):
	def minion(self):
		self.name = "Pint-Sized Summoner"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "The first minion you play each turn costs (1) less."

class pit_lord(Minion):
	def minion(self):
		self.name = "Pit Lord"
		self.attack = 5
		self.health = 6
		self.cost = 4
		self.race = "demon"
		self.description = "Battlecry: Deal 5 damage to your hero."

class priestess_of_elune(Minion):
	def minion(self):
		self.name = "Priestess of Elune"
		self.attack = 5
		self.health = 4
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Restore 4 Health to your hero."

class prophet_velen(Minion):
	def minion(self):
		self.name = "Prophet Velen"
		self.attack = 7
		self.health = 7
		self.cost = 7
		self.race = "normal"
		self.description = "Double the damage and healing of your spells and Hero Power."

class questing_adventurer(Minion):
	def minion(self):
		self.name = "Questing Adventurer"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever you play a card, gain +1\/+1."

class raging_worgen(Minion):
	def minion(self):
		self.name = "Raging Worgen"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Enrage: Windfury and +1 Attack"

class ragnaros_the_firelord(Minion):
	def minion(self):
		self.name = "Ragnaros the Firelord"
		self.attack = 8
		self.health = 8
		self.cost = 8
		self.race = "normal"
		self.description = "Can't Attack.  At the end of your turn, deal 8 damage to a random enemy."

class raid_leader(Minion):
	def minion(self):
		self.name = "Raid Leader"
		self.attack = 2
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Your other minions have +1 Attack."

class ravenholdt_assassin(Minion):
	def minion(self):
		self.name = "Ravenholdt Assassin"
		self.attack = 7
		self.health = 5
		self.cost = 7
		self.race = "normal"
		self.description = "Stealth"

class razorfen_hunter(Minion):
	def minion(self):
		self.name = "Razorfen Hunter"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Summon a 1\/1 Boar."

class reckless_rocketeer(Minion):
	def minion(self):
		self.name = "Reckless Rocketeer"
		self.attack = 5
		self.health = 2
		self.cost = 6
		self.race = "normal"
		self.description = "Charge"

class river_crocolisk(Minion):
	def minion(self):
		self.name = "River Crocolisk"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "beast"
		self.description = ""

class si7_agent(Minion):
	def minion(self):
		self.name = "SI:7 Agent"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Combo: Deal 2 damage."

class savannah_highmane(Minion):
	def minion(self):
		self.name = "Savannah Highmane"
		self.attack = 6
		self.health = 5
		self.cost = 6
		self.race = "beast"
		self.description = "Deathrattle: Summon two 2\/2 Hyenas."

class scarlet_crusader(Minion):
	def minion(self):
		self.name = "Scarlet Crusader"
		self.attack = 3
		self.health = 1
		self.cost = 3
		self.race = "normal"
		self.description = "Divine Shield"

class scavenging_hyena(Minion):
	def minion(self):
		self.name = "Scavenging Hyena"
		self.attack = 2
		self.health = 2
		self.cost = 2
		self.race = "beast"
		self.description = "Whenever a friendly Beast dies, gain +2\/+1."

class sea_giant(Minion):
	def minion(self):
		self.name = "Sea Giant"
		self.attack = 8
		self.health = 8
		self.cost = 10
		self.race = "normal"
		self.description = "Costs (1) less for each other minion on the battlefield."

class secretkeeper(Minion):
	def minion(self):
		self.name = "Secretkeeper"
		self.attack = 1
		self.health = 2
		self.cost = 1
		self.race = "normal"
		self.description = "Whenever a Secret is played, gain +1\/+1."

class senjin_shieldmasta(Minion):
	def minion(self):
		self.name = "Sen'jin Shieldmasta"
		self.attack = 3
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Taunt"

class shattered_sun_cleric(Minion):
	def minion(self):
		self.name = "Shattered Sun Cleric"
		self.attack = 3
		self.health = 2
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion +1\/+1."

class shieldbearer(Minion):
	def minion(self):
		self.name = "Shieldbearer"
		self.attack = 0
		self.health = 4
		self.cost = 1
		self.race = "normal"
		self.description = "Taunt"

class silver_hand_knight(Minion):
	def minion(self):
		self.name = "Silver Hand Knight"
		self.attack = 4
		self.health = 4
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Summon a 2\/2 Squire."

class silverback_patriarch(Minion):
	def minion(self):
		self.name = "Silverback Patriarch"
		self.attack = 1
		self.health = 4
		self.cost = 3
		self.race = "beast"
		self.description = "Taunt"

class silvermoon_guardian(Minion):
	def minion(self):
		self.name = "Silvermoon Guardian"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Divine Shield"

class sorcerers_apprentice(Minion):
	def minion(self):
		self.name = "Sorcerer's Apprentice"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Your spells cost (1) less."

class southsea_captain(Minion):
	def minion(self):
		self.name = "Southsea Captain"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "pirate"
		self.description = "Your other Pirates have +1\/+1."

class southsea_deckhand(Minion):
	def minion(self):
		self.name = "Southsea Deckhand"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "pirate"
		self.description = "Has Charge while you have a weapon equipped."

class spellbreaker(Minion):
	def minion(self):
		self.name = "Spellbreaker"
		self.attack = 4
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Silence a minion."

class spiteful_smith(Minion):
	def minion(self):
		self.name = "Spiteful Smith"
		self.attack = 4
		self.health = 6
		self.cost = 5
		self.race = "normal"
		self.description = "Enrage: Your weapon has +2 Attack."

class stampeding_kodo(Minion):
	def minion(self):
		self.name = "Stampeding Kodo"
		self.attack = 3
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = "Battlecry: Destroy a random enemy minion with 2 or less Attack."

class starving_buzzard(Minion):
	def minion(self):
		self.name = "Starving Buzzard"
		self.attack = 2
		self.health = 1
		self.cost = 2
		self.race = "beast"
		self.description = "Whenever you summon a Beast, draw a card."

class stonetusk_boar(Minion):
	def minion(self):
		self.name = "Stonetusk Boar"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Charge"

class stormpike_commando(Minion):
	def minion(self):
		self.name = "Stormpike Commando"
		self.attack = 4
		self.health = 2
		self.cost = 5
		self.race = "normal"
		self.description = "Battlecry: Deal 2 damage."

class stormwind_champion(Minion):
	def minion(self):
		self.name = "Stormwind Champion"
		self.attack = 6
		self.health = 6
		self.cost = 7
		self.race = "normal"
		self.description = "Your other minions have +1\/+1."

class stormwind_knight(Minion):
	def minion(self):
		self.name = "Stormwind Knight"
		self.attack = 2
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Charge"

class stranglethorn_tiger(Minion):
	def minion(self):
		self.name = "Stranglethorn Tiger"
		self.attack = 5
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = "Stealth"

class succubus(Minion):
	def minion(self):
		self.name = "Succubus"
		self.attack = 4
		self.health = 3
		self.cost = 2
		self.race = "demon"
		self.description = "Battlecry: Discard a random card."

class summoning_portal(Minion):
	def minion(self):
		self.name = "Summoning Portal"
		self.attack = 0
		self.health = 4
		self.cost = 4
		self.race = "normal"
		self.description = "Your minions cost (2) less, but not less than (1)."

class sunfury_protector(Minion):
	def minion(self):
		self.name = "Sunfury Protector"
		self.attack = 2
		self.health = 3
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Give adjacent minions Taunt."

class sunwalker(Minion):
	def minion(self):
		self.name = "Sunwalker"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Taunt. Divine Shield"

class sylvanas_windrunner(Minion):
	def minion(self):
		self.name = "Sylvanas Windrunner"
		self.attack = 5
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Deathrattle: Take control of a random enemy minion."

class tauren_warrior(Minion):
	def minion(self):
		self.name = "Tauren Warrior"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Taunt. Enrage: +3 Attack"

class temple_enforcer(Minion):
	def minion(self):
		self.name = "Temple Enforcer"
		self.attack = 6
		self.health = 6
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion +3 Health."

class the_beast(Minion):
	def minion(self):
		self.name = "The Beast"
		self.attack = 9
		self.health = 7
		self.cost = 6
		self.race = "beast"
		self.description = "Deathrattle: Summon a 3\/3 Finkle Einhorn for your opponent."

class the_black_knight(Minion):
	def minion(self):
		self.name = "The Black Knight"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Battlecry: Destroy an enemy minion with Taunt."

class thrallmar_farseer(Minion):
	def minion(self):
		self.name = "Thrallmar Farseer"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Windfury"

class timber_wolf(Minion):
	def minion(self):
		self.name = "Timber Wolf"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Your other Beasts have +1 Attack."

class tinkmaster_overspark(Minion):
	def minion(self):
		self.name = "Tinkmaster Overspark"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Battlecry: Transform another random minion into a 5\/5 Devilsaur or a 1\/1 Squirrel."

class tirion_fordring(Minion):
	def minion(self):
		self.name = "Tirion Fordring"
		self.attack = 6
		self.health = 6
		self.cost = 8
		self.race = "normal"
		self.description = "Divine Shield. Taunt. Deathrattle: Equip a 5\/3 Ashbringer."

class tundra_rhino(Minion):
	def minion(self):
		self.name = "Tundra Rhino"
		self.attack = 2
		self.health = 5
		self.cost = 5
		self.race = "beast"
		self.description = "Your Beasts have Charge."

class twilight_drake(Minion):
	def minion(self):
		self.name = "Twilight Drake"
		self.attack = 4
		self.health = 1
		self.cost = 4
		self.race = "dragon"
		self.description = "Battlecry: Gain +1 Health for each card in your hand."

class unbound_elemental(Minion):
	def minion(self):
		self.name = "Unbound Elemental"
		self.attack = 2
		self.health = 4
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever you play a card with Overload, gain +1\/+1."

class venture_co_mercenary(Minion):
	def minion(self):
		self.name = "Venture Co. Mercenary"
		self.attack = 7
		self.health = 6
		self.cost = 5
		self.race = "normal"
		self.description = "Your minions cost (3) more."

class violet_teacher(Minion):
	def minion(self):
		self.name = "Violet Teacher"
		self.attack = 3
		self.health = 5
		self.cost = 4
		self.race = "normal"
		self.description = "Whenever you cast a spell, summon a 1\/1 Violet Apprentice."

class void_terror(Minion):
	def minion(self):
		self.name = "Void Terror"
		self.attack = 3
		self.health = 3
		self.cost = 3
		self.race = "demon"
		self.description = "Battlecry: Destroy the minions on either side of this minion and gain their Attack and Health."

class voidwalker(Minion):
	def minion(self):
		self.name = "Voidwalker"
		self.attack = 1
		self.health = 3
		self.cost = 1
		self.race = "demon"
		self.description = "Taunt"

class voodoo_doctor(Minion):
	def minion(self):
		self.name = "Voodoo Doctor"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Battlecry: Restore 2 Health."

class war_golem(Minion):
	def minion(self):
		self.name = "War Golem"
		self.attack = 7
		self.health = 7
		self.cost = 7
		self.race = "normal"
		self.description = ""

class warsong_commander(Minion):
	def minion(self):
		self.name = "Warsong Commander"
		self.attack = 2
		self.health = 3
		self.cost = 3
		self.race = "normal"
		self.description = "Whenever you summon a minion with 3 or less Attack, give it Charge."

class water_elemental(Minion):
	def minion(self):
		self.name = "Water Elemental"
		self.attack = 3
		self.health = 6
		self.cost = 4
		self.race = "normal"
		self.description = "Freeze any character damaged by this minion."

class wild_pyromancer(Minion):
	def minion(self):
		self.name = "Wild Pyromancer"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "After you cast a spell, deal 1 damage to ALL minions."

class windfury_harpy(Minion):
	def minion(self):
		self.name = "Windfury Harpy"
		self.attack = 4
		self.health = 5
		self.cost = 6
		self.race = "normal"
		self.description = "Windfury"

class windspeaker(Minion):
	def minion(self):
		self.name = "Windspeaker"
		self.attack = 3
		self.health = 3
		self.cost = 4
		self.race = "normal"
		self.description = "Battlecry: Give a friendly minion Windfury."

class wisp(Minion):
	def minion(self):
		self.name = "Wisp"
		self.attack = 1
		self.health = 1
		self.cost = 0
		self.race = "normal"
		self.description = ""

class wolfrider(Minion):
	def minion(self):
		self.name = "Wolfrider"
		self.attack = 3
		self.health = 1
		self.cost = 3
		self.race = "normal"
		self.description = "Charge"

class worgen_infiltrator(Minion):
	def minion(self):
		self.name = "Worgen Infiltrator"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "Stealth"

class young_dragonhawk(Minion):
	def minion(self):
		self.name = "Young Dragonhawk"
		self.attack = 1
		self.health = 1
		self.cost = 1
		self.race = "beast"
		self.description = "Windfury"

class young_priestess(Minion):
	def minion(self):
		self.name = "Young Priestess"
		self.attack = 2
		self.health = 1
		self.cost = 1
		self.race = "normal"
		self.description = "At the end of your turn, give another random friendly minion +1 Health."

class youthful_brewmaster(Minion):
	def minion(self):
		self.name = "Youthful Brewmaster"
		self.attack = 3
		self.health = 2
		self.cost = 2
		self.race = "normal"
		self.description = "Battlecry: Return a friendly minion from the battlefield to your hand."

class ysera(Minion):
	def minion(self):
		self.name = "Ysera"
		self.attack = 4
		self.health = 12
		self.cost = 9
		self.race = "dragon"
		self.description = "At the end of your turn, draw a Dream Card."