number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
number4 = int(input("Enter fourth number: "))
number5 = int(input("Enter fifth number: "))


if number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
	print(number1)

if number2 > number3 and number2 > number4 and number2 > number5 and number2 > number1:
	print(number2)

if number3 > number4 and number3 > number5 and number3 > number1 and number3 > number2:
	print(number3)

if number4 > number5 and number4 > number3 and number4 > number2 and number4 > number1:
	print(number4)

if number5 > number1 and number5 > number2 and number5 > number3 and number5 > number4:
	print(number5)