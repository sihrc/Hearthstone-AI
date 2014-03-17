"""
spell.py
Contains definitions for Spell Class - Inherits Hearth

See init functions for what attributes are included

author: chris @ sihrc
"""	

from hearth import *
from wrappers import *
import minion as M
import effect as E


class Spell(Hearth):
	def __init__(self, owner, origin = None):
		self.health = 0
		self.owner = owner
		self.enemy = owner.enemy
		self.origin = origin
		self.spell()
	
	def toString(self):
		return "%s\n\tcost:%d\n\tdescription:%s" % (self.name, self.cost, self.description)

	def action(self):
		self.cast()

class ancestral_healing(Spell):
	def spell(self):
		self.name = "Ancestral Healing"
		self.classs = "Shaman"
		self.cost = 0
		self.description = "Restore a minion to full Health and give it Taunt."

class ancestral_spirit(Spell):
	def spell(self):
		self.name = "Ancestral Spirit"
		self.classs = "Shaman"
		self.cost = 2
		self.description = "Choose a minion. When that minion is destroyed, return it to the battlefield."

class ancient_secrets(Spell):
	def spell(self):
		self.name = "Ancient Secrets"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Restore 5 Health."

class ancient_teachings(Spell):
	def spell(self):
		self.name = "Ancient Teachings"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Draw 2 cards."

class animal_companion(Spell):
	def spell(self):
		self.name = "Animal Companion"
		self.classs = "Hunter"
		self.cost = 3
		self.description = "Summon a random Beast Companion."

class arcane_explosion(Spell):
	def spell(self):
		self.name = "Arcane Explosion"
		self.classs = "Mage"
		self.cost = 2
		self.description = "Deal 1 damage to all enemy minions."

class arcane_intellect(Spell):
	def spell(self):
		self.name = "Arcane Intellect"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Draw 2 cards."

class arcane_missiles(Spell):
	def spell(self):
		self.name = "Arcane Missiles"
		self.classs = "Mage"
		self.cost = 1
		self.description = "Deal 3 damage randomly split among enemy characters."

class arcane_shot(Spell):
	def spell(self):
		self.name = "Arcane Shot"
		self.classs = "Hunter"
		self.cost = 1
		self.description = "Deal 2 damage."

class assassinate(Spell):
	def spell(self):
		self.name = "Assassinate"
		self.classs = "Rogue"
		self.cost = 5
		self.description = "Destroy an enemy minion."

class avenging_wrath(Spell):
	def spell(self):
		self.name = "Avenging Wrath"
		self.classs = "Paladin"
		self.cost = 6
		self.description = "Deal 8 damage randomly split among enemy characters."

class backstab(Spell):
	def spell(self):
		self.name = "Backstab"
		self.classs = "Rogue"
		self.cost = 0
		self.description = "Deal 2 damage to an undamaged minion."

class bananas(Spell):
	def spell(self):
		self.name = "Bananas"
		self.classs = "normal"
		self.cost = 1
		self.description = "Give a minion +1\/+1."

class bane_of_doom(Spell):
	def spell(self):
		self.name = "Bane of Doom"
		self.classs = "Warlock"
		self.cost = 5
		self.description = "Deal 2 damage to a character.  If that kills it, summon a random Demon."

class barrel_toss(Spell):
	def spell(self):
		self.name = "Barrel Toss"
		self.classs = "normal"
		self.cost = 1
		self.description = "Deal 2 damage."

class battle_rage(Spell):
	def spell(self):
		self.name = "Battle Rage"
		self.classs = "Warrior"
		self.cost = 2
		self.description = "Draw a card for each damaged friendly character."

class bear_form(Spell):
	def spell(self):
		self.name = "Bear Form"
		self.classs = "Druid"
		self.cost = 0
		self.description = "+2 Health and Taunt."

class bestial_wrath(Spell):
	def spell(self):
		self.name = "Bestial Wrath"
		self.classs = "Hunter"
		self.cost = 1
		self.description = "Give a Beast +2 Attack and Immune this turn."

class betrayal(Spell):
	def spell(self):
		self.name = "Betrayal"
		self.classs = "Rogue"
		self.cost = 2
		self.description = "Force an enemy minion to deal its damage to the minions next to it."

class bite(Spell):
	def spell(self):
		self.name = "Bite"
		self.classs = "Druid"
		self.cost = 4
		self.description = "Give your hero +4 Attack this turn and 4 Armor."

