def main():

#This program introduces itself, asks for the user's name, and for their favorite color.
#It then returns a summary of that person's responses.

	print("hello!")

	name = input("What is your name?: ")
	print("Nice to meet you, " + name + "!")

	color = input("What is your favorite color?: ")
	print("That's a pretty color, " + name + "!")

	print("Okay, so your name is " + name + " and your favorite color is " + color.lower() + ". Cool!")

main()