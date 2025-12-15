def future_feature():
    # To be implemented later
    pass

def calculate_tax(income):
    if income < 10000:
        pass  # No tax for low income
    else:
        tax = income * 0.2
        return tax

# This will execute without error
future_feature()
result = calculate_tax(50000)
print(f"Tax for $50,000: ${result if result else 'No tax'}")