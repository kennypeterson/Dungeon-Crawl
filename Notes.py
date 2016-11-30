character properties
	name = "user chosen character name"
	class = "multi-prop list"
	moveset = "list of moves; attack (subbed from weapon), defend (subbed from shield), item, magic"
	items = "list of items currently held; max based on weight/size of items?"
	equipped_armor = "currently worn armor; contributes to base_defense, effects agility"
	equipped_weapon = "everything has a value, some negative"
	injury = "subbed to type of injury"
	dominant_hand = "choose your sword hand"
	
	
class properties "defined once, non-global"
	name = "Name of class"
	active_action = "Class specific action; consumes 1 turn"
	passive_action = "Class specific action; always active"
	
	#base stats are based on scale from 1 to 10
	base_attack = "Integer, aka strength, class based damage given"
	base_defense = "Float, aka forititude?, class based percentage of damage recieved"
	base_accuracy = "Integer, aka focus, class based move accuracy"
	base_speed = "Integer, aka agility, class based movement speed"
	base_crit = "Float, aka luck chance of crit for 2x damage"
	
injury properties
	head_cond = "float, bad stuff happens when low, effects below 50 stack"
		<= 100 (Clear headed, no negative effects)
		<= 90  (Lightheaded, small text reminders)
		<= 80  (Light headache stemming from blow to head or exposure to smoke)
		<= 50  (Severe headache, non-treated head wound or prolonged exposure to smoke)
		<= 40  (Visions, harsh accuracy and speed penalties)
		<= 20  (Function Loss, harsh attack and defense penalties)
		<= 10  (High crit chances, almost defenseless)
		<= 0   (Death, pretty self-explanatory)
	right_arm_cond = "float, lower attack if dominant_hand"
	left_arm cond = "float, lower defense if not dominant_hand"
	legs_cond = "float, stumbling possible, lowers agility"
		<= 100 (Sturdy footing, no negative effects)
		<= 60  (Limp, chance for stumble and attack or dodge miss)
		<= 10  (Crawl, harsh speed penalty)
	torso_cond = "float, similar to head_cond with lower consequences"
	body_cond = "multi-prop, overall health, poisons and heals apply"
		poisoned = "slow health loss"
		heavy_breathing = "agility penalty"
		open_wound = "left undressed, area of cond will deteriorate"
		festering_wound = "harder to dress, same effect as open_wound"
		cough = "left unchecked, could lead to diasease?"
		cursed = "effects are unknown and random until a random event is triggered"
		
		
Event Specifics
	crit_events = "qualifiers including how big target is, location, type of weapon, your class, etc"
	item_find = "class qualifiers, torch?"
	lowchance_enemy = "torch, items, passive_action qualifiers"
	
Weapons properties
	old_sword = "starter weapon"
		attack = "int, added to character base_attack"
		durability = "float, will default to 100 when acquired"
		weapon_type = "sword, defines type of attacks available"
			att_swipe = "low damage, high accuracy"
			att_swing = "med damage, med-high accuracy"
			att_lunge = "high damage, med-low accuracy"
			att_parry = "will only work if target is attacking, med damage, med accuracy, damages shield"
			
	old_shield = "starter sheild"
		defense = "int added to character base_defense"
		durability = "float, will decay from hard blows"
		defense_stance = "shield, defines types of blocks available, congifured once"
			def_block = "standard block, negates some damage, crit negates all"
			def_deflect = "lower chance of negating, but deflects some damage back, good low health option"
			def_drop = "chance-taking stance in which you focus on your sword hard, increased attack but you'll feel the blow"
						
current properties "specific to the now conditions"
	torch = "float, percentage of light being cast, decays over time"
	campfire = "bool, could lure enemies"
	light = "float, ambient light"
	wet_floor = "reduces agility, chance to slip(small)"
	fog = "reduces accuracy"
	smoke = "reduces accuracy, heavy_breathing"
	
