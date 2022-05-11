from cgi import print_exception
from unicodedata import name


class Product:
    def __init__(self, product_name, product_price, product_category):
        self.product_price = product_price
        self.product_name = product_name
        self.product_category = product_category