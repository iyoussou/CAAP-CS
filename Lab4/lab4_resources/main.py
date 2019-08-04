# ISMAIL YOUSSOU
# Assignemnt 2
# Due August 4 10:00 PM

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
def screen():
	turtle.screensize(200, 200, bg="#FFFFFF")
	global myPen
	myPen = turtle.Turtle()
	myPen.color("#000000")
	myPen.speed(0)
	global boxSize
	boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle (think unit circle).
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
def goto_origin(myPen):
	myPen.home()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim, color):
	myPen.color("%s" %(color))
	myPen.begin_fill()
	for i in range(4):
		myPen.forward(intDim)
		myPen.left(90)
	myPen.end_fill()  

# This function draws a triangle by drawing each side of the triangle and using the fill function
def triangle(intLength, color):
	myPen.color("%s" %(color))
	myPen.begin_fill()
	for i in range(3):
		myPen.forward(intLength)
		myPen.left(120)
	myPen.end_fill()

# This function draws a circle by using the built-in dot fucntion
def circle(intRadius, color):
	myPen.color("%s" %(color))
	myPen.dot(intRadius, color)

def screen_reset(myPen): # Paints over image with white, "reseting" the screen
	myPen.penup()
	myPen.goto(boxSize/2 - turtle.window_width()/2, turtle.window_height()/2)
	myPen.color("#FFFFFF")
	myPen.pendown()
	myPen.begin_fill()
	for i in range(4):
		myPen.forward(1000)
		myPen.left(-90)
	myPen.end_fill()

def save_image():
	save = myPen.getscreen()
	x = input("What would you like to name this file?\n > ")
	save.getcanvas().postscript(file = "saves/" + x + ".eps")
 
# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves, e.g.:
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings in text files, which you will read from the art folder.
# You have two sample art pieces already saved. The first line will be a list of colors, and the 
# rest of the lines will be rows of pixels, which you should read and save as a list of lists.
# This first list stores the color values, e.g.:
# #FFFFFF,#FFFF00,#000000,#61380B,#F4FA58
# The drawings are stored using a "list of lists" structure where each value within every list
# element is the index of the color in the pallet list for that pixel

# This function will take in a filename path and load the art piece stored in that file.
# You are to parse the art into two lists, one for the color palette (first line of file),
# and a second with the pixel values (list of lists).
# The function returns both lists
def load_art(path):
	art = open(path, 'r')
	art_set = art.read()
	art_set = art_set.split(None, 1)

	colors = art_set[0].split(",")
	art_set = art_set[1].splitlines()

	for i in range(len(art_set)):
		art_set[i] = art_set[i].split(',')
	
	return colors, art_set

# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels, shape):
	myPen.penup()
	myPen.goto(boxSize/2 - turtle.window_width()/2, turtle.window_height()/2 - boxSize/2) # Moves the pen to the top left of the screen
	for j in range(len(pixels)): #Loops through rows
		if j >= 1:
			myPen.penup()
			myPen.setpos(boxSize/2 - turtle.window_width()/2, turtle.window_height()/2 - boxSize/2 -(10*j)) # Moves the pen back to origin, moves the pen to next row
			myPen.pendown()
		for i in range(len(pixels[j])): # Loops through items within row
			color = pallet[int(pixels[j][i])]
			if shape == 'triangle':
				triangle(boxSize, color)
			elif shape == 'circle':
				circle(boxSize, color)
			else:
				box(boxSize, color)
			myPen.forward(boxSize)

# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, ask the if they would like to draw a different piece until they quit the program.
if __name__ == '__main__':
	persist = True
	banana = 'art/banana.txt'
	mario = 'art/mario.txt'
	ghost = 'art/ghost.txt'
	alien = 'art/alien.txt'
	mushroom = 'art/mushroom.txt'
	smile = 'art/smile.txt'
	cool = 'art/cool.txt'
	kitty = 'art/kitty.txt'
	while persist == True:
		x = input("What would you like me to draw?\n1) Banana\n2) Mario\n3) Ghost\n4) Alien\n5) Mushroom\n6) Smile\n7) Cool\n8) Kitty\n > ")
		if int(x) == 1:
			art = banana
		elif int(x) == 2:
			art = mario
		elif int(x) == 3:
			art = ghost
		elif int(x) == 4:
			art = alien
		elif int(x) == 5:
			art = mushroom
		elif int(x) == 6:
			art = smile
		elif int(x) == 7:
			art = cool
		else:
			art = kitty
		shape = input("What would you like the shape of each pixel to be?\n1) Square\n2) Triangle\n3) Circle\n > ")
		if int(shape) == 2:
			shape = 'triangle'
		elif int(shape) == 3:
			shape = 'circle'
		else:
			shape = 'square'

		screen()
		turtle.tracer(0, 0)
		pallet_1, pixels_1 = load_art(art)
		draw(pallet_1, pixels_1, shape)
		turtle.update()
		
		save_art = int(input("Would you like to save this image?\n1) Yes\n2) No\n > "))
		if save_art == 1:
			save_image()

		turtle.Terminator() # Keeps image on screen
		set_persist = input("Would you like me to draw another image?\n1) Yes\n2) No\n > ")
		if int(set_persist) == 1:
			screen_reset(myPen)
		else:
			persist = False
