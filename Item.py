class Item:
	name = ""
	#measured in lbs
	weight = 0
	#measured in gold
	value = 0
	#can be picked up as weapon
	isWieldable = False

	def __init__(self, name, weight):
		self.name = name;
		self.weight= weight;
