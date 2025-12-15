fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Searching for 'cherry':")

for fruit in fruits:
    print(f"Checking: {fruit}")
    if fruit == "cherry":
        print("Found cherry! Stopping search.")
        break