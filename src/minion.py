"""
minion.py
Contains definitions for Minion Class - Inherits Hearth

Minion:
	Holds information on a minion effects, statuses, and triggers
Specific Minion:
	Holds name and power information

See init functions for what attributes are included

author: zach @ zhomans
"""	
#Local Modules
from general import Hearth

class Minion(Hearth):
	def init (self, health = 1, attack = 0, cost = 0, statuses = [], effects = [], owner = Hero()):
		self.health = health
		self.attack = attack
		self.cost = cost
		self.statuses = statuses
		self.effects = effects
		self.minion()

	def attack(self, target):
		target.receiveDamage(self.attack)
		self.receiveDamage(target.attack)

	def receiveDamage(self, damage):
		self.health -= damage
		if self.health <= 0:
			self.die()

	def die(self):
		self.applyEffect(self.effects.deathrattle)
		self.removeFromField()

	def applyEffect(self, effect):
		if effect != None:
			effect.apply()

	def removeFromField(self):
		self.owner.field.remove(self)

	def toString(self):
		return "\n".join([self.name, "Health:\t%d" % self.health, "Attack:\t%d" % self.attack, "Mana Cost:\t%d" % self.cost, "%s" % self.statuses])


class abomination(Minion):
	def minion(self):
		self.name = "Abomination"
		self.health = 4
		self.attack = 4
		self.cost = 5
		self.description = "Taunt. Deathrattle: Deal 2 damage to ALL characters."

class abusive_sergeant(Minion):
	def minion(self):
		self.name = "Abusive Sergeant"
		self.health = 1
		self.attack = 2
		self.cost = 1
		self.description = "Battlecry: Give a minion +2 Attack this turn."

class acidic_swamp_ooze(Minion):
	def minion(self):
		self.name = "Acidic Swamp Ooze"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = "Battlecry: Destroy your opponent's weapon."

class acolyte_of_pain(Minion):
	def minion(self):
		self.name = "Acolyte of Pain"
		self.health = 3
		self.attack = 1
		self.cost = 3
		self.description = "Whenever this minion takes damage, draw a card."

class al'akir_the_windlord(Minion):
	def minion(self):
		self.name = "Al'Akir the Windlord"
		self.health = 5
		self.attack = 3
		self.cost = 8
		self.description = "Windfury, Charge, Divine Shield, Taunt"

class alarm-o-bot(Minion):
	def minion(self):
		self.name = "Alarm-o-Bot"
		self.health = 3
		self.attack = 0
		self.cost = 3
		self.description = "At the start of your turn, swap this minion with a random one in your hand."

class aldor_peacekeeper(Minion):
	def minion(self):
		self.name = "Aldor Peacekeeper"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Battlecry: Change an enemy minion's Attack to 1."

class alexstrasza(Minion):
	def minion(self):
		self.name = "Alexstrasza"
		self.health = 8
		self.attack = 8
		self.cost = 9
		self.description = "Battlecry: Set a hero's remaining Health to 15."

class amani_berserker(Minion):
	def minion(self):
		self.name = "Amani Berserker"
		self.health = 3
		self.attack = 2
		self.cost = 2
		self.description = "Enrage: +3 Attack"

class ancient_brewmaster(Minion):
	def minion(self):
		self.name = "Ancient Brewmaster"
		self.health = 4
		self.attack = 5
		self.cost = 4
		self.description = "Battlecry: Return a friendly minion from the battlefield to your hand."

class ancient_mage(Minion):
	def minion(self):
		self.name = "Ancient Mage"
		self.health = 5
		self.attack = 2
		self.cost = 4
		self.description = "Battlecry: Give adjacent minions Spell Damage +1."

class ancient_watcher(Minion):
	def minion(self):
		self.name = "Ancient Watcher"
		self.health = 5
		self.attack = 4
		self.cost = 2
		self.description = "Can't Attack."

class ancient_of_lore(Minion):
	def minion(self):
		self.name = "Ancient of Lore"
		self.health = 5
		self.attack = 5
		self.cost = 7
		self.description = "Choose One - Draw 2 cards; or Restore 5 Health."

class ancient_of_war(Minion):
	def minion(self):
		self.name = "Ancient of War"
		self.health = 5
		self.attack = 5
		self.cost = 7
		self.description = "Choose One - +5 Attack; or +5 Health and Taunt."

class angry_chicken(Minion):
	def minion(self):
		self.name = "Angry Chicken"
		self.health = 1
		self.attack = 1
		self.cost = 1
		self.description = "Enrage: +5 Attack."

class arathi_weaponsmith(Minion):
	def minion(self):
		self.name = "Arathi Weaponsmith"
		self.health = 3
		self.attack = 3
		self.cost = 4
		self.description = "Battlecry: Equip a 2\/2 weapon."

class arcane_golem(Minion):
	def minion(self):
		self.name = "Arcane Golem"
		self.health = 2
		self.attack = 4
		self.cost = 3
		self.description = "Charge. Battlecry: Give your opponent a Mana Crystal."

class archmage(Minion):
	def minion(self):
		self.name = "Archmage"
		self.health = 7
		self.attack = 4
		self.cost = 6
		self.description = "Spell Damage +1"

class archmage_antonidas(Minion):
	def minion(self):
		self.name = "Archmage Antonidas"
		self.health = 7
		self.attack = 5
		self.cost = 7
		self.description = "Whenever you cast a spell, put a 'Fireball' spell into your hand."

class argent_commander(Minion):
	def minion(self):
		self.name = "Argent Commander"
		self.health = 2
		self.attack = 4
		self.cost = 6
		self.description = "Charge, Divine Shield"

class argent_protector(Minion):
	def minion(self):
		self.name = "Argent Protector"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Battlecry: Give a friendly minion Divine Shield."

class argent_squire(Minion):
	def minion(self):
		self.name = "Argent Squire"
		self.health = 1
		self.attack = 1
		self.cost = 1
		self.description = "Divine Shield"

