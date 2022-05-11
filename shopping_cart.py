from product import Product

class ShoppingCart:
    def __init__(self):
        self.cart_name = 'Cartie-B'
        self.cart_inventory = []

    def show_items(self):
        for product in self.cart_inventory:
            print(product.product_name)

    def current_total(self):
        items_in_cart = len(self.cart_inventory)
        for amount in items_in_cart:
            if amount == 0:
                print("Your cart is empty!")
            elif amount != 0:
                return amount
        

    def add_to_cart(self, product):
        self.cart_inventory.append(product)

    def empty_cart(self):
        for items in self.cart_inventory:
            list.clear(items)