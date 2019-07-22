# imports random madule form library
from random import randint
from inventory import Inventory

inventory = Inventory()
# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class WakeUp(Scene):

	name = 'wake_up'
	already_taken = False

	def enter(self):
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
				print("\n----------------------------------------------------------------\n You look around the room. \n----------------------------------------------------------------")
			return self.action() # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("\n----------------------------------------------------------------\nYou walk through Door One. \n----------------------------------------------------------------")
			return self.exit_scene('door_one') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("\n----------------------------------------------------------------\nYou walk through Door Two. ")
			return self.exit_scene('door_two') # raise ValueError ('todo')
		elif int(choice) == 4:
			print ("\n----------------------------------------------------------------\n")
			print("Inventory:\n")
			inventory.check_inventory()
			print ("\n----------------------------------------------------------------")
			return self.action() # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome


class DoorOne(Scene):

	name = 'door_one'

	def enter(self):
		if inventory.storage('torch') == True:
			return self.action()
		else:
			print("The door closes behind you. It's pitch black. You feel along the wall looking for a soure of light until you bump into something. It grabs and bites your leg.\n You struggle to free yourself, but since you can't see anything, it's pointless.")
			return self.exit_scene('died')

	def exit_scene(self, outcome):
		return outcome

class DoorTwo(Scene):

	name = 'door_two'