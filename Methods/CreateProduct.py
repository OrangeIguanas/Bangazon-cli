import sqlite3
'''
Initilizing Product class
'''
class Product():

	def __init__(self, name, price, qty, description, category):
		self.__name = name
		self.__price = price
		self.__qty = qty
		self.__description = description
		self.__category = category


	'''
	Getters for returning values from the product
	'''
	
	def get_name(self):
		return self.__name

	def get_price(self):
		return self.__price

	def get_qty(self):
		return self.__qty

	def get_description(self):
		return self.__description

	def get_category(self):
		return self.__category
