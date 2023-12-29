num_scores = 0
passed = 0
failed = 0
scores = int(input("Enter the number of scores: "))
while(scores != -1):
    scores = int(input("Enter score number: "))
    if scores >= 45:
      passed += 1
else:
    failed +=1 
print("Number of students passed:", passed)
print("Number of students failed:", passed)