class armorsmith(Minion):
	def minion(self):
		self.name = "Armorsmith"
		self.health = 4
		self.attack = 1
		self.cost = 2
		self.description = "Whenever a friendly minion takes damage, gain 1 Armor."

class auchenai_soulpriest(Minion):
	def minion(self):
		self.name = "Auchenai Soulpriest"
		self.health = 5
		self.attack = 3
		self.cost = 4
		self.description = "Your cards and powers that restore Health now deal damage instead."

class azure_drake(Minion):
	def minion(self):
		self.name = "Azure Drake"
		self.health = 4
		self.attack = 4
		self.cost = 5
		self.description = "Spell Damage +1. Battlecry: Draw a card."

class baron_geddon(Minion):
	def minion(self):
		self.name = "Baron Geddon"
		self.health = 5
		self.attack = 7
		self.cost = 7
		self.description = "At the end of your turn, deal 2 damage to ALL other characters."

class big_game_hunter(Minion):
	def minion(self):
		self.name = "Big Game Hunter"
		self.health = 2
		self.attack = 4
		self.cost = 3
		self.description = "Battlecry: Destroy a minion with an Attack of 7 or more."

class blood_imp(Minion):
	def minion(self):
		self.name = "Blood Imp"
		self.health = 1
		self.attack = 0
		self.cost = 1
		self.description = "Stealth. At the end of your turn, give another random friendly minion +1 Health."

class blood_knight(Minion):
	def minion(self):
		self.name = "Blood Knight"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Battlecry: All minions lose Divine Shield. Gain +3\/+3 for each Shield lost."

class bloodfen_raptor(Minion):
	def minion(self):
		self.name = "Bloodfen Raptor"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = ""

class bloodmage_thalnos(Minion):
	def minion(self):
		self.name = "Bloodmage Thalnos"
		self.health = 1
		self.attack = 1
		self.cost = 2
		self.description = "Spell Damage +1. Deathrattle: Draw a card."

class bloodsail_corsair(Minion):
	def minion(self):
		self.name = "Bloodsail Corsair"
		self.health = 2
		self.attack = 1
		self.cost = 1
		self.description = "Battlecry: Remove 1 Durability from your opponent's weapon."

class bloodsail_raider(Minion):
	def minion(self):
		self.name = "Bloodsail Raider"
		self.health = 3
		self.attack = 2
		self.cost = 2
		self.description = "Battlecry: Gain Attack equal to the Attack of your weapon."

class bluegill_warrior(Minion):
	def minion(self):
		self.name = "Bluegill Warrior"
		self.health = 1
		self.attack = 2
		self.cost = 2
		self.description = "Charge"

class booty_bay_bodyguard(Minion):
	def minion(self):
		self.name = "Booty Bay Bodyguard"
		self.health = 4
		self.attack = 5
		self.cost = 5
		self.description = "Taunt"

class boulderfist_ogre(Minion):
	def minion(self):
		self.name = "Boulderfist Ogre"
		self.health = 7
		self.attack = 6
		self.cost = 6
		self.description = ""

class cabal_shadow_priest(Minion):
	def minion(self):
		self.name = "Cabal Shadow Priest"
		self.health = 5
		self.attack = 4
		self.cost = 6
		self.description = "Battlecry: Take control of an enemy minion that has 2 or less Attack."

class cairne_bloodhoof(Minion):
	def minion(self):
		self.name = "Cairne Bloodhoof"
		self.health = 5
		self.attack = 4
		self.cost = 6
		self.description = "Deathrattle: Summon a 4\/5 Baine Bloodhoof."

class captain_greenskin(Minion):
	def minion(self):
		self.name = "Captain Greenskin"
		self.health = 4
		self.attack = 5
		self.cost = 5
		self.description = "Battlecry: Give your weapon +1\/+1."

class captain's_parrot(Minion):
	def minion(self):
		self.name = "Captain's Parrot"
		self.health = 1
		self.attack = 1
		self.cost = 2
		self.description = "Battlecry: Put a random Pirate from your deck into your hand."

class cenarius(Minion):
	def minion(self):
		self.name = "Cenarius"
		self.health = 8
		self.attack = 5
		self.cost = 9
		self.description = "Choose One - Give your other minions +2\/+2; or Summon two 2\/2 Treants with Taunt."

class chillwind_yeti(Minion):
	def minion(self):
		self.name = "Chillwind Yeti"
		self.health = 5
		self.attack = 4
		self.cost = 4
		self.description = ""

class coldlight_oracle(Minion):
	def minion(self):
		self.name = "Coldlight Oracle"
		self.health = 2
		self.attack = 2
		self.cost = 3
		self.description = "Battlecry: Each player draws 2 cards."

class coldlight_seer(Minion):
	def minion(self):
		self.name = "Coldlight Seer"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Battlecry: Give ALL other Murlocs +2 Health."

class core_hound(Minion):
	def minion(self):
		self.name = "Core Hound"
		self.health = 5
		self.attack = 9
		self.cost = 7
		self.description = ""

class crazed_alchemist(Minion):
	def minion(self):
		self.name = "Crazed Alchemist"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Battlecry: Swap the Attack and Health of a minion."

class cruel_taskmaster(Minion):
	def minion(self):
		self.name = "Cruel Taskmaster"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Battlecry: Deal 1 damage to a minion and give it +2 Attack."

class cult_master(Minion):
	def minion(self):
		self.name = "Cult Master"
		self.health = 2
		self.attack = 4
		self.cost = 4
		self.description = "Whenever one of your other minions dies, draw a card."

class dalaran_mage(Minion):
	def minion(self):
		self.name = "Dalaran Mage"
		self.health = 4
		self.attack = 1
		self.cost = 3
		self.description = "Spell Damage +1"

