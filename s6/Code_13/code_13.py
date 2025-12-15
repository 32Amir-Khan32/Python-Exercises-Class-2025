class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"{self.name} (${self.price}) - {self.category}"
    
    def apply_discount(self, percentage):
        discount_amount = self.price * percentage / 100
        self.price -= discount_amount
        return self.price

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, product, quantity=1):
        cart_item = self.CartItem(product, quantity)
        self.items.append(cart_item)
        self.total += product.price * quantity
        print(f"Added {quantity}x {product.name} to cart")
    
    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.total -= item.subtotal()
                self.items.remove(item)
                print(f"Removed {product_name} from cart")
                return
        print(f"Product '{product_name}' not found in cart")
    
    def calculate_total(self):
        return sum(item.subtotal() for item in self.items)
    
    def apply_coupon(self, coupon_code):
        if coupon_code == "SAVE10":
            discount = self.total * 0.1
            self.total -= discount
            print(f"Applied 10% discount: -${discount:.2f}")
        elif coupon_code == "SAVE20":
            discount = self.total * 0.2
            self.total -= discount
            print(f"Applied 20% discount: -${discount:.2f}")
        else:
            print("Invalid coupon code")
    
    def checkout(self):
        if not self.items:
            print("Cart is empty!")
            return
        
        print("\n=== CHECKOUT ===")
        print("Items in cart:")
        for item in self.items:
            print(f"  {item}")
        
        print(f"\nSubtotal: ${self.calculate_total():.2f}")
        print(f"Total: ${self.total:.2f}")
        print("Thank you for your purchase!")
        self.clear_cart()
    
    def clear_cart(self):
        self.items = []
        self.total = 0
    
    def display_cart(self):
        if not self.items:
            print("Your cart is empty")
            return
        
        print("\n=== SHOPPING CART ===")
        for item in self.items:
            print(f"  {item}")
        print(f"\nTotal: ${self.total:.2f}")
    
    class CartItem:
        def __init__(self, product, quantity):
            self.product = product
            self.quantity = quantity
        
        def subtotal(self):
            return self.product.price * self.quantity
        
        def __str__(self):
            return f"{self.quantity}x {self.product.name} @ ${self.product.price:.2f} = ${self.subtotal():.2f}"

# Create products
laptop = Product("P001", "Laptop", 1200, "Electronics")
phone = Product("P002", "Smartphone", 800, "Electronics")
book = Product("P003", "Python Book", 50, "Books")
headphones = Product("P004", "Headphones", 100, "Electronics")

# Create shopping cart
cart = ShoppingCart()

# Add items to cart
cart.add_item(laptop)
cart.add_item(phone, 2)
cart.add_item(book, 3)

# Display cart
cart.display_cart()

# Apply coupon
cart.apply_coupon("SAVE10")

# Remove an item
cart.remove_item("Python Book")

# Display updated cart
cart.display_cart()

# Checkout
cart.checkout()