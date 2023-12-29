def maximum1(number1, number2, number3, number4, number5):

	if number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
		maximum = number1

	if number2 > number3 and number2 > number4 and number2 > number5 and number2 > number1:
		maximum = number2

	if number3 > number4 and number3 > number5 and number3 > number1 and number3 > number2:
		maximum = number3

	if number4 > number5 and number4 > number3 and number4 > number2 and number4 > number1:
		maximum = number4

	if number5 > number1 and number5 > number2 and number5 > number3 and number5 > number4:
		maximum = number5
	return maximum

print(maximum1(22,9,63,3,56))
print(maximum1(221,2,45,23,4))
	