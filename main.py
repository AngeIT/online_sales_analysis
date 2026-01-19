from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 20)
p3 = Product("Keyboard", 50, 10)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.show_products()
print("Total inventory value:", manager.total_inventory_value())

from cart import Cart

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.show_cart()
print("Total to pay:", cart.total_cart_value())

