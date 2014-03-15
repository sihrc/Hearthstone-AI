from hearth import *
import hero as H
import minion as M
import weapon as W
import effect as E
import spell as S

import sys

def test(func):
	"""
	Testing Suite Wrapper
	"""
	def wrapper(*args, **kwarges):
		log("BEGINNING TEST SUITE FOR %s" % func.__name__)
		for hero in [H.Druid, H.Paladin, H.Hunter, H.Mage, H.Priest, H.Warrior, H.Warlock, H.Shaman, H.Rogue]:
			with RedirectStdStreams(stdout=open("output",'wb'), stderr=None):
				hero, enemy = setupBoard(hero)
			div()
			print "Testing %s" % (hero.name)
			print
			res = func(hero, enemy, **kwarges)
			print
			print "%s passed" % (hero.name)
			div()
			raw_input()

		return res
	return wrapper

"""
TESTS
"""

@shutup
def setupBoard(hero):
	enemy = H.Druid()
	hero = hero()
	enemy.enemy = hero
	hero.enemy = enemy
	hero.update()
	enemy.update()
	return hero, enemy

@test
def attackWithHeroPower(hero,enemy):
	# log(hero, enemy)
	hero.heroPower(enemy)
	hero.attack_(enemy)
	# log(hero, enemy)

@test
def summoningMinion(hero,enemy, minion = M.silver_hand_recruit):
	hero.summon(minion, 0)


@test
def equipWeapon(hero, enemy, weapon = W.ashbringer):
	# log(hero, enemy)
	hero.update()
	hero.update()
	hero.update()
	hero.equip(weapon)
	hero.heroAttack()
	# log(hero, enemy)

@test
def useSpell(hero, enemy, spell = S.ancient_secrets):
	hero.update()
	hero.update()
	hero.update()
	hero.hand.append(spell(hero))
	log(hero, enemy)
	hero.playCard(hero.hand[0])
	log(hero, enemy)

if __name__ == "__main__":
	useSpell(spell = S.ancient_secrets)
