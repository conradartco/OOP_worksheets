from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart_items = ShoppingCart()
        
    def add_item(self, product_input):
        product_input = ShoppingCart()
        product_input.add_to_cart()

    def view_cart(self):
        for items in ShoppingCart():
            print(items)