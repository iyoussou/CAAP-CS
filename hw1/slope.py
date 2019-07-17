#This program accepts a specified amount of numbers to be summed, the numbers in question, and then sums them.
def main():

	print("This program will sum any series of numbers you desire!")

	loop_duration = eval(input("How many numbers do you plan on adding?: "))

	total = 0
	for i in range(0, loop_duration):
		total += eval(input("What number would you like to add?: "))

	print("Your sum is " + str(total) + ".")

main()