class dark_iron_dwarf(Minion):
	def minion(self):
		self.name = "Dark Iron Dwarf"
		self.health = 4
		self.attack = 4
		self.cost = 4
		self.description = "Battlecry: Give a minion +2 Attack this turn."

class darkscale_healer(Minion):
	def minion(self):
		self.name = "Darkscale Healer"
		self.health = 5
		self.attack = 4
		self.cost = 5
		self.description = "Battlecry: Restore 2 Health to all friendly characters."

class deathwing(Minion):
	def minion(self):
		self.name = "Deathwing"
		self.health = 12
		self.attack = 12
		self.cost = 10
		self.description = "Battlecry: Destroy all other minions and discard your hand."

class defender_of_argus(Minion):
	def minion(self):
		self.name = "Defender of Argus"
		self.health = 3
		self.attack = 2
		self.cost = 4
		self.description = "Battlecry: Give adjacent minions +1\/+1 and Taunt."

class defias_ringleader(Minion):
	def minion(self):
		self.name = "Defias Ringleader"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Combo: Summon a 2\/1 Defias Bandit."

class demolisher(Minion):
	def minion(self):
		self.name = "Demolisher"
		self.health = 4
		self.attack = 1
		self.cost = 3
		self.description = "At the start of your turn, deal 2 damage to a random enemy."

class dire_wolf_alpha(Minion):
	def minion(self):
		self.name = "Dire Wolf Alpha"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Adjacent minions have +1 Attack."

class doomguard(Minion):
	def minion(self):
		self.name = "Doomguard"
		self.health = 7
		self.attack = 5
		self.cost = 5
		self.description = "Charge. Battlecry: Discard two random cards."

class doomsayer(Minion):
	def minion(self):
		self.name = "Doomsayer"
		self.health = 7
		self.attack = 0
		self.cost = 2
		self.description = "At the start of your turn, destroy ALL minions."

class dragonling_mechanic(Minion):
	def minion(self):
		self.name = "Dragonling Mechanic"
		self.health = 4
		self.attack = 2
		self.cost = 4
		self.description = "Battlecry: Summon a 2\/1 Mechanical Dragonling."

class dread_corsair(Minion):
	def minion(self):
		self.name = "Dread Corsair"
		self.health = 3
		self.attack = 3
		self.cost = 4
		self.description = "Taunt. Costs (1) less per Attack of your weapon."

class dread_infernal(Minion):
	def minion(self):
		self.name = "Dread Infernal"
		self.health = 6
		self.attack = 6
		self.cost = 6
		self.description = "Battlecry: Deal 1 damage to ALL other characters."

class druid_of_the_claw(Minion):
	def minion(self):
		self.name = "Druid of the Claw"
		self.health = 4
		self.attack = 4
		self.cost = 5
		self.description = "Choose One - Charge; or +2 Health and Taunt."

class dust_devil(Minion):
	def minion(self):
		self.name = "Dust Devil"
		self.health = 1
		self.attack = 3
		self.cost = 1
		self.description = "Windfury. Overload: (2)"

class earth_elemental(Minion):
	def minion(self):
		self.name = "Earth Elemental"
		self.health = 8
		self.attack = 7
		self.cost = 5
		self.description = "Taunt. Overload: (3)"

class earthen_ring_farseer(Minion):
	def minion(self):
		self.name = "Earthen Ring Farseer"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Battlecry: Restore 3 Health."

class edwin_vancleef(Minion):
	def minion(self):
		self.name = "Edwin VanCleef"
		self.health = 2
		self.attack = 2
		self.cost = 3
		self.description = "Combo: Gain +2\/+2 for each card played earlier this turn."

class elite_tauren_chieftain(Minion):
	def minion(self):
		self.name = "Elite Tauren Chieftain"
		self.health = 5
		self.attack = 5
		self.cost = 5
		self.description = "Battlecry: Give both players the power to ROCK! (with a Power Chord card)"

class elven_archer(Minion):
	def minion(self):
		self.name = "Elven Archer"
		self.health = 1
		self.attack = 1
		self.cost = 1
		self.description = "Battlecry: Deal 1 damage."

class emperor_cobra(Minion):
	def minion(self):
		self.name = "Emperor Cobra"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Destroy any minion damaged by this minion."

class ethereal_arcanist(Minion):
	def minion(self):
		self.name = "Ethereal Arcanist"
		self.health = 3
		self.attack = 3
		self.cost = 4
		self.description = "If you control a Secret at the end of your turn, gain +2\/+2."

class faceless_manipulator(Minion):
	def minion(self):
		self.name = "Faceless Manipulator"
		self.health = 3
		self.attack = 3
		self.cost = 5
		self.description = "Battlecry: Choose a minion and become a copy of it."

class faerie_dragon(Minion):
	def minion(self):
		self.name = "Faerie Dragon"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = "Can't be targeted by Spells or Hero Powers."

class felguard(Minion):
	def minion(self):
		self.name = "Felguard"
		self.health = 5
		self.attack = 3
		self.cost = 3
		self.description = "Taunt. Battlecry: Destroy one of your Mana Crystals."

class fen_creeper(Minion):
	def minion(self):
		self.name = "Fen Creeper"
		self.health = 6
		self.attack = 3
		self.cost = 5
		self.description = "Taunt"

class fire_elemental(Minion):
	def minion(self):
		self.name = "Fire Elemental"
		self.health = 5
		self.attack = 6
		self.cost = 6
		self.description = "Battlecry: Deal 3 damage."

class flame_imp(Minion):
	def minion(self):
		self.name = "Flame Imp"
		self.health = 2
		self.attack = 3
		self.cost = 1
		self.description = "Battlecry: Deal 3 damage to your hero."

class flametongue_totem(Minion):
	def minion(self):
		self.name = "Flametongue Totem"
		self.health = 3
		self.attack = 0
		self.cost = 2
		self.description = "Adjacent minions have +2 Attack."

class flesheating_ghoul(Minion):
	def minion(self):
		self.name = "Flesheating Ghoul"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Whenever a minion dies, gain +1 Attack."

