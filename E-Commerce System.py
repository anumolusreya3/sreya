class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(product.name, "added to cart")

    def show_cart(self):
        total = 0
        for item in self.items:
            print(item.name, "-", item.price)
            total += item.price
        print("Total:", total)
class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
p3 = Product("Headphones", 2000)

user = User("Sreya")

while True:
    print("\n1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("1.", p1.name, p1.price)
        print("2.", p2.name, p2.price)
        print("3.", p3.name, p3.price)

    elif choice == 2:
        item = int(input("Enter product number: "))
        if item == 1:
            user.cart.add_product(p1)
        elif item == 2:
            user.cart.add_product(p2)
        elif item == 3:
            user.cart.add_product(p3)

    elif choice == 3:
        user.cart.show_cart()

    elif choice == 4:
        print("Order placed successfully!")
        break
