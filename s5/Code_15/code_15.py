def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate / 100
    final_price = price - discount_amount
    return final_price

original_price = 100
final = calculate_discount(original_price, 20)
print(f"Original Price: ${original_price}")
print(f"Final Price after 20% discount: ${final}")