class frost_elemental(Minion):
	def minion(self):
		self.name = "Frost Elemental"
		self.health = 5
		self.attack = 5
		self.cost = 6
		self.description = "Battlecry: Freeze a character."

class frostwolf_grunt(Minion):
	def minion(self):
		self.name = "Frostwolf Grunt"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Taunt"

class frostwolf_warlord(Minion):
	def minion(self):
		self.name = "Frostwolf Warlord"
		self.health = 4
		self.attack = 4
		self.cost = 5
		self.description = "Battlecry: Gain +1\/+1 for each other friendly minion on the battlefield."

class frothing_berserker(Minion):
	def minion(self):
		self.name = "Frothing Berserker"
		self.health = 4
		self.attack = 2
		self.cost = 3
		self.description = "Whenever a minion takes damage, gain +1 Attack."

class gadgetzan_auctioneer(Minion):
	def minion(self):
		self.name = "Gadgetzan Auctioneer"
		self.health = 4
		self.attack = 4
		self.cost = 5
		self.description = "Whenever you cast a spell, draw a card."

class gelbin_mekkatorque(Minion):
	def minion(self):
		self.name = "Gelbin Mekkatorque"
		self.health = 6
		self.attack = 6
		self.cost = 6
		self.description = "Battlecry: Summon an AWESOME invention."

class gnomish_inventor(Minion):
	def minion(self):
		self.name = "Gnomish Inventor"
		self.health = 4
		self.attack = 2
		self.cost = 4
		self.description = "Battlecry: Draw a card."

class goldshire_footman(Minion):
	def minion(self):
		self.name = "Goldshire Footman"
		self.health = 2
		self.attack = 1
		self.cost = 1
		self.description = "Taunt"

class grimscale_oracle(Minion):
	def minion(self):
		self.name = "Grimscale Oracle"
		self.health = 1
		self.attack = 1
		self.cost = 1
		self.description = "ALL other Murlocs have +1 Attack."

class grommash_hellscream(Minion):
	def minion(self):
		self.name = "Grommash Hellscream"
		self.health = 9
		self.attack = 4
		self.cost = 8
		self.description = "Charge.  Enrage: +6 Attack"

class gruul(Minion):
	def minion(self):
		self.name = "Gruul"
		self.health = 7
		self.attack = 7
		self.cost = 8
		self.description = "At the end of each turn, gain +1\/+1 ."

class guardian_of_kings(Minion):
	def minion(self):
		self.name = "Guardian of Kings"
		self.health = 6
		self.attack = 5
		self.cost = 7
		self.description = "Battlecry: Restore 6 Health to your hero."

class gurubashi_berserker(Minion):
	def minion(self):
		self.name = "Gurubashi Berserker"
		self.health = 7
		self.attack = 2
		self.cost = 5
		self.description = "Whenever this minion takes damage, gain +3 Attack."

class harrison_jones(Minion):
	def minion(self):
		self.name = "Harrison Jones"
		self.health = 4
		self.attack = 5
		self.cost = 5
		self.description = "Battlecry: Destroy your opponent's weapon and draw cards equal to its Durability."

class harvest_golem(Minion):
	def minion(self):
		self.name = "Harvest Golem"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Deathrattle: Summon a 2\/1 Damaged Golem."

class hogger(Minion):
	def minion(self):
		self.name = "Hogger"
		self.health = 4
		self.attack = 4
		self.cost = 6
		self.description = "At the end of your turn, summon a 2\/2 Gnoll with Taunt."

class houndmaster(Minion):
	def minion(self):
		self.name = "Houndmaster"
		self.health = 3
		self.attack = 4
		self.cost = 4
		self.description = "Battlecry: Give a friendly Beast +2\/+2 and Taunt."

class hungry_crab(Minion):
	def minion(self):
		self.name = "Hungry Crab"
		self.health = 2
		self.attack = 1
		self.cost = 1
		self.description = "Battlecry: Destroy a Murloc and gain +2\/+2."

class illidan_stormrage(Minion):
	def minion(self):
		self.name = "Illidan Stormrage"
		self.health = 5
		self.attack = 7
		self.cost = 6
		self.description = "Whenever you play a card, summon a 2\/1 Flame of Azzinoth."

class imp_master(Minion):
	def minion(self):
		self.name = "Imp Master"
		self.health = 5
		self.attack = 1
		self.cost = 3
		self.description = "At the end of your turn, deal 1 damage to this minion and summon a 1\/1 Imp."

class injured_blademaster(Minion):
	def minion(self):
		self.name = "Injured Blademaster"
		self.health = 7
		self.attack = 4
		self.cost = 3
		self.description = "Battlecry: Deal 4 damage to HIMSELF."

class ironbark_protector(Minion):
	def minion(self):
		self.name = "Ironbark Protector"
		self.health = 8
		self.attack = 8
		self.cost = 8
		self.description = "Taunt"

class ironbeak_owl(Minion):
	def minion(self):
		self.name = "Ironbeak Owl"
		self.health = 1
		self.attack = 2
		self.cost = 2
		self.description = "Battlecry: Silence a minion."

class ironforge_rifleman(Minion):
	def minion(self):
		self.name = "Ironforge Rifleman"
		self.health = 2
		self.attack = 2
		self.cost = 3
		self.description = "Battlecry: Deal 1 damage."

class ironfur_grizzly(Minion):
	def minion(self):
		self.name = "Ironfur Grizzly"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Taunt"

class jungle_panther(Minion):
	def minion(self):
		self.name = "Jungle Panther"
		self.health = 2
		self.attack = 4
		self.cost = 3
		self.description = "Stealth"

class keeper_of_the_grove(Minion):
	def minion(self):
		self.name = "Keeper of the Grove"
		self.health = 4
		self.attack = 2
		self.cost = 4
		self.description = "Choose One - Deal 2 damage; or Silence a minion."

