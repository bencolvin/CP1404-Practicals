import random
print(random.randint(5, 20))
#This line of code prints a random number between 5 and 20

print(random.randrange(3, 10, 2))
#This line of code prints a random number between 3 and 10 but only picks the second number, this line could not produce a 4, only odd numbers

print(random.uniform(2.5, 5.5))
#This line of code prints a random number between 2.5 and 5.5 and displays the decimal places, the smallest number you could have seen would be 2.5 and the largest 5.5