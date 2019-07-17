#Converts kilograms into pounds
def main():
	
	print("If you think the metric system us un-American, then input your kilograms and I will turn them into freedom units (lbs)!")
	kilograms = eval(input("Enter the weight in kilograms now!: "))
	pounds = kilograms/0.45359237

	print(str(kilograms) + " kilograms is equivalent to " + str(pounds) + " pounds. Enjoy your freedom!")

main()