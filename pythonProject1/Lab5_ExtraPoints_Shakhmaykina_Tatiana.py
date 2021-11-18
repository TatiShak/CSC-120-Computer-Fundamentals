def display_title():
	print("Feet and Meters Converter")
	print()


def display_menu():
	print("Conversions Menu:")
	print("a. Feet to Meters")
	print("b. Meters to Feet")

def to_meters(feet):
	meters = feet * 0.3048
	return meters

def to_feet(meters):
	feet = meters / 0.3048
	return feet

display_title()

repeat = "first run"
while repeat.upper() != "N":
	display_menu()

	choice = input("Select a conversion (a/b): ")
	if choice.lower() == "a":
		feet = float(input("Enter feet: "))
		meters = to_meters(feet)
		print(round(meters, 2), "meters")
	elif choice.lower() == "b":
		meters = float(input("Enter meters: "))
		feet = to_feet(meters)
		print(round(feet, 2), "feet")
	else:
		print("Invalid Entry")

	repeat = input("Would you like to perform another conversion? (y/n) ")

print("Thanks, bye!")
