class Item:
	name = ""
	#measured in lbs
	weight = 0
	#measured in gold
	value = 0
	#can be picked up as weapon
	isWieldable = False
	description = ""

	def __init__(self, name, weight):
		self.name = name;
		self.weight= weight;

	def getWeight(self):
		return self.weight
	def setValue(self, value):
		self.value = value
		return self

class Container(Item):
	contents = []

	def __init__(self, name, weight):
		Item.__init__(self, name, weight)
		isWieldable = False
	def getWeight(self):
		sum = weight;
		for x in contents:
			sum = sum + x.getWeight()
		return sum
	def addObject(self, object):
		contents.append(object)
	def removeObject(self, object):
		contents.remove(object)

class Weapon(Item):

	def __init__(self):
		damageValue = 1

item_cheese = Item("Cheese Wheel", 2)
item_stone1 = Item("Pebble", .5)
item_stone2 = Item("Stone", 1)
item_stone3 = Item("Rock", 15)
item_stone4 = Item("Boulder", 50)
item_hammer = Item("Hammer", 2).setValue(2)
item_metal_rod = Item("Metal Rod", 2).setValue(1)
item_string = Item("String", .1)
item_bone = Item("Bone", 1).setValue(0.5)
item_gold = Item("Gold Coin", 0.25)
item_silver = Item("Silver", 0.25).setValue(0.5)

item_key1 = Item("Key", 0)
item_key2 = Item("Key", 0)
item_key3 = Item("Key", 0)
item_key4 = Item("Key", 0)
item_key5 = Item("Key", 0)
item_key6 = Item("Key", 0)

item_chest = Container("Oak Chest", 30)
item_sack = Container("Cloth Sack", 1)
item_quiver = Container("Quiver", 1)



