def my_discount(price, discount):
	discount_amount = price * (discount / 100)
	discount_price = price - discount_amount
	return discount_price
result = my_discount(150, 15)
print(result) 