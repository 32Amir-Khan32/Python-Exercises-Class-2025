def outer_function():
    message = "Hello from outer function"
    
    def inner_function():
        nonlocal message
        message = "Modified by inner function"
        print(f"Inner: {message}")
    
    print(f"Before inner: {message}")
    inner_function()
    print(f"After inner: {message}")

outer_function()