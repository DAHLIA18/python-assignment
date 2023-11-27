amount = float(input("Enter funds: "))

if amount < 1000000:
   print(amount * 0.1)

elif amount >= 1000000 and amount < 3000000:
     print(amount * 0.15)

elif amount >= 3000000 and amount < 5000000:
     print(amount * 0.2)

elif amount >= 5000000:
     print(amount * 0.25)