class kidnapper(Minion):
	def minion(self):
		self.name = "Kidnapper"
		self.health = 3
		self.attack = 5
		self.cost = 6
		self.description = "Combo: Return a minion to its owner's hand."

class king_krush(Minion):
	def minion(self):
		self.name = "King Krush"
		self.health = 8
		self.attack = 8
		self.cost = 9
		self.description = "Charge"

class king_mukla(Minion):
	def minion(self):
		self.name = "King Mukla"
		self.health = 5
		self.attack = 5
		self.cost = 3
		self.description = "Battlecry: Give your opponent 2 Bananas."

class kirin_tor_mage(Minion):
	def minion(self):
		self.name = "Kirin Tor Mage"
		self.health = 3
		self.attack = 4
		self.cost = 3
		self.description = "Battlecry: The next Secret you play this turn costs (0)."

class knife_juggler(Minion):
	def minion(self):
		self.name = "Knife Juggler"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = "After you summon a minion, deal 1 damage to a random enemy."

class kobold_geomancer(Minion):
	def minion(self):
		self.name = "Kobold Geomancer"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Spell Damage +1"

class kor'kron_elite(Minion):
	def minion(self):
		self.name = "Kor'kron Elite"
		self.health = 3
		self.attack = 4
		self.cost = 4
		self.description = "Charge"

class leeroy_jenkins(Minion):
	def minion(self):
		self.name = "Leeroy Jenkins"
		self.health = 2
		self.attack = 6
		self.cost = 4
		self.description = "Charge. Battlecry: Summon two 1\/1 Whelps for your opponent."

class leper_gnome(Minion):
	def minion(self):
		self.name = "Leper Gnome"
		self.health = 1
		self.attack = 2
		self.cost = 1
		self.description = "Deathrattle: Deal 2 damage to the enemy hero."

class lightspawn(Minion):
	def minion(self):
		self.name = "Lightspawn"
		self.health = 5
		self.attack = 0
		self.cost = 4
		self.description = "This minion's Attack is always equal to its Health."

class lightwarden(Minion):
	def minion(self):
		self.name = "Lightwarden"
		self.health = 2
		self.attack = 1
		self.cost = 1
		self.description = "Whenever a character is healed, gain +2 Attack."

class lightwell(Minion):
	def minion(self):
		self.name = "Lightwell"
		self.health = 5
		self.attack = 0
		self.cost = 2
		self.description = "At the start of your turn, restore 3 Health to a damaged friendly character."

class loot_hoarder(Minion):
	def minion(self):
		self.name = "Loot Hoarder"
		self.health = 1
		self.attack = 2
		self.cost = 2
		self.description = "Deathrattle: Draw a card."

class lord_jaraxxus(Minion):
	def minion(self):
		self.name = "Lord Jaraxxus"
		self.health = 15
		self.attack = 3
		self.cost = 9
		self.description = "Battlecry: Destroy your hero and replace him with Lord Jaraxxus."

class lord_of_the_arena(Minion):
	def minion(self):
		self.name = "Lord of the Arena"
		self.health = 5
		self.attack = 6
		self.cost = 6
		self.description = "Taunt"

class lorewalker_cho(Minion):
	def minion(self):
		self.name = "Lorewalker Cho"
		self.health = 4
		self.attack = 0
		self.cost = 2
		self.description = "Whenever a player casts a spell, put a copy into the other player\u2019s hand."

class mad_bomber(Minion):
	def minion(self):
		self.name = "Mad Bomber"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = "Battlecry: Deal 3 damage randomly split between all other characters."

class magma_rager(Minion):
	def minion(self):
		self.name = "Magma Rager"
		self.health = 1
		self.attack = 5
		self.cost = 3
		self.description = ""

class malygos(Minion):
	def minion(self):
		self.name = "Malygos"
		self.health = 12
		self.attack = 4
		self.cost = 9
		self.description = "Spell Damage +5"

class mana_addict(Minion):
	def minion(self):
		self.name = "Mana Addict"
		self.health = 3
		self.attack = 1
		self.cost = 2
		self.description = "Whenever you cast a spell, gain +2 Attack this turn."

class mana_tide_totem(Minion):
	def minion(self):
		self.name = "Mana Tide Totem"
		self.health = 3
		self.attack = 0
		self.cost = 3
		self.description = "At the end of your turn, draw a card."

class mana_wraith(Minion):
	def minion(self):
		self.name = "Mana Wraith"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "ALL minions cost (1) more."

class mana_wyrm(Minion):
	def minion(self):
		self.name = "Mana Wyrm"
		self.health = 3
		self.attack = 1
		self.cost = 1
		self.description = "Whenever you cast a spell, gain +1 Attack."

class master_swordsmith(Minion):
	def minion(self):
		self.name = "Master Swordsmith"
		self.health = 3
		self.attack = 1
		self.cost = 2
		self.description = "At the end of your turn, give another random friendly minion +1 Attack."

class master_of_disguise(Minion):
	def minion(self):
		self.name = "Master of Disguise"
		self.health = 4
		self.attack = 4
		self.cost = 4
		self.description = "Battlecry: Give a friendly minion Stealth."

class millhouse_manastorm(Minion):
	def minion(self):
		self.name = "Millhouse Manastorm"
		self.health = 4
		self.attack = 4
		self.cost = 2
		self.description = "Battlecry: Enemy spells cost (0) next turn."

class mind_control_tech(Minion):
	def minion(self):
		self.name = "Mind Control Tech"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Battlecry: If your opponent has 4 or more minions, take control of one at random."

class mogu'shan_warden(Minion):
	def minion(self):
		self.name = "Mogu'shan Warden"
		self.health = 7
		self.attack = 1
		self.cost = 4
		self.description = "Taunt"

class molten_giant(Minion):
	def minion(self):
		self.name = "Molten Giant"
		self.health = 8
		self.attack = 8
		self.cost = 20
		self.description = "Costs (1) less for each damage your hero has taken."

