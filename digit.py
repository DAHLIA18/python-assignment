number = int(input("Enter a five-digit integer: "))

digit5 = number % 10
number //= 10
digit4 = number % 10
number //= 10
digit3 = number % 10
number //= 10
digit2 = number % 10
number //= 10
digit1 = number % 10

print(digit1, digit2, digit3, digit4, digit5)