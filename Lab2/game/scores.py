class Score(object):
	name = 'player'
	score = 0

	# initializes score and players name
	def __init__(self, name, score):
		self.name = name
		self.score = score

	# returns the name associated with score
	def get_name(self):
		return self.name

	# returns score of player
	def get_score(self):
		return self.score
