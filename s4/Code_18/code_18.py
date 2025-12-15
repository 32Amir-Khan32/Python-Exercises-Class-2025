cart_items = [
    {"name": "Laptop", "price": 1200, "quantity": 1},
    {"name": "Mouse", "price": 25, "quantity": 2},
    {"name": "Keyboard", "price": 80, "quantity": 1},
    {"name": "Monitor", "price": 300, "quantity": 1}
]

print("Shopping Cart:")
print("-" * 40)

total_cost = 0
for item in cart_items:
    item_total = item["price"] * item["quantity"]
    total_cost += item_total
    print(f"{item['name']}: ${item['price']} x {item['quantity']} = ${item_total}")

print("-" * 40)
print(f"Total: ${total_cost}")

# Apply discount if total is high
if total_cost > 1000:
    discount = total_cost * 0.1
    final_cost = total_cost - discount
    print(f"Discount (10%): -${discount}")
    print(f"Final Total: ${final_cost}")
else:
    print(f"Final Total: ${total_cost}")