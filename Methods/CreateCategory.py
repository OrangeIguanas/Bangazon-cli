# This creates a 'category' class to add to our products table, which will allow them to be 
# easily sorted by category 

import sqlite3 

class Category(): 
	def __init__(self, name): 
		self.__name = name 
	
	def get_category_name(self):
		return self.__name