magic properties "powerful but at a high cost. found in tomes, default 1 is defined by class, used in or out of fights"
	cast_spark = "low-cost, starts fire to dry hay or oil, cauterizes wounds, may take a few tries"
	cast_ember = "low-cost, start fire to a campfire"
	cast_splash = "low-cost, small amount of water, cleans wound or weapon, may take a few tries"
	cast_light = "low-med cost torch alternative"
	cast_detect = "low-med cost, detects magic (use??)"
	cast_key = "med-cost, unlocks locked door"
	cast_heal = "med-cost, NOT A SELF-HEAL, SELF-HEALS ARE NOT CANON, heals a target"
	
List of Acceptable General commands = "could be used at anytime"
	General Commands
		walk, go, forward = "i think this is pretty easy to understand"
		run = "fast but loud, chance to blow out torch"
		jog = "a picked up walk, louder than walking"
		sprint = "make a quick getaway, watch for wet floors"
		wade = "traverse water less than waist-high, slow travels"
		swim = "swim through water, loud + med-slow travels, being wet sucks"
		use, use item = "action for present/equipped items"
		cast, magic = "cast a spell from a tome or from memory (if learned)"
		jump = "enviroment specific, clear a gap, trap, or maybe dodge an attack"
		scream, yell = "small chance for enemy to be intimidated and flee, alerts others to your precense"
			yell/scream what?
		stop, freeze, dont move, stand still = "small chance for enemy to not see you when passing"
		look, look around, examine = "prompt for subject, never consumes turn"
		open bag, open pack = "opens bag and lists items inside"
		equip = "change the item you're holding"
		listen = "uh... i guess you just listen for something"
		peek = "peek around corners, over ledges, or through keyholes"
		search, loot = "search local surroundings or corpse"
		
	
	Combat Commands
		flee = "run command specific to being in a fight"
			run
		block, shield = "used to deflect or negate damage from a telegraphed attack"
			raise, brace, lift
		attack, sword = "action for equipped weapon"
			stab, swipe, swing, lunge
		crawl = "use when knocked down to avoid an attack or when injured, last-ditch effort mainly"
		dodge = "from agility, avoid an attack"	
		stand ground = "small chance for enemy to be intimidated and flee"
		crouch, duck = "dodge similar to jump"
		
Enemy Text Samples
	TBD Final Boss - "towering sumthin-ruther with a blade the length of your body"
		#really only need one set of these since the encounter is scripted
		is_near = "You've got a bad feeling about this..."
		is_examined = "The creature's head nearly scrapes the ceiling of the hall. You wonder how it got in here..."
		is_defeated = "The beasts heavy body falls to the floor with a resonating blow... "
	
	Walking Bones - "very common, skellington with low base stats, slow and weak, ALMOST never crits"
		#variety in descs would be helpful and interesting
		is_near = "You hear rattling echoes against the hard cavern walls..."
		is_examined = "The skeleton's bones rattle rythmically as its' souless eyes wander."
		is_defeated = "The shattered bits of bone collapse to the floor as the spirit's will fades."
	
	Vicious Rat - "common, ROUS, aka rodent of unusual size, makes festering wounds"
	
	Rat King - "mini-boss, group of ROUS with their tails tangled together, makes festering wounds"
	
	Mimic - "very low-chance encounter, a disguised treasure chest"
	
	Shambler - "uncommon, hunched man with no concept of humanity, yells and screams"
	
	Rotting Hound - "uncommon, mangy dog that travels in packs often, howls(yells), makes festering wounds"
	
	Shadow - "30% encounter chance, a dark spirit composed of thick fog, causes cough, heavy breathing"
		#this tricky bugger isn't affected by physical attacks. magic only (maybe magic/enchanted weapons too)
		when attacked physically = "You swing your sword thru the shadow. It hums smuggly."
		is_near = "The air is thick and musty, the walls are dripping with condensation."
		is_examined = "The dark figure floats at eye level with long thin arms stretching out from the veil of fog."
		is_defeated = "The fog disperses slowly as the shadow is cast away."
		