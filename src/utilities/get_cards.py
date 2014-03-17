"""
Utilities file to help download and write classes for cards in hearthstone

author: chris @ sihrc
"""

import urllib2, re, json, os
from bs4 import BeautifulSoup as soup
import pickle as p


def grabCardsFromDatabase(urls):
	"""
	Grabs HTML from hearthhead database and parses for hearthstone card json
	"""
	list_of_cards = []
	for url in urls:
		page = urllib2.urlopen(url)
		read = page.read()
		jsonArray = re.search("var hearthstoneCards = .+?]",read).group(0)
		exec(jsonArray[4:].replace("popularity",'"popularity"').replace("\"", "\\\""))
		list_of_cards += hearthstoneCards
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
	attack = minion["attack"] if "attack" in minion else 0
	race = races[minion["race"]] if "race" in minion else "normal"
	classs = classes[minion["classs"]] if "classs" in minion else "normal"
	return "class %s(Minion):\n\tdef minion(self):\n\t\tself.name = \"%s\"\n\t\tself.classs = \"%s\"\n\t\tself.attack = %s\n\t\tself.health = %d\n\t\tself.cost = %d\n\t\tself.race = \"%s\"\n\t\tself.description = \"%s\"\n\n"\
	 % ("_".join(re.sub(r'([^\s\w]|_)+', '', minion["name"].lower()).split()), minion["name"],  classs, attack, minion["health"], minion["cost"], race, descr)

def spellCode(spell):
	"""
	Helper Function to write Spell Class
	"""
	descr = spell["description"] if "description" in spell else ""
	classs = classes[spell["classs"]] if "classs" in spell else "normal"
	return "class %s(Spell):\n\tdef spell(self):\n\t\tself.name = \"%s\"\n\t\tself.classs = \"%s\"\n\t\tself.cost = %d\n\t\tself.description = \"%s\"\n\n"\
	 % ("_".join(re.sub(r'([^\s\w]|_)+', '', spell["name"].lower()).split()), spell["name"], classs, spell["cost"], descr)

def weaponCode(weapon):
	"""
	Helper Function to write Weapon Class
	"""
	descr = weapon["description"] if "description" in weapon else ""
	classs = classes[weapon["classs"]] if "classs" in weapon else "normal"
	return "class %s(Weapon):\n\tdef weapon(self):\n\t\tself.name = \"%s\"\n\t\tself.classs = \"%s\"\n\t\tself.attack = %s\n\t\tself.health = %d\n\t\tself.cost = %d\n\t\tself.description = \"%s\"\n\n"\
	 % ("_".join(re.sub(r'([^\s\w]|_)+', '', weapon["name"].lower()).split()), weapon["name"], classs, weapon["attack"], weapon["durability"], weapon["cost"], descr)


def main(categ):
	saveListToPickle(grabCardsFromDatabase(categ[0]), categ[1])
	writeCode(loadListFromPickle(categ[1]), categ[1], categ[2])

def createDeck(classs, url):
	page = soup(urllib2.urlopen(url).read())
	deckName = re.search("/deck.+/",url).group(0)[1:-1].replace("=","_")
	with open (os.path.join("..","decks","__init__.py"), 'ab') as f:
		f.write("import %s_%s\n" % (classs, deckName))
	with open(os.path.join("..","decks","%s_%s.py" % (classs, deckName)), 'wb') as f:
		f.write("import minion as M\nimport weapon as W\nimport spell as S\nimport deck as D\ncards = [")
		for cardType in page.find_all("div",attrs={"class":"deckguide-cards-type"}):
			code = cardType.h3.text.split()[0][0] + ".%s,"
			for card in cardType.find_all("li"):
				cardText = re.sub(r'([^\s\w]|_)+', '', card.text.lower())
				split = cardText.split()
				if ("x2" in cardText):
					f.write(code % ("_".join(split[:-1])))
					f.write(code % ("_".join(split[:-1])))
				else:
					f.write(code % ("_".join(split)))
		f.write("]\ndeck = D.Deck(cards)")

if __name__ == "__main__":
	classes = {1:"Warrior",2:"Paladin",3:"Hunter", 4:"Rogue", 5:"Priest",11:"Druid",7:"Shaman",8:"Mage",9:"Warlock"}
	minions = (["http://www.hearthhead.com/cards=4","http://www.hearthhead.com/cards?filter=type=4;uc=on"], "minions.p", minionCode)
	spells = (["http://www.hearthhead.com/cards=5" ,"http://www.hearthhead.com/cards?filter=type=5;uc=on"], "spells.p", spellCode)
	weapons = (["http://www.hearthhead.com/cards=7", "http://www.hearthhead.com/cards?filter=type=7;uc=on"], "weapons.p", weaponCode)
	# main(minions)
	# main(spells)
	# main(weapons)
	"""
	Making Decks
	"""
	createDeck("Druid", "http://www.hearthhead.com/deck=550/basic-druid")
	createDeck("Hunter", "http://www.hearthhead.com/deck=586/basic-hunter-deck")

