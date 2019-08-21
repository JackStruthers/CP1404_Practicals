number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price >= 100:
    total_price = total_price - (total_price * 0.1)

print("total price for", str(number_of_items), "items is ${:.2f}".format(total_price))
