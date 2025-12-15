def analyze_numbers(numbers):
    if not numbers:
        return None, None, None, None
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum

def number_analyzer():
    print("Enter numbers separated by spaces")
    try:
        numbers = [float(num) for num in input("Numbers: ").split()]
        
        if numbers:
            total, avg, maximum, minimum = analyze_numbers(numbers)
            
            print(f"\nAnalysis Results:")
            print(f"Numbers: {numbers}")
            print(f"Total: {total}")
            print(f"Average: {avg:.2f}")
            print(f"Maximum: {maximum}")
            print(f"Minimum: {minimum}")
            print(f"Range: {maximum - minimum}")
        else:
            print("No numbers entered.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Uncomment to test interactively
# number_analyzer()