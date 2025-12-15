def get_valid_number():
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Number Validator")
    num = get_valid_number()
    print(f"You entered: {num}")
    print(f"Square of {num} is: {num * num}")

# Uncomment to test interactively
# main()