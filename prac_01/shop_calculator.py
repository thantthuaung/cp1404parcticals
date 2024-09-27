total_price = 0
item_amount = int(input("Number of items: "))
while item_amount < 0:
    print("Invalid number of items!")
    item_amount = int(input("Number of items: "))
for i in range (item_amount):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    final_price = total_price - (total_price * 0.1)
    print(f"Total price for {item_amount} items is ${final_price:.2f}")
else:
    print(f"Total price for {item_amount} items is ${total_price:.2f}")