class blade_flurry(Spell):
	def spell(self):
		self.name = "Blade Flurry"
		self.classs = "Rogue"
		self.cost = 2
		self.description = "Destroy your weapon and deal its damage to all enemies."

class blessed_champion(Spell):
	def spell(self):
		self.name = "Blessed Champion"
		self.classs = "Paladin"
		self.cost = 5
		self.description = "Double a minion's Attack."

class blessing_of_kings(Spell):
	def spell(self):
		self.name = "Blessing of Kings"
		self.classs = "Paladin"
		self.cost = 4
		self.description = "Give a minion +4\/+4. (+4 Attack\/+4 Health)"

class blessing_of_might(Spell):
	def spell(self):
		self.name = "Blessing of Might"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Give a minion +3 Attack."

class blessing_of_wisdom(Spell):
	def spell(self):
		self.name = "Blessing of Wisdom"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Choose a minion.  Whenever it attacks, draw a card."

class blizzard(Spell):
	def spell(self):
		self.name = "Blizzard"
		self.classs = "Mage"
		self.cost = 6
		self.description = "Deal 2 damage to all enemy minions and Freeze them."

class bloodlust(Spell):
	def spell(self):
		self.name = "Bloodlust"
		self.classs = "Shaman"
		self.cost = 5
		self.description = "Give your minions +3 Attack this turn."

class brawl(Spell):
	def spell(self):
		self.name = "Brawl"
		self.classs = "Warrior"
		self.cost = 5
		self.description = "Destroy all minions except one.  (chosen randomly)"

class cat_form(Spell):
	def spell(self):
		self.name = "Cat Form"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Charge"

class charge(Spell):
	def spell(self):
		self.name = "Charge"
		self.classs = "Warrior"
		self.cost = 3
		self.description = "Give a friendly minion +2 Attack and Charge."

class circle_of_healing(Spell):
	def spell(self):
		self.name = "Circle of Healing"
		self.classs = "Priest"
		self.cost = 0
		self.description = "Restore 4 Health to ALL minions."

class claw(Spell):
	def spell(self):
		self.name = "Claw"
		self.classs = "Druid"
		self.cost = 1
		self.description = "Give your hero +2 Attack this turn and 2 Armor."

class cleave(Spell):
	def spell(self):
		self.name = "Cleave"
		self.classs = "Warrior"
		self.cost = 2
		self.description = "Deal 2 damage to two random enemy minions."

class cold_blood(Spell):
	def spell(self):
		self.name = "Cold Blood"
		self.classs = "Rogue"
		self.cost = 1
		self.description = "Give a minion +2 Attack. Combo: +4 Attack instead."

class commanding_shout(Spell):
	def spell(self):
		self.name = "Commanding Shout"
		self.classs = "Warrior"
		self.cost = 2
		self.description = "Your minions can't be reduced below 1 Health this turn.  Draw a card."

class conceal(Spell):
	def spell(self):
		self.name = "Conceal"
		self.classs = "Rogue"
		self.cost = 1
		self.description = "Give your minions Stealth until your next turn."

class cone_of_cold(Spell):
	def spell(self):
		self.name = "Cone of Cold"
		self.classs = "Mage"
		self.cost = 4
		self.description = "Freeze a minion and the minions next to it, and deal 1 damage to them."

class consecration(Spell):
	def spell(self):
		self.name = "Consecration"
		self.classs = "Paladin"
		self.cost = 4
		self.description = "Deal 2 damage to all enemies."

class corruption(Spell):
	def spell(self):
		self.name = "Corruption"
		self.classs = "Warlock"
		self.cost = 1
		self.description = "Choose an enemy minion.   At the start of your turn, destroy it."

class counterspell(Spell):
	def spell(self):
		self.name = "Counterspell"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Secret: When your opponent casts a spell, Counter it."

class deadly_poison(Spell):
	def spell(self):
		self.name = "Deadly Poison"
		self.classs = "Rogue"
		self.cost = 1
		self.description = "Give your weapon +2 Attack."

class deadly_shot(Spell):
	def spell(self):
		self.name = "Deadly Shot"
		self.classs = "Hunter"
		self.cost = 3
		self.description = "Destroy a random enemy minion."

class demigods_favor(Spell):
	def spell(self):
		self.name = "Demigod's Favor"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Give your other minions +2\/+2."

