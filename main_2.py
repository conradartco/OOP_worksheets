from customer import Customer
from shopping_cart import ShoppingCart
from product import Product

product_one = Product('Soap', '$2.49', 'Health & Body')
product_two = Product('Granola', '$4.98', 'Food')
product_three = Product('Crayons', '$3.00', 'Misc')

customer_one = Customer(input("What is your name? : "))
print(f"Hello ", customer_one.customer_name,"!")

customer_one.add_item(product_one)
customer_one.add_item(product_two)
customer_one.add_item(product_three)
customer_one.view_cart()

total_items = ShoppingCart()
print(total_items.current_total)

empty_cart = ShoppingCart()
empty_cart.empty_cart

print(total_items)