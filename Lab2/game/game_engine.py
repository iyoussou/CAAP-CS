# This is the engine of the game, basically runs everything

class Engine(object):

	# global variables to keep track of game status and live count
	escaped = False
	lives = 3

	# initializes the map in the game
	def __init__(self, scene_map):
		self.scene_map = scene_map

	# takes current scene, plays it, gets the next scene, and updates the game
	# should also return the number of moves the game takes in total
	def play(self):
		current_scene = self.scene_map.opening_scene()
		next_scene_name = ''
		checkpoint = ''
		n_moves = 0
		while (next_scene_name != 'finished' and self.lives > 0):
			print ("\n*******************************************************************") #raise ValueError ('todo')
			next_scene_name = current_scene.enter()
			if (next_scene_name == ':q'):
				exit(1)
			elif (next_scene_name == 'death'):
				checkpoint = current_scene
				n_moves += 1
				current_scene = self.scene_map.next_scene(next_scene_name)
			elif (next_scene_name == 'died'):
				self.lives -= 1
				current_scene = checkpoint
			else:
				checkpoint = current_scene
				current_scene = self.scene_map.next_scene(next_scene_name)
				n_moves += 1
		if (raise ValueError ('todo')):
			self.escaped = True
		return n_moves

	# updates the variable to determine whether player won or failed.
	def won(self):
		return self.escaped
