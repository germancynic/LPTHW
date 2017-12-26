from sys import exit
import time

def forecourt():
	print """
	You are walking through an opened gate.
	Through the fog you notice the fascade of an an impressive building.
	As you come closer you notice the building is probably a manor house.
		Without further thought you are following the big staircase
		and find yourself knocking on a wooden door."""
	time.sleep(1)
	print """
	Choose between these options:
		1) Bad idea! You run away from that door.
		2) Doesn't matter, I will wait and see what happens."""
	choice = raw_input("> ")
	if choice == "1":
		print "\tTotally scared you run into another wing of the building."
		the_other_wing()
	elif choice == "2":
		print "\tZUMM you hear the door opens, you enter."
		hallway()
	else:
		print "\tYou did nothing, that is the same result as scenario 2."
		print "\tZUMM! You hear the door opens, you are entering manor house."
		hallway()
		
def the_other_wing():
	print """
	There is a staircase you could:
		1) go up or
		2) go down...
		3) or to the left, where stands a Porsche!"""
	choice = raw_input("> ")
	if choice == "1":
		print "\tYou chose to go up."
		time.sleep(2)
		print """
	You ended up in a small apartment where a Polish family is eating Bigos.
	They are offering you a plate. While enjoying this traditional Polish dish,
	you try to understand what they are talking about.
		Kiedy widzisz  tecz. Po deszczuza toba przed toba.
		Wiekszosc ludzi mysli. Czerwony!"""
		end("\r\tPoor thing, you are now married to a Polish wife and you don't even know what happened. Na zdrowie!")
	elif choice == "2":
		print "\tYou chose to go down."
		time.sleep(2)
		basement()
	elif choice == "3":
		print "\tYou don't have the keys so looking at it will be enough for now."
		the_other_wing_postPorsche()
	else:
		print "\tYou haven't chosen either to go up, or down neither the Porsche."
		print "\r\tYou were probably not the smartest kid in class."
		time.sleep(5)
		patiently_waiting()

def the_other_wing_postPorsche():
	print """
	You already know that staircase you could:
		1) go up or
		2) go down."""
	choice = raw_input("> ")
	if choice == "1":
		print "\tYou chose to go up."
		time.sleep(2)
		print """
	You ended up in a small apartment where a Polish family is eating Bigos.
	They are offering you a plate. While enjoying this traditional Polish dish,
	you try to understand what they are talking about.
		Kiedy widzisz  tecz. Po deszczuza toba przed toba.
		Wiekszosc ludzi mysli. Czerwony!"""
		end("\n\tPoor thing, you are now married to a Polish wife and you don't even know what happened. Na zdrowie!")
	elif choice == "2":
		print "\tYou chose to go down."
		time.sleep(2)
		basement()
	else:
		print "\tYou haven't chosen either to go up, or down neither the Porsche."
		print "\r\tYou were probably not the smartest kid in class."
		time.sleep(5)
		patiently_waiting()

def basement():
	print """
	You are following the stairs down. But was is that?
	In an ancient basement a bunch of teenagers do party.
		Sick trap beats are hammering. Beer and pizza for free!
		Well that's your jam! You stay and juck, juck, juck."""
	time.sleep(3)
	print """
	What are you going to do now?
		1) Continue partying or 
		2) drive Porsche and drink on!
		3) I can't stand that Moon Clouds anymore. Irish exit!"""
	choice = raw_input("> ")
	if choice == "1":
		tracklist = ['Mans_not_hot', 'LSD', 'GucciGang', 'Codeine_Dreaming']
		for song in tracklist:
			print "\n\t%s is fire." % song
		end("\tNowadays every song seems to be fire. Your head is hammering like ka, ka, ka.")
	elif choice == "2":
		print "\tThat ride was crazy..."
		time.sleep(2)
		print "\tHow did I manage to turn this thing on?"
		print "\tWhatever... dreams are never die."
		the_other_wing_postPorsche()
	elif choice == "3":
		print """
	You enter another wing. This manor house is huge!
		A guy with violett trackpants and red shoes is playing computer games.
		After looking at you he screams:
		"I am Platin League" and stares at his screen again."""
		time.sleep(5)
		print "\n\tThis dude is weird. You leave ignoring all places you've already seen."
		piano_room()
	else:
		print "\tYou did nothing that is why those teenagers kicked you in a pond. In December!"
		end("\tYou are wet and cold. Better go home.")	
	
