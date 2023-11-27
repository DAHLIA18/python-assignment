even_number = 0
odd_number = 0

for number in range(1, 101):
    if number % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

print("Number of even numbers:", even_number)
print("Number of odd numbers:", odd_number)