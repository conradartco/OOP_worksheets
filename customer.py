from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart_items = ShoppingCart()
        
    def add_item(self, product_input):
        self.cart_items.add_to_cart(product_input)

    def view_cart(self):
        self.cart_items.show_items()