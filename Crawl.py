#CRAWL MAIN FILE
import Dictionary
import json
import os
from Area import Area
from Item import Item
from pprint import pprint

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

turnNumber = 1
item_dict = []

area = Area()
cheese = Item("Cheese Wheel",10)

area.objects.append(cheese)
area.objects.append(cheese)

class ItemEntry:
	filename = ""
	json = ""
	def __init__(self, filename, json):
		self.filename = filename
		self.json = json


# loading items code
def loadItem(filename):
	rel_path = "items/" + filename
	abs_file_path = os.path.join(script_dir, rel_path)
	with open(abs_file_path, encoding='utf-8') as data_file:
		data = json.loads(data_file.read())
		return data

for file in os.listdir(os.path.join(script_dir, "items/")):
	jsonFile = loadItem(file)
	item_dict.append(ItemEntry(file.replace(".json", ""), jsonFile))

def findItem(name):
	for item in item_dict:
		if(item.filename == name):
			return item


#main loop
while(True):
	cmd = input("Turn: " + str(turnNumber) + "  >>")
	if(Dictionary.isValidCommand(cmd)):
		turnNumber = turnNumber + 1
		Dictionary.processCommand(cmd, area)
	else:
		print("Not a recognized command")