class mountain_giant(Minion):
	def minion(self):
		self.name = "Mountain Giant"
		self.health = 8
		self.attack = 8
		self.cost = 12
		self.description = "Costs (1) less for each other card in your hand."

class murloc_raider(Minion):
	def minion(self):
		self.name = "Murloc Raider"
		self.health = 1
		self.attack = 2
		self.cost = 1
		self.description = ""

class murloc_tidecaller(Minion):
	def minion(self):
		self.name = "Murloc Tidecaller"
		self.health = 2
		self.attack = 1
		self.cost = 1
		self.description = "Whenever a Murloc is summoned, gain +1 Attack."

class murloc_tidehunter(Minion):
	def minion(self):
		self.name = "Murloc Tidehunter"
		self.health = 1
		self.attack = 2
		self.cost = 2
		self.description = "Battlecry: Summon a 1\/1 Murloc Scout."

class murloc_warleader(Minion):
	def minion(self):
		self.name = "Murloc Warleader"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "ALL other Murlocs have +2\/+1."

class nat_pagle(Minion):
	def minion(self):
		self.name = "Nat Pagle"
		self.health = 4
		self.attack = 0
		self.cost = 2
		self.description = "At the start of your turn, you have a 50% chance to draw an extra card."

class nightblade(Minion):
	def minion(self):
		self.name = "Nightblade"
		self.health = 4
		self.attack = 4
		self.cost = 5
		self.description = "Battlecry: Deal 3 damage to the enemy hero."

class northshire_cleric(Minion):
	def minion(self):
		self.name = "Northshire Cleric"
		self.health = 3
		self.attack = 1
		self.cost = 1
		self.description = "Whenever a minion is healed, draw a card."

class novice_engineer(Minion):
	def minion(self):
		self.name = "Novice Engineer"
		self.health = 1
		self.attack = 1
		self.cost = 2
		self.description = "Battlecry: Draw a card."

class nozdormu(Minion):
	def minion(self):
		self.name = "Nozdormu"
		self.health = 8
		self.attack = 8
		self.cost = 9
		self.description = "Players only have 15 seconds to take their turns."

class oasis_snapjaw(Minion):
	def minion(self):
		self.name = "Oasis Snapjaw"
		self.health = 7
		self.attack = 2
		self.cost = 4
		self.description = ""

class ogre_magi(Minion):
	def minion(self):
		self.name = "Ogre Magi"
		self.health = 4
		self.attack = 4
		self.cost = 4
		self.description = "Spell Damage +1"

class old_murk-eye(Minion):
	def minion(self):
		self.name = "Old Murk-Eye"
		self.health = 4
		self.attack = 2
		self.cost = 4
		self.description = "Charge. Has +1 Attack for each other Murloc on the battlefield."

class onyxia(Minion):
	def minion(self):
		self.name = "Onyxia"
		self.health = 8
		self.attack = 8
		self.cost = 9
		self.description = "Battlecry: Summon 1\/1 Whelps until your side of the battlefield is full."

class patient_assassin(Minion):
	def minion(self):
		self.name = "Patient Assassin"
		self.health = 1
		self.attack = 1
		self.cost = 2
		self.description = "Stealth. Destroy any minion damaged by this minion."

class pint-sized_summoner(Minion):
	def minion(self):
		self.name = "Pint-Sized Summoner"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "The first minion you play each turn costs (1) less."

class pit_lord(Minion):
	def minion(self):
		self.name = "Pit Lord"
		self.health = 6
		self.attack = 5
		self.cost = 4
		self.description = "Battlecry: Deal 5 damage to your hero."

class priestess_of_elune(Minion):
	def minion(self):
		self.name = "Priestess of Elune"
		self.health = 4
		self.attack = 5
		self.cost = 6
		self.description = "Battlecry: Restore 4 Health to your hero."

class prophet_velen(Minion):
	def minion(self):
		self.name = "Prophet Velen"
		self.health = 7
		self.attack = 7
		self.cost = 7
		self.description = "Double the damage and healing of your spells and Hero Power."

class questing_adventurer(Minion):
	def minion(self):
		self.name = "Questing Adventurer"
		self.health = 2
		self.attack = 2
		self.cost = 3
		self.description = "Whenever you play a card, gain +1\/+1."

class raging_worgen(Minion):
	def minion(self):
		self.name = "Raging Worgen"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Enrage: Windfury and +1 Attack"

class ragnaros_the_firelord(Minion):
	def minion(self):
		self.name = "Ragnaros the Firelord"
		self.health = 8
		self.attack = 8
		self.cost = 8
		self.description = "Can't Attack.  At the end of your turn, deal 8 damage to a random enemy."

class raid_leader(Minion):
	def minion(self):
		self.name = "Raid Leader"
		self.health = 2
		self.attack = 2
		self.cost = 3
		self.description = "Your other minions have +1 Attack."

class ravenholdt_assassin(Minion):
	def minion(self):
		self.name = "Ravenholdt Assassin"
		self.health = 5
		self.attack = 7
		self.cost = 7
		self.description = "Stealth"

class razorfen_hunter(Minion):
	def minion(self):
		self.name = "Razorfen Hunter"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Battlecry: Summon a 1\/1 Boar."

class reckless_rocketeer(Minion):
	def minion(self):
		self.name = "Reckless Rocketeer"
		self.health = 2
		self.attack = 5
		self.cost = 6
		self.description = "Charge"

class river_crocolisk(Minion):
	def minion(self):
		self.name = "River Crocolisk"
		self.health = 3
		self.attack = 2
		self.cost = 2
		self.description = ""

class si:7_agent(Minion):
	def minion(self):
		self.name = "SI:7 Agent"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Combo: Deal 2 damage."

class savannah_highmane(Minion):
	def minion(self):
		self.name = "Savannah Highmane"
		self.health = 5
		self.attack = 6
		self.cost = 6
		self.description = "Deathrattle: Summon two 2\/2 Hyenas."

