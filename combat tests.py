from random import randint

command = input()

if command == "attack":
	print ()

min_damage = 5
max_damage = 10
attack = randint(min_damage,max_damage)
	
	
def damage_counter():
	def crit(damage):
		crit_hit = 10
		chance = randint(0,crit_hit)
		if chance >= crit_hit:
			return damage * 2
		else:
			return damage	
	total_damage = crit(attack)
	if total_damage > max_damage:
		return (str(total_damage) + " CRIT!")
	else:
		return (total_damage)
	


