count = 0
total_sum = 0

while True:
    num = int(input("Enter an integer number (enter 0 to finish): "))
    if num == 0:
        break
    total_sum += num
    count += 1

if count == 0:
    print("No numbers to calculate.")
else:
    average = total_sum / count
    print("Sum of the numbers:", total_sum)
    print("Average of the numbers:", average)