class scarlet_crusader(Minion):
	def minion(self):
		self.name = "Scarlet Crusader"
		self.health = 1
		self.attack = 3
		self.cost = 3
		self.description = "Divine Shield"

class scavenging_hyena(Minion):
	def minion(self):
		self.name = "Scavenging Hyena"
		self.health = 2
		self.attack = 2
		self.cost = 2
		self.description = "Whenever a friendly Beast dies, gain +2\/+1."

class sea_giant(Minion):
	def minion(self):
		self.name = "Sea Giant"
		self.health = 8
		self.attack = 8
		self.cost = 10
		self.description = "Costs (1) less for each other minion on the battlefield."

class secretkeeper(Minion):
	def minion(self):
		self.name = "Secretkeeper"
		self.health = 2
		self.attack = 1
		self.cost = 1
		self.description = "Whenever a Secret is played, gain +1\/+1."

class sen'jin_shieldmasta(Minion):
	def minion(self):
		self.name = "Sen'jin Shieldmasta"
		self.health = 5
		self.attack = 3
		self.cost = 4
		self.description = "Taunt"

class shattered_sun_cleric(Minion):
	def minion(self):
		self.name = "Shattered Sun Cleric"
		self.health = 2
		self.attack = 3
		self.cost = 3
		self.description = "Battlecry: Give a friendly minion +1\/+1."

class shieldbearer(Minion):
	def minion(self):
		self.name = "Shieldbearer"
		self.health = 4
		self.attack = 0
		self.cost = 1
		self.description = "Taunt"

class silver_hand_knight(Minion):
	def minion(self):
		self.name = "Silver Hand Knight"
		self.health = 4
		self.attack = 4
		self.cost = 5
		self.description = "Battlecry: Summon a 2\/2 Squire."

class silverback_patriarch(Minion):
	def minion(self):
		self.name = "Silverback Patriarch"
		self.health = 4
		self.attack = 1
		self.cost = 3
		self.description = "Taunt"

class silvermoon_guardian(Minion):
	def minion(self):
		self.name = "Silvermoon Guardian"
		self.health = 3
		self.attack = 3
		self.cost = 4
		self.description = "Divine Shield"

class sorcerer's_apprentice(Minion):
	def minion(self):
		self.name = "Sorcerer's Apprentice"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = "Your spells cost (1) less."

class southsea_captain(Minion):
	def minion(self):
		self.name = "Southsea Captain"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Your other Pirates have +1\/+1."

class southsea_deckhand(Minion):
	def minion(self):
		self.name = "Southsea Deckhand"
		self.health = 1
		self.attack = 2
		self.cost = 1
		self.description = "Has Charge while you have a weapon equipped."

class spellbreaker(Minion):
	def minion(self):
		self.name = "Spellbreaker"
		self.health = 3
		self.attack = 4
		self.cost = 4
		self.description = "Battlecry: Silence a minion."

class spiteful_smith(Minion):
	def minion(self):
		self.name = "Spiteful Smith"
		self.health = 6
		self.attack = 4
		self.cost = 5
		self.description = "Enrage: Your weapon has +2 Attack."

class stampeding_kodo(Minion):
	def minion(self):
		self.name = "Stampeding Kodo"
		self.health = 5
		self.attack = 3
		self.cost = 5
		self.description = "Battlecry: Destroy a random enemy minion with 2 or less Attack."

class starving_buzzard(Minion):
	def minion(self):
		self.name = "Starving Buzzard"
		self.health = 1
		self.attack = 2
		self.cost = 2
		self.description = "Whenever you summon a Beast, draw a card."

class stonetusk_boar(Minion):
	def minion(self):
		self.name = "Stonetusk Boar"
		self.health = 1
		self.attack = 1
		self.cost = 1
		self.description = "Charge"

class stormpike_commando(Minion):
	def minion(self):
		self.name = "Stormpike Commando"
		self.health = 2
		self.attack = 4
		self.cost = 5
		self.description = "Battlecry: Deal 2 damage."

class stormwind_champion(Minion):
	def minion(self):
		self.name = "Stormwind Champion"
		self.health = 6
		self.attack = 6
		self.cost = 7
		self.description = "Your other minions have +1\/+1."

class stormwind_knight(Minion):
	def minion(self):
		self.name = "Stormwind Knight"
		self.health = 5
		self.attack = 2
		self.cost = 4
		self.description = "Charge"

class stranglethorn_tiger(Minion):
	def minion(self):
		self.name = "Stranglethorn Tiger"
		self.health = 5
		self.attack = 5
		self.cost = 5
		self.description = "Stealth"

class succubus(Minion):
	def minion(self):
		self.name = "Succubus"
		self.health = 3
		self.attack = 4
		self.cost = 2
		self.description = "Battlecry: Discard a random card."

class summoning_portal(Minion):
	def minion(self):
		self.name = "Summoning Portal"
		self.health = 4
		self.attack = 0
		self.cost = 4
		self.description = "Your minions cost (2) less, but not less than (1)."

class sunfury_protector(Minion):
	def minion(self):
		self.name = "Sunfury Protector"
		self.health = 3
		self.attack = 2
		self.cost = 2
		self.description = "Battlecry: Give adjacent minions Taunt."

class sunwalker(Minion):
	def minion(self):
		self.name = "Sunwalker"
		self.health = 5
		self.attack = 4
		self.cost = 6
		self.description = "Taunt. Divine Shield"

class sylvanas_windrunner(Minion):
	def minion(self):
		self.name = "Sylvanas Windrunner"
		self.health = 5
		self.attack = 5
		self.cost = 6
		self.description = "Deathrattle: Take control of a random enemy minion."

class tauren_warrior(Minion):
	def minion(self):
		self.name = "Tauren Warrior"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Taunt. Enrage: +3 Attack"

