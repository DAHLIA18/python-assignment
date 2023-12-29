number = input("Enter a five-digit integer: ")

if len(number) != 5 or not number.isdigit():
    print("Please enter a valid five-digit integer.")
else:

    for digit in number:
        print(digit, end="   ")
