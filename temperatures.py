
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def calculate_celsius():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


def calculate_fahrenheit():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        calculate_celsius()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        calculate_fahrenheit()
        print("Result: {:.2f} F".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")