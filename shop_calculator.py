price = 0
PRICE_DISCOUNT_RATE = 0.9
user_items = int(input("How many items: "))
while user_items < 0:
    print("Invalid number of items!")
    user_items = int(input("How many items: "))
for i in range(user_items):
    item_price = float(input("Price of item: "))
    price += item_price
if price >= 100:
    price *= PRICE_DISCOUNT_RATE
print("Total price for {} items is ${:.2f}".format(user_items, price))
