import sqlite3


class ProductOrders():
    
    def __init__(self, product, order):
        self.__product = product
        self.__order = order

    def get_product(self):
        return self.__product

    def get_order(self):
        return self.__order  
