#This program receives the input of Fahrenheit and outputs that in Celsuis five times.
def main():

	print("This program receives the input of Fahrenheit and outputs that in Celsuis five times.")
	
	fahrenheit = eval(input("Degrees in Fahrenheit: "))
	celsuis = (fahrenheit - 32)*(5/9)

	for i in range(0,5):
		print(str(fahrenheit) + " degrees fahrenheit is equivalent to " + str(celsuis) + " degrees celsuis.")

main()