class demonfire(Spell):
	def spell(self):
		self.name = "Demonfire"
		self.classs = "Warlock"
		self.cost = 2
		self.description = "Deal 2 damage to a minion.   If it\u2019s a friendly Demon, give it +2\/+2 instead."

class dispel(Spell):
	def spell(self):
		self.name = "Dispel"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Silence a minion."

class divine_favor(Spell):
	def spell(self):
		self.name = "Divine Favor"
		self.classs = "Paladin"
		self.cost = 3
		self.description = "Draw cards until you have as many in hand as your opponent."

class divine_spirit(Spell):
	def spell(self):
		self.name = "Divine Spirit"
		self.classs = "Priest"
		self.cost = 2
		self.description = "Double a minion's Health."

class drain_life(Spell):
	def spell(self):
		self.name = "Drain Life"
		self.classs = "Warlock"
		self.cost = 3
		self.description = "Deal 2 damage. Restore 2 Health to your hero."

class dream(Spell):
	def spell(self):
		self.name = "Dream"
		self.classs = "normal"
		self.cost = 0
		self.description = "Return a minion to its owner's hand."

class earth_shock(Spell):
	def spell(self):
		self.name = "Earth Shock"
		self.classs = "Shaman"
		self.cost = 1
		self.description = "Silence a minion, then deal 1 damage to it."

class equality(Spell):
	def spell(self):
		self.name = "Equality"
		self.classs = "Paladin"
		self.cost = 2
		self.description = "Change the Health of ALL minions to 1."

class eviscerate(Spell):
	def spell(self):
		self.name = "Eviscerate"
		self.classs = "Rogue"
		self.cost = 2
		self.description = "Deal 2 damage. Combo: Deal 4 damage instead."

class excess_mana(Spell):
	def spell(self):
		self.name = "Excess Mana"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Draw a card. (You can only have 10 Mana in your tray.)"

class execute(Spell):
	def spell(self):
		self.name = "Execute"
		self.classs = "Warrior"
		self.cost = 1
		self.description = "Destroy a damaged enemy minion."

class explosive_shot(Spell):
	def spell(self):
		self.name = "Explosive Shot"
		self.classs = "Hunter"
		self.cost = 5
		self.description = "Deal 5 damage to a minion and 2 damage to adjacent ones."

class explosive_trap(Spell):
	def spell(self):
		self.name = "Explosive Trap"
		self.classs = "Hunter"
		self.cost = 2
		self.description = "Secret: When your hero is attacked, deal 2 damage to all enemies."

class eye_for_an_eye(Spell):
	def spell(self):
		self.name = "Eye for an Eye"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Secret: When your hero takes damage, deal that much damage to the enemy hero."

class fan_of_knives(Spell):
	def spell(self):
		self.name = "Fan of Knives"
		self.classs = "Rogue"
		self.cost = 3
		self.description = "Deal 1 damage to all enemy minions. Draw a card."

class far_sight(Spell):
	def spell(self):
		self.name = "Far Sight"
		self.classs = "Shaman"
		self.cost = 3
		self.description = "Draw a card. That card costs (3) less."

class feral_spirit(Spell):
	def spell(self):
		self.name = "Feral Spirit"
		self.classs = "Shaman"
		self.cost = 3
		self.description = "Summon two 2\/3 Spirit Wolves with Taunt. Overload: (2)"

class fireball(Spell):
	def spell(self):
		self.name = "Fireball"
		self.classs = "Mage"
		self.cost = 4
		self.description = "Deal 6 damage."

class flame_burst(Spell):
	def spell(self):
		self.name = "Flame Burst"
		self.classs = "normal"
		self.cost = 3
		self.description = "Shoot 5 missiles at random enemies for 1 damage each."

class flamestrike(Spell):
	def spell(self):
		self.name = "Flamestrike"
		self.classs = "Mage"
		self.cost = 7
		self.description = "Deal 4 damage to all enemy minions."

class flare(Spell):
	def spell(self):
		self.name = "Flare"
		self.classs = "Hunter"
		self.cost = 1
		self.description = "All minions lose Stealth. Destroy all enemy Secrets. Draw a card."

class force_of_nature(Spell):
	def spell(self):
		self.name = "Force of Nature"
		self.classs = "Druid"
		self.cost = 6
		self.description = "Summon three 2\/2 Treants with Charge that die at the end of the turn."

