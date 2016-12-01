def isValidCommand(command):
	command = command.lower()
	parsed = command.split(" ")
	if(parsed[0] == "eat"):
		return True
	if(parsed[0] == "examine"):
		return True

def processCommand(command, area):
	command = command.lower()
	parsed = command.split(" ")
	if(parsed[0] == "examine"):
		print("This room contains: ");
		for x in area.objects:
			print(x.name)