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


