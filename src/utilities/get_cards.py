import urllib2, re, json
import pickle as p


def grabCardsFromDatabase():
	list_of_cards = []
	for page_num in xrange(0,240,40):
		page = urllib2.urlopen("http://www.hearthhead.com/cards=4#gallery:%d+1" % (page_num))
		read = page.read()
		jsonArray = re.search("var hearthstoneCards = .+?]",read).group(0)
		exec(jsonArray[4:].replace("popularity",'"popularity"'))
		list_of_cards.extend(hearthstoneCards)
	return list_of_cards

def saveListToPickle(l):
	with open("minions.p", 'wb') as f:
		p.dump(l, f)

def loadListFromPickle():
	with open("minions.p", 'rb') as f:
		list_of_cards = p.load(f)
	return list_of_cards

def writeCode(list_of_cards):
	from operator import itemgetter
	code = "class %s(Minion):\n\tdef minion(self):\n\t\tself.name = \"%s\"\n\t\tself.health = %d\n\t\tself.attack = %d\n\t\tself.cost = %d\n\t\tself.description = \"%s\"\n\n"
	counted = []
	with open("minions_write.txt", 'wb') as f:
		list_of_cards.sort(key=itemgetter("name"))
		for minion in list_of_cards:
			if minion["name"] in counted:
				continue
			counted.append(minion["name"])
			descr = minion["description"] if "description" in minion else ""
			write = code % ("_".join(minion["name"].lower().split()), minion["name"], minion["health"], minion["attack"], minion["cost"], descr)
			f.write(write)

if __name__ == "__main__":
	saveListToPickle(grabCardsFromDatabase())
	writeCode(loadListFromPickle())

