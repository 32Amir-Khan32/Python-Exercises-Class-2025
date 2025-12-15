def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numbers = [0, 1, 5, 7, 10]
for num in numbers:
    print(f"Factorial of {num} is {factorial(num)}")