class temple_enforcer(Minion):
	def minion(self):
		self.name = "Temple Enforcer"
		self.health = 6
		self.attack = 6
		self.cost = 6
		self.description = "Battlecry: Give a friendly minion +3 Health."

class the_beast(Minion):
	def minion(self):
		self.name = "The Beast"
		self.health = 7
		self.attack = 9
		self.cost = 6
		self.description = "Deathrattle: Summon a 3\/3 Finkle Einhorn for your opponent."

class the_black_knight(Minion):
	def minion(self):
		self.name = "The Black Knight"
		self.health = 5
		self.attack = 4
		self.cost = 6
		self.description = "Battlecry: Destroy an enemy minion with Taunt."

class thrallmar_farseer(Minion):
	def minion(self):
		self.name = "Thrallmar Farseer"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Windfury"

class timber_wolf(Minion):
	def minion(self):
		self.name = "Timber Wolf"
		self.health = 1
		self.attack = 1
		self.cost = 1
		self.description = "Your other Beasts have +1 Attack."

class tinkmaster_overspark(Minion):
	def minion(self):
		self.name = "Tinkmaster Overspark"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Battlecry: Transform another random minion into a 5\/5 Devilsaur or a 1\/1 Squirrel."

class tirion_fordring(Minion):
	def minion(self):
		self.name = "Tirion Fordring"
		self.health = 6
		self.attack = 6
		self.cost = 8
		self.description = "Divine Shield. Taunt. Deathrattle: Equip a 5\/3 Ashbringer."

class tundra_rhino(Minion):
	def minion(self):
		self.name = "Tundra Rhino"
		self.health = 5
		self.attack = 2
		self.cost = 5
		self.description = "Your Beasts have Charge."

class twilight_drake(Minion):
	def minion(self):
		self.name = "Twilight Drake"
		self.health = 1
		self.attack = 4
		self.cost = 4
		self.description = "Battlecry: Gain +1 Health for each card in your hand."

class unbound_elemental(Minion):
	def minion(self):
		self.name = "Unbound Elemental"
		self.health = 4
		self.attack = 2
		self.cost = 3
		self.description = "Whenever you play a card with Overload, gain +1\/+1."

class venture_co._mercenary(Minion):
	def minion(self):
		self.name = "Venture Co. Mercenary"
		self.health = 6
		self.attack = 7
		self.cost = 5
		self.description = "Your minions cost (3) more."

class violet_teacher(Minion):
	def minion(self):
		self.name = "Violet Teacher"
		self.health = 5
		self.attack = 3
		self.cost = 4
		self.description = "Whenever you cast a spell, summon a 1\/1 Violet Apprentice."

class void_terror(Minion):
	def minion(self):
		self.name = "Void Terror"
		self.health = 3
		self.attack = 3
		self.cost = 3
		self.description = "Battlecry: Destroy the minions on either side of this minion and gain their Attack and Health."

class voidwalker(Minion):
	def minion(self):
		self.name = "Voidwalker"
		self.health = 3
		self.attack = 1
		self.cost = 1
		self.description = "Taunt"

class voodoo_doctor(Minion):
	def minion(self):
		self.name = "Voodoo Doctor"
		self.health = 1
		self.attack = 2
		self.cost = 1
		self.description = "Battlecry: Restore 2 Health."

class war_golem(Minion):
	def minion(self):
		self.name = "War Golem"
		self.health = 7
		self.attack = 7
		self.cost = 7
		self.description = ""

class warsong_commander(Minion):
	def minion(self):
		self.name = "Warsong Commander"
		self.health = 3
		self.attack = 2
		self.cost = 3
		self.description = "Whenever you summon a minion with 3 or less Attack, give it Charge."

class water_elemental(Minion):
	def minion(self):
		self.name = "Water Elemental"
		self.health = 6
		self.attack = 3
		self.cost = 4
		self.description = "Freeze any character damaged by this minion."

class wild_pyromancer(Minion):
	def minion(self):
		self.name = "Wild Pyromancer"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = "After you cast a spell, deal 1 damage to ALL minions."

class windfury_harpy(Minion):
	def minion(self):
		self.name = "Windfury Harpy"
		self.health = 5
		self.attack = 4
		self.cost = 6
		self.description = "Windfury"

class windspeaker(Minion):
	def minion(self):
		self.name = "Windspeaker"
		self.health = 3
		self.attack = 3
		self.cost = 4
		self.description = "Battlecry: Give a friendly minion Windfury."

class wisp(Minion):
	def minion(self):
		self.name = "Wisp"
		self.health = 1
		self.attack = 1
		self.cost = 0
		self.description = ""

class wolfrider(Minion):
	def minion(self):
		self.name = "Wolfrider"
		self.health = 1
		self.attack = 3
		self.cost = 3
		self.description = "Charge"

class worgen_infiltrator(Minion):
	def minion(self):
		self.name = "Worgen Infiltrator"
		self.health = 1
		self.attack = 2
		self.cost = 1
		self.description = "Stealth"

class young_dragonhawk(Minion):
	def minion(self):
		self.name = "Young Dragonhawk"
		self.health = 1
		self.attack = 1
		self.cost = 1
		self.description = "Windfury"

class young_priestess(Minion):
	def minion(self):
		self.name = "Young Priestess"
		self.health = 1
		self.attack = 2
		self.cost = 1
		self.description = "At the end of your turn, give another random friendly minion +1 Health."

class youthful_brewmaster(Minion):
	def minion(self):
		self.name = "Youthful Brewmaster"
		self.health = 2
		self.attack = 3
		self.cost = 2
		self.description = "Battlecry: Return a friendly minion from the battlefield to your hand."

class ysera(Minion):
	def minion(self):
		self.name = "Ysera"
		self.health = 12
		self.attack = 4
		self.cost = 9
		self.description = "At the end of your turn, draw a Dream Card."


if __name__ == "__main__":
	minion1 = silver_hand_recruit()
	print minion1