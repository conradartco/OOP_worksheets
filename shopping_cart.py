from product import Product

class ShoppingCart:
    def __init__(self):
        self.cart_inventory = []

    def current_total(self):
        for items in self.cart_inventory:
            item_count = items
            if items == 0:
                print("Your cart is empty!")
        return item_count

    def add_to_cart(self):
        self.cart_inventory.append('')

    def empty_cart(self):
        for items in self.cart_inventory:
            list.clear(items)