class forked_lightning(Spell):
	def spell(self):
		self.name = "Forked Lightning"
		self.classs = "Shaman"
		self.cost = 1
		self.description = "Deal 2 damage to 2 random enemy minions. Overload: (2)"

class freezing_trap(Spell):
	def spell(self):
		self.name = "Freezing Trap"
		self.classs = "Hunter"
		self.cost = 2
		self.description = "Secret: When an enemy minion attacks, return it to its owner's hand and it costs (2) more."

class frost_nova(Spell):
	def spell(self):
		self.name = "Frost Nova"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Freeze all enemy minions."

class frost_shock(Spell):
	def spell(self):
		self.name = "Frost Shock"
		self.classs = "Shaman"
		self.cost = 1
		self.description = "Deal 1 damage to an enemy character and Freeze it."

class frostbolt(Spell):
	def spell(self):
		self.name = "Frostbolt"
		self.classs = "Mage"
		self.cost = 2
		self.description = "Deal 3 damage to a character and Freeze it."

class hammer_of_wrath(Spell):
	def spell(self):
		self.name = "Hammer of Wrath"
		self.classs = "Paladin"
		self.cost = 4
		self.description = "Deal 3 damage.  Draw a card."

class hand_of_protection(Spell):
	def spell(self):
		self.name = "Hand of Protection"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Give a minion Divine Shield."

class headcrack(Spell):
	def spell(self):
		self.name = "Headcrack"
		self.classs = "Rogue"
		self.cost = 3
		self.description = "Deal 2 damage to the enemy hero. Combo: Return this to your hand next turn."

class healing_touch(Spell):
	def spell(self):
		self.name = "Healing Touch"
		self.classs = "Druid"
		self.cost = 3
		self.description = "Restore 8 Health."

class hellfire(Spell):
	def spell(self):
		self.name = "Hellfire"
		self.classs = "Warlock"
		self.cost = 4
		self.description = "Deal 3 damage to ALL characters."

class heroic_strike(Spell):
	def spell(self):
		self.name = "Heroic Strike"
		self.classs = "Warrior"
		self.cost = 2
		self.description = "Give your hero +4 Attack this turn."

class hex(Spell):
	def spell(self):
		self.name = "Hex"
		self.classs = "Shaman"
		self.cost = 3
		self.description = "Transform a minion into a 0\/1 Frog with Taunt."

class hogger_smash(Spell):
	def spell(self):
		self.name = "Hogger SMASH!"
		self.classs = "normal"
		self.cost = 3
		self.description = "Deal 4 damage."

class holy_fire(Spell):
	def spell(self):
		self.name = "Holy Fire"
		self.classs = "Priest"
		self.cost = 6
		self.description = "Deal 5 damage.  Restore 5 Health to your hero."

class holy_light(Spell):
	def spell(self):
		self.name = "Holy Light"
		self.classs = "Paladin"
		self.cost = 2
		self.description = "Restore 6 Health."

class holy_nova(Spell):
	def spell(self):
		self.name = "Holy Nova"
		self.classs = "Priest"
		self.cost = 5
		self.description = "Deal 2 damage to all enemies.  Restore 2 Health to all  friendly characters."

class holy_smite(Spell):
	def spell(self):
		self.name = "Holy Smite"
		self.classs = "Priest"
		self.cost = 1
		self.description = "Deal 2 damage."

class holy_wrath(Spell):
	def spell(self):
		self.name = "Holy Wrath"
		self.classs = "Paladin"
		self.cost = 5
		self.description = "Draw a card and deal damage equal to its cost."

class humility(Spell):
	def spell(self):
		self.name = "Humility"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Change a minion's Attack to 1."

class hunters_mark(Spell):
	def spell(self):
		self.name = "Hunter's Mark"
		self.classs = "Hunter"
		self.cost = 0
		self.description = "Change a minion's Health to 1."

class i_am_murloc(Spell):
	def spell(self):
		self.name = "I Am Murloc"
		self.classs = "normal"
		self.cost = 4
		self.description = "Summon three, four, or five 1\/1 Murlocs."

class ice_barrier(Spell):
	def spell(self):
		self.name = "Ice Barrier"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Secret: As soon as your hero is attacked, gain 8 Armor."

class ice_block(Spell):
	def spell(self):
		self.name = "Ice Block"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Secret: When your hero takes fatal damage, prevent it and become Immune this turn."

