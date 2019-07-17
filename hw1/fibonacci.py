#Prints a specific value of the Fibonacci Sequence.
def main():

	print("This program prints a specific term of the Fibonacci Sequence.")

	term = eval(input("Which term of the Fibonacci Sequence would you like?: "))

	current = 1
	previous = 0
	old_previous = 0

	for i in range(0, term-1):
		old_previous = previous
		previous = current
		current = previous + old_previous


	print("Term " + str(term) + " of the Fibonacci Sequence is " + str(current) + ".")

main()
