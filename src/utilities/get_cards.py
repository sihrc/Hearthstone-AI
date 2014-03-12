"""
Utilities file to help download and write classes for cards in hearthstone

author: chris @ sihrc
"""

import urllib2, re, json
import pickle as p


def grabCardsFromDatabase(url):
	"""
	Grabs HTML from hearthhead database and parses for hearthstone card json
	"""
	list_of_cards = []
	page = urllib2.urlopen(url)
	read = page.read()
	jsonArray = re.search("var hearthstoneCards = .+?]",read).group(0)
	exec(jsonArray[4:].replace("popularity",'"popularity"'))
	list_of_cards.extend(hearthstoneCards)
	return list_of_cards

def saveListToPickle(l, filename):
	"""
	Caches the downloaded information to prevent request blocks
	"""
	with open(filename, 'wb') as f:
		p.dump(l, f)

def loadListFromPickle(filename):
	"""
	Loads cached
	"""
	with open(filename, 'rb') as f:
		list_of_cards = p.load(f)
	return list_of_cards

def writeCode(list_of_cards, filename, code):
	"""
	Writes the code to copy-paste into python script
	"""
	from operator import itemgetter
	counted = []
	with open(filename[:-1] + "txt", 'wb') as f:
		list_of_cards.sort(key=itemgetter("name"))
		for card in list_of_cards:
			if card["name"] in counted:
				continue
			counted.append(card["name"])
			f.write(code(card))

def minionCode(minion):
	"""
	Helper Function to write Minion Class
	"""
	races = {14:"murloc",15:"demon",20:"beast",21:"totem",23:"pirate",24:"dragon"}
	descr = minion["description"] if "description" in minion else ""
	race = races[minion["race"]] if "race" in minion else "normal"
	return "class %s(Minion):\n\tdef minion(self):\n\t\tself.name = \"%s\"\n\t\tself.health = %d\n\t\tself.race = \"%s\"\n\t\tself.attack = %s\n\t\tself.cost = %d\n\t\tself.description = \"%s\"\n\n"\
	 % ("_".join(minion["name"].lower().split()), minion["name"], minion["health"], race, minion["attack"], minion["cost"], descr)

def spellCode(spell):
	"""
	Helper Function to write Spell Class
	"""
	return "" #TO-DO

def main(categ):
	saveListToPickle(grabCardsFromDatabase(categ[0]), categ[1])
	writeCode(loadListFromPickle(categ[1]), categ[1])

if __name__ == "__main__":
	minions = ("http://www.hearthhead.com/cards=4", "minions.p")
	spells = ("http://www.hearthhead.com/cards=5", "spells.p")

	main(minions)

class Spell(Hearth)