class ice_lance(Spell):
	def spell(self):
		self.name = "Ice Lance"
		self.classs = "Mage"
		self.cost = 1
		self.description = "Freeze a character. If it was already Frozen, deal 4 damage instead."

class inner_fire(Spell):
	def spell(self):
		self.name = "Inner Fire"
		self.classs = "Priest"
		self.cost = 1
		self.description = "Change a minion's Attack to be equal to its Health."

class inner_rage(Spell):
	def spell(self):
		self.name = "Inner Rage"
		self.classs = "Warrior"
		self.cost = 0
		self.description = "Deal 1 damage to a minion and give it +2 Attack."

class innervate(Spell):
	def spell(self):
		self.name = "Innervate"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Gain 2 Mana Crystals this turn only."

class kill_command(Spell):
	def spell(self):
		self.name = "Kill Command"
		self.classs = "Hunter"
		self.cost = 3
		self.description = "Deal 3 damage.  If you have a Beast, deal 5 damage instead."

class lava_burst(Spell):
	def spell(self):
		self.name = "Lava Burst"
		self.classs = "Shaman"
		self.cost = 3
		self.description = "Deal 5 damage. Overload: (2)"

class lay_on_hands(Spell):
	def spell(self):
		self.name = "Lay on Hands"
		self.classs = "Paladin"
		self.cost = 8
		self.description = "Restore 8 Health. Draw 3 cards."

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

class lightning_bolt(Spell):
	def spell(self):
		self.name = "Lightning Bolt"
		self.classs = "Shaman"
		self.cost = 1
		self.description = "Deal 3 damage. Overload: (1)"

class lightning_storm(Spell):
	def spell(self):
		self.name = "Lightning Storm"
		self.classs = "Shaman"
		self.cost = 3
		self.description = "Deal 2-3 damage to all enemy minions. Overload: (2)"

class mark_of_nature(Spell):
	def spell(self):
		self.name = "Mark of Nature"
		self.classs = "Druid"
		self.cost = 3
		self.description = "Choose One - Give a minion +4 Attack; or +4 Health and Taunt."

class mark_of_the_wild(Spell):
	def spell(self):
		self.name = "Mark of the Wild"
		self.classs = "Druid"
		self.cost = 2
		self.description = "Give a minion Taunt and +2\/+2. (+2 Attack\/+2 Health)"

class mass_dispel(Spell):
	def spell(self):
		self.name = "Mass Dispel"
		self.classs = "Priest"
		self.cost = 4
		self.description = "Silence all enemy minions. Draw a card."

class metamorphosis(Spell):
	def spell(self):
		self.name = "Metamorphosis"
		self.classs = "normal"
		self.cost = 6
		self.description = "Do something crazy."

class mind_blast(Spell):
	def spell(self):
		self.name = "Mind Blast"
		self.classs = "Priest"
		self.cost = 2
		self.description = "Deal 5 damage to the enemy hero."

class mind_control(Spell):
	def spell(self):
		self.name = "Mind Control"
		self.classs = "Priest"
		self.cost = 10
		self.description = "Take control of an enemy minion."

class mind_vision(Spell):
	def spell(self):
		self.name = "Mind Vision"
		self.classs = "Priest"
		self.cost = 1
		self.description = "Put a copy of a random card in your opponent's hand into your hand."

class mindgames(Spell):
	def spell(self):
		self.name = "Mindgames"
		self.classs = "Priest"
		self.cost = 4
		self.description = "Put a copy of a random minion from your opponent's deck into the battlefield."

class mirror_entity(Spell):
	def spell(self):
		self.name = "Mirror Entity"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Secret: When your opponent plays a minion, summon a copy of it."

class mirror_image(Spell):
	def spell(self):
		self.name = "Mirror Image"
		self.classs = "Mage"
		self.cost = 1
		self.description = "Summon two 0\/2 minions with Taunt."

class misdirection(Spell):
	def spell(self):
		self.name = "Misdirection"
		self.classs = "Hunter"
		self.cost = 2
		self.description = "Secret: When a character attacks your hero, instead he attacks another random character."

class moonfire(Spell):
	def spell(self):
		self.name = "Moonfire"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Deal 1 damage."

class mortal_coil(Spell):
	def spell(self):
		self.name = "Mortal Coil"
		self.classs = "Warlock"
		self.cost = 1
		self.description = "Deal 1 damage to a minion. If that kills it, draw a card."

