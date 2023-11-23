number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2:
	if number1 > number3:
		print(number1,'is the highest')

if number2 > number3:
	if number2 > number1:
		print(number2,'is the highest')

if number3 > number2:
	if number3 > number1:
		print(number3,'is the higest')     

