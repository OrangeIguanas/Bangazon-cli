import sqlite3


class Order():
    """
    Purpose: Allow a Customer to create an order
    Author: Abby
    Methods: get_customer, get_order_complete, set_order_to_completed
    """

    def __init__(self, customer, order_complete):
        self.__customer = customer
        self.__order_complete = False



    def get_customer_full_name(self):
        return self.__customer.get_full_name()

    def get_order_complete(self):
        return self.__order_complete

    def set_order_to_completed(self):
    	self.__order_complete = True
        return self.__order_complete