class mortal_strike(Spell):
	def spell(self):
		self.name = "Mortal Strike"
		self.classs = "Warrior"
		self.cost = 4
		self.description = "Deal 4 damage.  If you have 12 or less Health, deal 6 instead."

class multishot(Spell):
	def spell(self):
		self.name = "Multi-Shot"
		self.classs = "Hunter"
		self.cost = 4
		self.description = "Deal 3 damage to two random enemy minions."

class noooooooooooo(Spell):
	def spell(self):
		self.name = "NOOOOOOOOOOOO"
		self.classs = "normal"
		self.cost = 2
		self.description = "Somehow, the card you USED to have has been deleted.  Here, have this one instead!"

class naturalize(Spell):
	def spell(self):
		self.name = "Naturalize"
		self.classs = "Druid"
		self.cost = 1
		self.description = "Destroy a minion. Your opponent draws 2 cards."

class nightmare(Spell):
	def spell(self):
		self.name = "Nightmare"
		self.classs = "normal"
		self.cost = 0
		self.description = "Give a minion +5\/+5.  At the start of your next turn, destroy it."

class noble_sacrifice(Spell):
	def spell(self):
		self.name = "Noble Sacrifice"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Secret: When an enemy attacks, summon a 2\/1 Defender as the new target."

class nourish(Spell):
	def spell(self):
		self.name = "Nourish"
		self.classs = "Druid"
		self.cost = 5
		self.description = "Choose One - Gain 2 Mana Crystals; or Draw 3 cards."

class polymorph(Spell):
	def spell(self):
		self.name = "Polymorph"
		self.classs = "Mage"
		self.cost = 4
		self.description = "Transform a minion into a 1\/1 Sheep."

class power_overwhelming(Spell):
	def spell(self):
		self.name = "Power Overwhelming"
		self.classs = "Warlock"
		self.cost = 1
		self.description = "Give a friendly minion +4\/+4 until end of turn. Then, it dies. Horribly."

class power_word_shield(Spell):
	def spell(self):
		self.name = "Power Word: Shield"
		self.classs = "Priest"
		self.cost = 1
		self.description = "Give a minion +2 Health. Draw a card."

class power_of_the_horde(Spell):
	def spell(self):
		self.name = "Power of the Horde"
		self.classs = "normal"
		self.cost = 4
		self.description = "Summon a random Horde Warrior."

class power_of_the_wild(Spell):
	def spell(self):
		self.name = "Power of the Wild"
		self.classs = "Druid"
		self.cost = 2
		self.description = "Choose One - Give your minions +1\/+1; or Summon a 3\/2 Panther."

class preparation(Spell):
	def spell(self):
		self.name = "Preparation"
		self.classs = "Rogue"
		self.cost = 0
		self.description = "The next spell you cast this turn costs (3) less."

class pyroblast(Spell):
	def spell(self):
		self.name = "Pyroblast"
		self.classs = "Mage"
		self.cost = 10
		self.description = "Deal 10 damage."

class rampage(Spell):
	def spell(self):
		self.name = "Rampage"
		self.classs = "Warrior"
		self.cost = 2
		self.description = "Give a damaged minion +3\/+3."

class redemption(Spell):
	def spell(self):
		self.name = "Redemption"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Secret: When one of your minions dies, return it to life with 1 Health."

class repentance(Spell):
	def spell(self):
		self.name = "Repentance"
		self.classs = "Paladin"
		self.cost = 1
		self.description = "Secret: When your opponent plays a minion, reduce its Health to 1."

class rockbiter_weapon(Spell):
	def spell(self):
		self.name = "Rockbiter Weapon"
		self.classs = "Shaman"
		self.cost = 1
		self.description = "Give a friendly character +3 Attack this turn."

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

class sacrificial_pact(Spell):
	def spell(self):
		self.name = "Sacrificial Pact"
		self.classs = "Warlock"
		self.cost = 0
		self.description = "Destroy a Demon. Restore 5 Health to your hero."

class sap(Spell):
	def spell(self):
		self.name = "Sap"
		self.classs = "Rogue"
		self.cost = 2
		self.description = "Return an enemy minion to your opponent's hand."

class savage_roar(Spell):
	def spell(self):
		self.name = "Savage Roar"
		self.classs = "Druid"
		self.cost = 3
		self.description = "Give your characters +2 Attack this turn."

