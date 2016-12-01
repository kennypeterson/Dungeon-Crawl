#CRAWL MAIN FILE
import Dictionary
from Area import Area
from Item import Item

turnNumber = 1

area = Area()
cheese = Item("Cheese Wheel",10)


area.objects.append(cheese)
area.objects.append(cheese)


while(True):
	cmd = input("Turn: " + str(turnNumber) + "  >>")
	if(Dictionary.isValidCommand(cmd)):
		turnNumber = turnNumber + 1
		Dictionary.processCommand(cmd, area)
	else:
		print("Not a recognized command")
