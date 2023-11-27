number = int(input("Enter number of unit:"))
 
lightbill = number - 100

if number > 0 and number <= 100:
   print("No charge")

if number > 100 and number <= 200:
   print(number - 100) * 10

if number > 200:
   print(100 * 10 + (number - 200) * 20)