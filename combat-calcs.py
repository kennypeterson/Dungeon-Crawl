Combat Calcs


#Calulated damage given for both character and enemy
def is_attacking(character)
	attack_power = character.base_attack + weapon.attack
	
	#need to work out rng mechanic for crit reg
	if crit_power >= crit
		attack_crit = True
		attack_power_crit = attack_power * 2
		return attack_power_crit
	
	#some kind of system to add defense stance and other stuff factored in
	
	#use this to get a random int
	import random
	#(bottom of range, top of range)
	random.randint(1, 10)
	
	#if attack_crit == True	
		#if defense_stance == drop
			#total_attack = 

		
			
#Calculates damage recieved/negated/reflected for both character and enemy
def is_defending(character)
	enemy.attack_power = recieved_damage
	total_defense = character.base_defense + weapon.defense + armor.defense
	if defense_stance == block
		#reduces damage taken, multiplies attack_power by shield
		received_damage = attack_power - total_defense
		#need something to make sure this doesn't come out negative
		return received_damage
	elif defense_stance == deflect
		#also hurts attacker for small percentage, can crit
		recieved_damage = attack_power * weapon.defense
		return received_damage
	elif defense_stance == drop
		#recieve full damage from enemy attack
		return received_damage
		