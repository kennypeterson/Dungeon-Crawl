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

class Container(Item):
	contents = []

	def __init__(self, name, weight):
		Item.__init__(self, name, weight)
		isWieldable = False;

item_cheese = Item("Cheese Wheel", 2)
item_stone1 = Item("Pebble", .5)
item_stone2 = Item("Stone", 1)
item_stone3 = Item("Rock", 15)
item_stone4 = Item("Boulder", 50)
item_hammer = Item("Hammer", 2)
item_metal_rod = Item("Metal Rod", 2)
item_string = Item("String", .1)
item_key1 = Item("Key", 0)
item_key2 = Item("Key", 0)
item_key3 = Item("Key", 0)
item_key4 = Item("Key", 0)
item_key5 = Item("Key", 0)
item_key6 = Item("Key", 0)


