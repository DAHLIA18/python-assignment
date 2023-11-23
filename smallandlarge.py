number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

total = number1 + number2 + number3
average = total / 3
product = number1 * number2 * number3
smallest = min(number1,number2,number3)
largest = max(number1,number2,number3)

print("Sum:",total)
print("Average:",average)
print("Product:",product)
print("Smallest:",smallest)
print("Largest:",largest)