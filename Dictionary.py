def isValidCommand(command):
	command = command.lower()
	parsed = command.split(" ")
	if(parsed[0] == "eat"):
		print("tada")