class savagery(Spell):
	def spell(self):
		self.name = "Savagery"
		self.classs = "Druid"
		self.cost = 1
		self.description = "Deal damage equal to your hero's Attack to a minion."

class sense_demons(Spell):
	def spell(self):
		self.name = "Sense Demons"
		self.classs = "Warlock"
		self.cost = 3
		self.description = "Put 2 random Demons from your deck into your hand."

class shadow_bolt(Spell):
	def spell(self):
		self.name = "Shadow Bolt"
		self.classs = "Warlock"
		self.cost = 3
		self.description = "Deal 4 damage to a minion."

class shadow_madness(Spell):
	def spell(self):
		self.name = "Shadow Madness"
		self.classs = "Priest"
		self.cost = 4
		self.description = "Gain control of an enemy minion with 3 or less Attack until end of turn."

class shadow_word_death(Spell):
	def spell(self):
		self.name = "Shadow Word: Death"
		self.classs = "Priest"
		self.cost = 3
		self.description = "Destroy a minion with an Attack of 5 or more."

class shadow_word_pain(Spell):
	def spell(self):
		self.name = "Shadow Word: Pain"
		self.classs = "Priest"
		self.cost = 2
		self.description = "Destroy a minion with 3 or less Attack."

class shadowflame(Spell):
	def spell(self):
		self.name = "Shadowflame"
		self.classs = "Warlock"
		self.cost = 4
		self.description = "Destroy a friendly minion and deal its Attack damage to all enemy minions."

class shadowform(Spell):
	def spell(self):
		self.name = "Shadowform"
		self.classs = "Priest"
		self.cost = 3
		self.description = "Your Hero Power becomes 'Deal 2 damage'. If already in Shadowform: 3 damage."

class shadowstep(Spell):
	def spell(self):
		self.name = "Shadowstep"
		self.classs = "Rogue"
		self.cost = 0
		self.description = "Return a friendly minion to your hand. It costs (2) less."

class shandos_lesson(Spell):
	def spell(self):
		self.name = "Shan'do's Lesson"
		self.classs = "Druid"
		self.cost = 0
		self.description = "Summon two 2\/2 Treants with Taunt."

class shield_block(Spell):
	def spell(self):
		self.name = "Shield Block"
		self.classs = "Warrior"
		self.cost = 3
		self.description = "Gain 5 Armor.  Draw a card."

class shield_slam(Spell):
	def spell(self):
		self.name = "Shield Slam"
		self.classs = "Warrior"
		self.cost = 1
		self.description = "Deal 1 damage to a minion for each Armor you have."

class shiv(Spell):
	def spell(self):
		self.name = "Shiv"
		self.classs = "Rogue"
		self.cost = 2
		self.description = "Deal 1 damage. Draw a card."

class silence(Spell):
	def spell(self):
		self.name = "Silence"
		self.classs = "Priest"
		self.cost = 0
		self.description = "Silence a minion."

class sinister_strike(Spell):
	def spell(self):
		self.name = "Sinister Strike"
		self.classs = "Rogue"
		self.cost = 1
		self.description = "Deal 3 damage to the enemy hero."

class siphon_soul(Spell):
	def spell(self):
		self.name = "Siphon Soul"
		self.classs = "Warlock"
		self.cost = 6
		self.description = "Destroy a minion. Restore 3 Health to your hero."

class slam(Spell):
	def spell(self):
		self.name = "Slam"
		self.classs = "Warrior"
		self.cost = 2
		self.description = "Deal 2 damage to a minion.  If it survives, draw a card."

class snake_trap(Spell):
	def spell(self):
		self.name = "Snake Trap"
		self.classs = "Hunter"
		self.cost = 2
		self.description = "Secret: When one of your minions is attacked, summon three 1\/1 Snakes."

class snipe(Spell):
	def spell(self):
		self.name = "Snipe"
		self.classs = "Hunter"
		self.cost = 2
		self.description = "Secret: When your opponent plays a minion, deal 4 damage to it."

class soul_of_the_forest(Spell):
	def spell(self):
		self.name = "Soul of the Forest"
		self.classs = "Druid"
		self.cost = 4
		self.description = "Give your minions\"Deathrattle: Summon a 2\/2 Treant.\""

class soulfire(Spell):
	def spell(self):
		self.name = "Soulfire"
		self.classs = "Warlock"
		self.cost = 0
		self.description = "Deal 4 damage. Discard a random card."

