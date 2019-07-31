# imports random madule form library
from random import randint
from inventory import Inventory

inventory = Inventory()
# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):
	print("Initializing...")
	
class WakeUp(Scene):

	name = 'wake_up'
	already_taken = False

	def enter(self):
		if self.already_taken == True:
			inventory.storage.remove('torch')
			self.already_taken = False
		print ("\n----------------------------------------------------------------\n")
		print("You wake up in a cave. You don't remember the last time you've seen sunlight. In front of you are two doors. To the left, there is a bright light.\n")
		return self.action()


	def action(self):
		print ("What will you do?")
		choice = input("\n 1) Check Room\n 2) Enter Door One\n 3) Enter Door Two\n 4) Check Inventory\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			if self.already_taken == False:
				
				x = input("\n---------------------------------------------------------------- \n You look around the room. Upon further examination, the source of light is revealed to be a torch. \n---------------------------------------------------------------- \n 1) Take the torch\n 2) Walk away\n > ")

				if int(x) == 1:
					inventory.store_item('torch')
					print("\n----------------------------------------------------------------\nYou take the torch.\n----------------------------------------------------------------\n")
					self.already_taken = True
					return self.action()
				else:
					print("\n----------------------------------------------------------------\nYou walk away.\n----------------------------------------------------------------\n")
					return self.action()
			
			else:
				print("\n----------------------------------------------------------------\n You look around the room.\n----------------------------------------------------------------")
			return self.action() # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("\n----------------------------------------------------------------\nYou walk through Door One.\n----------------------------------------------------------------")
			return self.exit_scene('door_one') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("\n----------------------------------------------------------------\nYou walk through Door Two.\n----------------------------------------------------------------")
			return self.exit_scene('door_two') # raise ValueError ('todo')
		elif int(choice) == 4:
			inventory.check_inventory()
			return self.action() # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome


class DoorOne(Scene):

	name = 'door_one'
	already_taken = False

	def enter(self):
		if inventory.return_item('torch') == True:
			print ("\n----------------------------------------------------------------\n")
			print("The door closes behind you. The light from your torch illuminates the room.\n\n'Hissss...'\n\nYou look down and find a giant spider the size of your torso. You can see its hunger reflected by all eight of its beady eyes.")
			return self.action()
		else:
			print("\n----------------------------------------------------------------\n")
			print("The door closes behind you. It's pitch black. You feel along the wall looking for a soure of light until you bump into something. It grabs and bites your leg.\n\nYou struggle to free yourself, but since you can't see anything, it's pointless.")
			return self.exit_scene('death')

	def action(self):
		print("\nWhat will you do?")
		choice = input("\n 1) Check Room\n 2) Step on it\n 3) Pretend to be a spider\n 4) Cry and curl into a fetal position\n 5) Check Inventory\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			if self.already_taken == False:
				print("\n----------------------------------------------------------------")
				print("\nHow nice of the spider to wait while you walk around the room.\n\nThere's a hole in the wall directly behind the spider, but turning your back to it probably isn't the smartest idea.")
				print("\n----------------------------------------------------------------")
				self.already_taken = True
			else:
				print("\n----------------------------------------------------------------")
				print("\nYou look around. Still spidery.")
				print("\n----------------------------------------------------------------")
			return self.action()
		if int(choice) == 2:
			print("\n----------------------------------------------------------------")
			print("\nYou attempt to step on the spider, stomping as hard as you can, but the spider jumps out of the way.")
			print("\n\nBlinded by adredaline, you didn't realize how much force you put into that stomp. The spider can only watch with second-hand embarassment as you lose your balance and slam your head against a wall, killing you instantly.")
			print("\n----------------------------------------------------------------")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print("\n----------------------------------------------------------------\n")
			print("You get on all fours, bend your elbows back, and begin to mimic the spider's body language.\n\nConfused, the spider doesn't know how to respond to you. While it's distracted, you punch it in the eyes and make a break towards the hole in the wall.")
			print("\n----------------------------------------------------------------")
			return self.exit_scene('bridge_door_one')
		elif int(choice) == 4:
			print("\n----------------------------------------------------------------")
			print("\nYou decide the best course of action is to... lay down and cry...\n\nYou cry so much that it'd put a toddler to shame. You curl up on the ground in a puddle of your own tears and press your chest against your knees.")
			print("\n\nThe spider laughs at your complete lack of composure and decision-making skills. The spider pulls out their phone and suddenly your utterly miserable display of ineptitude is all over the Web. Millions are now watching the sad explorer wallow in their own tears and sweat over the sight of an insect.")
			print("\n\nYour self esteem has dropped so low that you don't even care when the spider begins wrapping you in a web, laughing the entire time.")
			print("\n----------------------------------------------------------------")
			return self.exit_scene('death')
		elif int(choice) == 5:
			inventory.check_inventory()
			return self.action()


	def exit_scene(self, outcome):
		return outcome

class BridgeDoorOne(Scene):

	name = 'bridge_door_one'
	already_taken = 0
	
	def enter(self):
		print("***CHECKPOINT REACHED***\n\n")
		print("\n\nYou burst into a spacious room and almost stumble into a massive chasm. After composing yourself, you can see that the only thing connecting you to the other side is a rickety-looking bridge.")
		return self.action()

	def action(self):
		print("\nWhat will you do?")
		choice = input("\n 1) Check Room\n 2) Climb down the cliff\n 3) Walk across the bridge\n 4) Check Inventory\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print("\n----------------------------------------------------------------")
			print("\nYou walk to the edge of the cliff and look down. Even with your torch, all you can see is darkness.\nYou look up and see an equal measure of darkness above. You must be on the side of a cliff.")
			print("\nYou wiggle the post of the wooden bridge. It wiggles right back.")

			x = input("\n\nTo your left, you find a pile of rocks.\n\n1) Take a rock\n2) Walk away\n > ")

			if int(x) == 1:
				inventory.store_item('rock')
				self.already_taken += 1
				print("\n----------------------------------------------------------------")
				
				x = input("\n\nFor literally no reason whatsoever, you decide to take a rock.\n\n1) Take another rock\n2) Walk away\n > ")

				if int(x) == 1:
					inventory.store_item('rock')
					self.already_taken += 1
					print("\n----------------------------------------------------------------")

					x = input("\nUh, okay.\n\nYou decide to take another rock.\n\n1) Take another rock\n2) Walk away\n > ")

					if int(x) == 1:
						inventory.store_item('rock')
						self.already_taken += 1
						print("\n----------------------------------------------------------------")

						x = input("\nYou take another rock and jam it into your pocket. You may be developing an addiction.\n\n1) Take more rocks\n2) Walk away\n > ")

						if int(x) == 1:
							inventory.store_item('rock')
							self.already_taken += 1
							print("\n----------------------------------------------------------------")
							print("\nYou feel an undeniable connection to the ever-decreasing pile of rocks. Every second you spend considering not picking up a rock is agony.\n\nIrregardless of life and limb, you shove as many rocks as you can carry into your pockets, your bag, anywhere that will let you hold just one more rock.")

							x = input("\n\n1) Take more rocks\n2) Walk away\n > ")

							if int(x) == 1:
								print("\n----------------------------------------------------------------")
								print("\nThe seperation is too much to bear. All of the rocks overflowing your bag and under your clothes are only a substitute for the real thing. You yearn to be as intimate to the pile of rocks as possible.\n\nThe real pile.\n\nYou dive headfirst into the pile in a reckless display of passion, cracking your skull.\n\nThe fatal injury matters to you little, for at last, you can be one with the rocks.\n\nForever.")
								for i in range(self.already_taken):
									inventory.storage.remove('rock')
								return self.exit_scene('death')
							else:
								print("\n----------------------------------------------------------------")
								print("You decide enough is enough. It's not the pile's fault, it's yours. With the rocks weighing you down, you can only shuffle away.")
								print("\n----------------------------------------------------------------")
								return self.action()
						else:
							print("\n----------------------------------------------------------------")
							print("With the rocks weighing you down, you can only shuffle away.")
							print("\n----------------------------------------------------------------")
							return self.action()
					else:
						print("\n----------------------------------------------------------------")
						print("You walk away.")
						print("\n----------------------------------------------------------------")
						return self.action()
				else:
					print("\n----------------------------------------------------------------")
					print("You walk away.")
					print("\n----------------------------------------------------------------")
					return self.action()
			else:
				print("\n----------------------------------------------------------------")
				print("You walk away.")
				print("\n----------------------------------------------------------------")
				return self.action()
		elif int(choice) == 2:
			if self.already_taken >= 2:
				print("\n----------------------------------------------------------------")
				print("\nYou walk towards the edge and the ground immediately collapses under you. Hope those rocks were worth it, you're about to land on a much larger one.")
				print("\n----------------------------------------------------------------")
				for i in range(self.already_taken):
					inventory.storage.remove('rock')
				return self.exit_scene('death')
			else:
				print("\n----------------------------------------------------------------")
				print("\nYou walk towards the edge and begin climbing down. However, because gravity exists and you did none of the proper tests before spelunking, you immediately slip on a crumbling rock and fall into oblivion.")
				print("\n----------------------------------------------------------------")
				return self.exit_scene('death')
		elif int(choice) == 3:
			if self.already_taken >= 2:
				print("\n----------------------------------------------------------------")
				print("\nYou do your best to walk across the bridge with all of the rocks you've taken. You make it about halfway before the rope snaps.\n\nIt's a good thing you like rocks! You're about to land on a much, much larger one.")
				print("\n----------------------------------------------------------------")
				for i in range(self.already_taken):
					inventory.storage.remove('rock')
				return self.exit_scene('death')
			else:
				print("\n----------------------------------------------------------------")
				print("\nYou walk across the bridge.\n\nWell that was easy.")
				print("\n----------------------------------------------------------------")
				return self.exit_scene('cyclops_room')
		elif int(choice) == 4:
			inventory.check_inventory()
			return self.action()
	
	def exit_scene(self, outcome):
		return outcome

class CyclopsRoom(Scene):

	name = 'cyclops_room'
	already_taken = 0

	def enter(self):
		print("\n----------------------------------------------------------------")
		print("\nYou walk into the opening in the wall and immediately feel a sense of doom.")
		print("\n\nAs you continue walking, the hallway becomes noticeably wider.\nYou wonder how much further you have to walk.\n\nThe tunnel is about triple its original size.\n\nYou can see an opening.")
		print("\n\nA shiver crawls up your spine.\n\nIn front of you stands a 30-foot tall cyclops armed with a club as large as your body.\n\nYou know he's the only thing standing between you and freedom.")
		return self.action()

	def action(self):
		print("\n\nWhat will you do?")
		if inventory.return_item('rock') == True:
			choice = input("\n1) Check Room\n2) Cry and curl into a fetal position\n3) TORCH: Toss it\n4) ROCK: Toss it at...\n > ")
		elif inventory.return_item('rope') == True:
			choice = input("\n1) Check Room\n2) Cry and curl into a fetal position\n3) TORCH: Toss it\n4) ROPE: Wrap around...\n > ")
		else:
			choice = input("\n1) Check Room\n2) Cry and curl into a fetal position\n3) TORCH: Toss it\n > ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			if self.already_taken >= 1:
				self.already_taken = 0
				print("\n----------------------------------------------------------------")
				print("You look around the room again. The cyclops grows impatient and prepares a kick.\n\nBecause you weren't paying attention, the kick connects and you slam into a wall. It doesn't take long for you to blackout.")
				return self.exit_scene('death')
			else:
				self.already_taken += 1
				print("\n----------------------------------------------------------------")
				print("You look around the room.\n\nThe cyclops appears to be gazing at your torch.\n\nYou should hurry and make a decision...")
				return self.action()
		elif int(choice) == 2:
			print("\n----------------------------------------------------------------")
			print("\nYou begin to bawl and lay down on the ground, clutching your knees.\n\nThe cyclops doesn't hesitate to crush you with his club.\n\n\nWhy... Why did you think that would work?")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print("\n----------------------------------------------------------------")
			print("\nYou toss the torch to the other side of the room and make a break for the exit. The cyclops, following the light, turns his body, including his club, to view the torch.")
			print("\nWith the loss of light obstructing your view, you accidentally run into his club, stopping you in your tracks and flinging you backwards.")
			print("\nThe cyclops, now aware of what you attempted, swiftly clubs you.\n\nYou're too wounded to dodge.\n\n\nPerhaps there is something you're missing...")
			return self.exit_scene('death')
		elif int(choice) == 4 and inventory.return_item('rock') == True:
			choice = input("\n1) Throw the rock at his eye\n2) Throw the rock at the ceiling\n > ")

			if int(choice) == 1:
				print("\n----------------------------------------------------------------")
				print("\nYou throw the rock and hit his eye.\n\nThe cyclops begins to stumble back, swinging his club in the process. His club makes contact with your hand and knocks your torch away. The cyclops falls backwards and lands in front of the exit, blocking your path.")
				print("\nThe force of his collapse violently shakes the ground, and the ceiling begins to crumble. You try to avoid the rubble, but without the torch, its pointless.\n\nYou're buried alive.")
				return self.exit_scene('death')
			else:
				print("\n----------------------------------------------------------------")
				print("\nYou throw the rock and hit the ceiling.\n\nThe ceiling begins to crumble. A giant boulder falls on top of the cyclops, knocking it unconcious.\n\nUsing your torch, you skillfully evade the falling rocks and make it to the exit.\n\nUnfortunately for you, the collapse has spread to the exit tunnel.")
				return self.exit_scene('collapsing_tunnel')
		elif int(choice) == 4 and inventory.return_item('rope') == True:
			choice = input("\n1) Wrap the rope around yourself\n2) Wrap the rope around a stalactite\n3) Wrap the rope around his legs\n > ")

			if int(choice) == 1:
				print("\n----------------------------------------------------------------")
				print("\nYou wrap the rope around yourself, creating makeshift protective armor.\n\nYou understand completely why people don't use ropes to make armor after a swift kick to your stomach shatters your ribs.")
				return self.exit_scene('death')
			if int(choice) == 2:
				print("\n----------------------------------------------------------------")
				print("\nYou plan to lasso a stalactite and simply climb over the cyclops. Genius!\n\nYou create about a fourth of your knot before the cyclops gets impatient and clubs you, killing you instantly.")
				return self.exit_scene('death')
			if int(choice) == 3:
				print("\n----------------------------------------------------------------")
				print("\nYou take the rope and throw it between the cyclops' legs.\n\nThe cyclops swings his club, but you dodge right, taking the rope and running around both of his legs. Lacking depth perception, the cyclops can barely keep up with your speed.\n\nAfter six rotations, you pull on the rope. The cyclops drops to the ground.\n\n\nThe force of the cyclops' fall causes the ceiling to lose it's integrity.\n\nThe ceiling begins to crumble. A giant boulder falls on top of the cyclops, knocking it unconcious.\n\nUsing your torch, you skillfully evade the falling rocks and make it to the exit.\n\nUnfortunately for you, the collapse has spread to the exit tunnel.")
				return self.exit_scene('collapsing_tunnel')

	def exit_scene(self, outcome):
		return outcome

class CollapsingTunnel(Scene):

	def enter(self):
		print("\nYou run as fast as you can, trying to outpace the rapidly-approaching collapse. Ahead of you in the ceiling lies a ladder leading to a source of light. You can make it if you jump.")
		return self.action()

	def action(self):
		print("\nWhat will you do?")
		choice = input("\n1) Check Room\n2) Jump for the ladder\n3) Keep running\n > ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print("\n----------------------------------------------------------------")
			print("\nYou stop to look around the tunnel.\n\nYou are immediately crushed by the weight of several tons of boulder.\n\nProbably not the time to go sightseeing.")
			return self.exit_scene('death')
		if int(choice) == 2:
			print("\n----------------------------------------------------------------")
			print("\nYou jump for the ladder.\n\nIt works!\n\nYou start climbing and smell fresh air. You can taste freedom!\n\nUnfortunately for you, the cave is collapsing. The rocks holding the ladder together separate, and just as you stick your hand out and feel a smooth breeze, you fall and are crushed underneath the rubble.")
			return self.exit_scene('death')
		if int(choice) == 3:
			print("\n----------------------------------------------------------------")
			print("\nYou decide to chance it and keep running, speeding past the ladder.\n\nThe exit is in view, but the falling rubble isn't far behind.\n\n\nWith one final leap, you fly out of the tunnel, right in the nick of time.")
			return self.exit_scene('finished')

	def exit_scene(self, outcome):
		return outcome


class DoorTwo(Scene):

	name = 'door_two'

	def enter(self):
		if inventory.return_item('torch') == True:
			print("\n----------------------------------------------------------------\n")
			print("The door closes behind you. The light from your torch illuminates the room.")
			print("\n\nImmediately your attention is drawn to the several holes scattered around the room. They appear to be dart traps. You don't know where the triggers are.\n\nIt's a good thing you stopped moving.")
			return self.action()
		else:
			print("\n----------------------------------------------------------------\n")
			print("The door closes behind you. It's pitch black. You feel along the wall looking for a soure of light until you step on a button.")
			print("\n\n*click*")
			print("\n\nSomething shoots a dart in your throat. You immediately collapse.")
			return self.exit_scene('death')

	def action(self):
		print("\nWhat will you do?")
		choice =  input("\n1) Check Room\n2) Catch the darts\n3) Make a break for it\n4) Check Inventory\n > ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print("\n----------------------------------------------------------------")
			print("\nYou start walking around the room to check for any items.\n\n*click*\n\nAs you slip into unconciousness you think, 'so THAT'S why I stopped moving...'")
			return self.exit_scene('death')
		if int(choice) == 2:
			print("\n----------------------------------------------------------------")
			print("\nFinally, you can put those hours spent watching ninja videos to good use.\n\nYou begin walking forward.\n\n*click*\n\nYou catch the first dart effortlessly. You continue walking, the darts continue flying, and you continue catching.\n\nTen in each hand, five in your elbows and armits, and two behind one of your knees.\n\nYou're at your limit; one more dart and your dead.\n\nYou begin creeping towards the door until you hear that dreaded noise.\n\n*click*\n\nFortunately for you, the machines are out of ammo. You continue onwards.")
			return self.exit_scene('cliff')
		elif int(choice) == 3:
			print("\n----------------------------------------------------------------")
			print("\nYou begin sprinting through the room. You immediately reget it.\n\nYou look cute as a porcupine...")
			return self.exit_scene('death')
		elif int(choice) == 4:
			print("\n----------------------------------------------------------------")
			print("\nYou reach into your inventory, readjusting to do so.\n\n*click*\n\nAs you slip into unconciousness you think, 'so THAT'S why I stopped moving...'")
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		return outcome

class Cliff(Scene):

	name = 'cliff'
	already_taken = False

	def enter(self):
		print("\n\nAfter a suprisingly large amount of stairs, you reach a massive gorge. On the other side, you can see some kind of exit. There are pointed stalactites hanging from the ceiling.")
		return self.action()

	def action(self):
		print("\nWhat will you do?")
		if inventory.return_item('rope') == True:
			choice = input("\n1) Check Room\n2) Run and jump\n3) Climb down\n4) Check Inventory\n5) ROPE: Grapple a stalactite and swing across\n > ")
		else:
			choice = input("\n1) Check Room\n2) Run and jump\n3) Climb down\n4) Check Inventory\n > ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print("\n----------------------------------------------------------------")
			
			if self.already_taken == False:
				print("\nAfter looking around the cliff ledge, you find hidden behind a boulder a long strand of rope. You test it's strength and it's pretty durable.")

				x = input("\n1) Take the rope\n2) Walk away\n > ")

				if int(x) == 1:
					inventory.store_item('rope')
					print("\n----------------------------------------------------------------\nYou take the rope.\n----------------------------------------------------------------\n")
					self.already_taken = True
					return self.action()
				else:
					print("\n----------------------------------------------------------------\nYou walk away\n----------------------------------------------------------------\n")
					return self.action()
			else:
				print("\nYou look around the cliff ledge. No more property to steal.")
				return self.action()
		elif int(choice) == 2:
			print("\nYou take a running start and attempt to jump the gap, nevermind that the gorge is about the length of 30 of you stacked vertically.\n\nAs soon as you jump, your head makes contact with a stalactite and knocks you unconcious.\n\n\nYour body imitates a pinwheel as you hilariously spin to your doom.")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print("\n----------------------------------------------------------------")
			print("\nYou walk towards the edge and begin climbing down. However, because gravity exists and you did none of the proper tests before spelunking, you immediately slip on a crumbling rock and fall into oblivion.")
			print("\n----------------------------------------------------------------")
			return self.exit_scene('death')
		elif int(choice) == 4:
			inventory.check_inventory()
			return self.action()
		elif int(choice) == 5:
			print("\nYou determine that the rope is sturdy enough to get you across.\n\nAfter making what you think a lasso looks like, you wind it up and toss it to the stalactite closest to the center.\n\nSuccess!\n\nYou frimly grasp the rope, take a running start, and jump.\n\nAlmost immediately after you place your weight on the rope, the knot becomes undone.")
			return self.exit_scene('bridge_door_two')

	def exit_scene(self, outcome):
		return outcome

class BridgeDoorTwo(Scene):
	
	name = 'bridge_door_two'

	def enter(self):
		print("***CHECKPOINT REACHED***\n\n")
		print("\nYou fall for a while, but you eventually land on a wooden bridge. Looks like the momentum from the rope carried you to safety. The rope falls safely onto your lap.\n\nYou look around. On one side of the bridge there is a web-covered hole. On the opposite side there is an ominous opening in the wall.")
		return self.action()

	def action(self):
		print("\nWhat will you do?")
		choice = input("\n1) Walk to the web-covered hole\n2) Walk to the ominous opening in the wall\n > ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print("\n----------------------------------------------------------------")
			print("\nYou decide to cross the bridge and walk to the web-covered hole.\n\nYou make it about five feet inside the hole before you get stuck.\n\nIn your struggle to free yourself, you drop your torch on the web.\n\nAt least the spiders can enjoy a barbeque.")
			return self.exit_scene('death')
		if int(choice) == 2:
			return self.exit_scene('cyclops_room')

	def exit_scene(self, outcome):
		return outcome

