score = float(input("enter scores: "))
total = 0
count = 0
while score != -1:
      total += score
      count += 1
      score = float(input("enter scores: "))

average = total / count
print("The average score is ", average)