class spellbender(Spell):
	def spell(self):
		self.name = "Spellbender"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Secret: When an enemy casts a spell on a minion, summon a 1\/3 as the new target."

class sprint(Spell):
	def spell(self):
		self.name = "Sprint"
		self.classs = "Rogue"
		self.cost = 7
		self.description = "Draw 4 cards."

class starfall(Spell):
	def spell(self):
		self.name = "Starfall"
		self.classs = "Druid"
		self.cost = 5
		self.description = "Choose One - Deal 5 damage to a minion; or 2 damage to all enemy minions."

class starfire(Spell):
	def spell(self):
		self.name = "Starfire"
		self.classs = "Druid"
		self.cost = 6
		self.description = "Deal 5 damage.  Draw a card."

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

class swipe(Spell):
	def spell(self):
		self.name = "Swipe"
		self.classs = "Druid"
		self.cost = 4
		self.description = "Deal 4 damage to an enemy and 1 damage to all other enemies."

class the_coin(Spell):
	def spell(self):
		self.name = "The Coin"
		self.classs = "normal"
		self.cost = 0
		self.description = "Gain 1 Mana Crystal this turn only."

class thoughtsteal(Spell):
	def spell(self):
		self.name = "Thoughtsteal"
		self.classs = "Priest"
		self.cost = 3
		self.description = "Copy 2 cards from your opponent's deck and put them into your hand."

class totemic_might(Spell):
	def spell(self):
		self.name = "Totemic Might"
		self.classs = "Shaman"
		self.cost = 0
		self.description = "Give your Totems +2 Health."

class tracking(Spell):
	def spell(self):
		self.name = "Tracking"
		self.classs = "Hunter"
		self.cost = 1
		self.description = "Look at the top three cards of your deck. Draw one and discard the others."

class transcendence(Spell):
	def spell(self):
		self.name = "Transcendence"
		self.classs = "normal"
		self.cost = 1
		self.description = "Until you kill Cho's minions, he can't be attacked."

class twisting_nether(Spell):
	def spell(self):
		self.name = "Twisting Nether"
		self.classs = "Warlock"
		self.cost = 8
		self.description = "Destroy all minions."

class unleash_the_hounds(Spell):
	def spell(self):
		self.name = "Unleash the Hounds"
		self.classs = "Hunter"
		self.cost = 2
		self.description = "For each enemy minion, summon a 1\/1 Hound with Charge."

class upgrade(Spell):
	def spell(self):
		self.name = "Upgrade!"
		self.classs = "Warrior"
		self.cost = 1
		self.description = "If you have a weapon, give it +1\/+1.  Otherwise equip a 1\/3 weapon."

class uproot(Spell):
	def spell(self):
		self.name = "Uproot"
		self.classs = "Druid"
		self.cost = 0
		self.description = "+5 Attack."

class vanish(Spell):
	def spell(self):
		self.name = "Vanish"
		self.classs = "Rogue"
		self.cost = 6
		self.description = "Return all minions to their owner's hand."

class vaporize(Spell):
	def spell(self):
		self.name = "Vaporize"
		self.classs = "Mage"
		self.cost = 3
		self.description = "Secret: When a minion attacks your hero, destroy it."

class whirlwind(Spell):
	def spell(self):
		self.name = "Whirlwind"
		self.classs = "Warrior"
		self.cost = 1
		self.description = "Deal 1 damage to ALL minions."

class wild_growth(Spell):
	def spell(self):
		self.name = "Wild Growth"
		self.classs = "Druid"
		self.cost = 2
		self.description = "Gain an empty Mana Crystal."

class will_of_mukla(Spell):
	def spell(self):
		self.name = "Will of Mukla"
		self.classs = "normal"
		self.cost = 3
		self.description = "Restore 8 Health."

class windfury(Spell):
	def spell(self):
		self.name = "Windfury"
		self.classs = "Shaman"
		self.cost = 2
		self.description = "Give a minion Windfury."

class wrath(Spell):
	def spell(self):
		self.name = "Wrath"
		self.classs = "Druid"
		self.cost = 2
		self.description = "Choose One - Deal 3 damage to a minion; or 1 damage and draw a card."

class ysera_awakens(Spell):
	def spell(self):
		self.name = "Ysera Awakens"
		self.classs = "normal"
		self.cost = 2
		self.description = "Deal 5 damage to all characters except Ysera."

