guess = 0
import random
number = int(input("Enter a guess number: "))
number = random.randint(1, 10)
while guess != number:
	if guess < number:
        	print("Too low. Try again.")
	elif guess > number:
        	print("Too high. Try again.")
	if guess == number:
        	print("That's correct! Well done.")
	guess = guess + 1