def hallway():
	print """
	You enter a Baroque alike giant hallway.
	You noticing there is hell alot of clothes and shoes in that room.
	Who is living here? How can anyone wear 20 pairs of New Balance shoes?
	A geography teacher? Anyways there are two possible ways to go:
		1) One door to the left
		2) and one to the right.
		Which one do you choose?"""
	choice = raw_input("> ")
	
	if choice == "1":
		print "\r\tYou decide to turn left."
		time.sleep(1)
		piano_room()
	elif choice == "2":
		print "\r\tYou decide to turn right."
		time.sleep(1)
		living_room()
	else:
		print "\r\tYou haven't chosen either left nor right. So all you do is standing waiting."
		time.sleep(5)
		patiently_waiting()

def piano_room():
	print """
	You enter a room with really high ceilings where stands a piano.
		But what is that? You hear something growling.
		Oh no! It's a black dog starring at you from a white-red-striped sofa."""
	time.sleep(1)
	print "But hey this dog is wearing a electro shock bracelet. Maybe you could use that."
	print """
	You have various possibilities.
		1) You could shock that dog,
		2) try to guess his name right
		3) or just run to the next door.
		You could also try some crazy stuff.
	Life is short and dogs are fast."""
	carlos_runs = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "Carlos!" or choice == "Carlos" or choice == "carlos":
			print "The dog recognizes its name and let you pass tail wagging."
			kitchen()
		elif choice == "1" or choice == "Shock" or choice == "shock" and not carlos_runs:
			print "\n\tIn the run the dog is whining and jumps back on th sofa"
			carlos_runs = True
			kitchen()
		elif choice == "1" or choice == "Shock" or choice == "shock" and carlos_runs:
			carlos_runs = False
			end("\r\tThis is sadistic. The dog hasn't even moved.")
		elif choice == "Run" and carlos_runs:
			print "You should not try to outrun a doggo."
			end("\r\tYou've been bitten in your backside. Ouch!")
		elif choice == "crazy stuff":
			print "You somehow opened a wormhole. I get the feeling you should have chosen that angry dog."
			time.sleep(2)
			print "\r\tYeah you should have. On the planet you've arrived Rick enslaved an alien species. Those starving creatures eat your brain right now."
			end("\r\tAt least Morty dug a grave. That's a sweet gesture, but does not change the fact that aliens digest your brain.")
		else:
			print "\r\tYou messed up with the possible commands. Please try again any read more carefully."
			piano_room()

def living_room():
	print """
	This is the living room.
	An elderly gentleman nipping from a glass
	of wine seemingly happy about your appearance."""
	time.sleep(2)
	print "\r\tDo you like the Bundesliga?"
	choice = raw_input("> ")
	if choice == "yes" or choice == "Yes" or choice == "y":
		print "\r\tElderly man: Great! That's Italy versus Germany. Come watch with me."
		time.sleep(3)
		print """
	Unfortunately it is the World Cup.
		After 2 weeks of permanent football games...
		you try to kill yourself with a wine corkscrew."""
		end("\tYou poor thing ended in a lunatic asylum.")
	elif choice == "No" or choice == "no" or choice == "n":
		print "\r\tAh you must be one of that young rap music people."
		print "\tYoung G's party is in the basement"
		basement()
	else:
		patiently_waiting()
		
def kitchen():
	print """
	You enter the kitchen. A peculiar dressed woman is baking a cake.
	Meanwhile she is telephoning while she listens to an audio book.
	You notice the door in the garden is open what do you do?
		1) Talk to the woman.
		2) Leave manor house."""
	choice = raw_input("> ")
	if choice == "1":
		print """
	As a stranger you should not surprise anyone in their kitchen.
		The woman is shouting for the dog besides his name is 'Carlos'."""
		end("\r\tYou've been bitten in your backside. Ouch!")
	elif choice == "2":
		print """
	You have left that house without injuries, have not damaged anything or gone mad.
	Besides you nor married, drink and drive, neither got in touch with the police.
		So much possibilities but you made it. You must be very smart or very lucky."""
		end("\r\t Well done!")
	else:
		patiently_waiting()
		
def patiently_waiting():
	print "Patiently waiting until forever?"
	time.sleep(5)
	print "\r\tNo, your weird appearance is noticed."
	print "\tA security guard wants to know the emergency word."
	emergency_word = raw_input("> ")
	if emergency_word == "Tennis" or "tennis":
		print "\n\tSecurity guard: You must be a guest of the house. Excuse me!"
		hallway()
	else:
		print "\r\tI will accompany you to the next police station."
		end("\tYou were busted for trespassing. Poor thing.")
		
def end(why):
	print why,
	print """
		Your adventure in manor house is over.
		Type python ex36.py to start the next one!"""
	exit(0)
	
forecourt()