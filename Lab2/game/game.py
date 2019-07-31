# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	if won == True:
		print("You won!")
		leaderboard.update(score)
	print ("\nGame Over.")
	leaderboard.print_board()
	moves = 0
	name = ""


# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name
		global moves
		print ("Welcome to my game! To quit enter :q at any time. You will have three lives. Good luck!") # raise ValueError ('todo')
		lives = input("\nPlease select a difficulty\n\n1) Hard\n2) Medium\n3) Easy\n > ")
		if int(lives) > 3:
			print("\nOkay, it's clear you meant to select easy. Please read the directions.")
			lives = 3
		name = input("\nLet's play. Enter your name. > ") # raise ValueError ('todo')
		if (name == ':q'):
			exit(1)
		a_map = Map('wake_up') # raise ValueError ('todo')
		a_game = Engine(a_map, lives)
		moves = a_game.play()
		game_over(a_game.won())

play_game()
