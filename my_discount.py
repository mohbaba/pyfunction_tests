def my_discount(price , discount):

	discount_price = price * (discount / 100)
	return price - discount_price

print(my_discount(150,15))