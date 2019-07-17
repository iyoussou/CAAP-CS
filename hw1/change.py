# User inputs amount of change and specifies how many of which they want back, function optimizes output
def main():
	
	change = eval(input("Insert the amount of change to be split: "))

	# Initializes variables; converts change into an integer.
	
	change *= 100
	initial_change = change
	quarters = 0
	dimes = 0
	nickels = 0
	pennies = 0
	
	# Distributes and optimizes change given the inputted maximum.

	max_quarters = eval(input("What is the most amount of quarters you want back: "))
	if change >= 25 and max_quarters > 0:
		while change >= 25 and max_quarters > 0:
			change -= 25
			quarters += 1
			max_quarters -= 1

	max_dimes = eval(input("What is the most amount of dimes you want back: "))
	if change >= 10 and max_dimes > 0:		
		while change >= 10:
			change -= 10
			dimes += 1
			max_dimes -= 1

	max_nickels = eval(input("What is the most amount of nickels you want back: "))
	if change >= 5 and max_nickels > 0:
		while change >= 5 and max_nickels > 0:
			change -= 5
			nickels += 1
			max_nickels -= 1

	max_pennies = eval(input("What is the most amount of pennies you want back: "))
	if change >= 1 and max_pennies > 0:
		while change >=1 and max_pennies > 0:
			change -= 1
			pennies += 1
			max_pennies -= 1
	
	# Checks if distribution is possible. If so, prints result.
	
	if initial_change > (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1):
		print("Error: Not enough maximum to return change.")
	else:
		print("Your change is " + str(int(quarters)) + " quarters, " + str(int(dimes)) + " dimes, " + str(int(nickels)) + " nickels, and " + str(int(pennies)) + " pennies.")

main()