from general import Hearth
import hero as H
import minion as M
import effects as E


if __name__ == "__main__":
	enemy = H.Druid()
	for hero in [H.Druid, H.Paladin, H.Hunter, H.Mage, H.Priest, H.Warrior, H.Warlock, H.Shaman, H.Rogue]:
		chris = hero()
		print "=================="
		print chris
		print "=================="
		print enemy
		print "=========================="
		chris.turnUpdate()
		chris.heroPower(enemy)
		chris.attack_(enemy)
		print "=========================="
		print chris
		print enemy

		raw_input()

	
