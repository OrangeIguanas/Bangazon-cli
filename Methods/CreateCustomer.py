import sqlite3

class Customer():

    def __init__(self, first_name, last_name, email, phone_number, city, state, postalZip, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__city = city
        self.__state = state
        self.__postalZip = postalZip
        self.__address = address
        self.__is_active = False

    def get_full_name(self):
        return "{},{}".format(self.__first_name, self.__last_name)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email
        
    def get_address(self):
    	return self.__address

    def get_active_status(self):
    	return self.__is_active

# Added method to set an active customer, with which the user can create new orders -ps
    def set_active_customer(self): 
        self.__is_active = True
        return self.__is_active
   
#Method to set an inactive customer for logging out
    def set_logout_customer(self):
        self.__is_active = False
        return self.__is_active

