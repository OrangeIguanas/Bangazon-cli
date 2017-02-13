import sqlite3
'''
Initilizing Product class
'''
class Product():

	def __init__(self, name, price, qty, description, category):
		self.__name = name
		self.__price = price
		self.__description = description
		self.__qty = qty
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

# Method to create a products table and rows in the database -ps
	def register_product(self, product): 
		# Link method to the database
		with sqlite3.connect("bangazon_cli.db") as bang: 
			cursor = bang.cursor() 

			try: 
				cursor.execute("SELECT * FROM Products")
				products = cursor.fetchall() 
			except sqlite3.OperationalError: 
				# Build the SQL tables
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `Products`(
					product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL, 
					price INTEGER NOT NULL, 
					description TEXT NOT NULL, 
					qty INTEGER NOT NULL, 
					category_id INTEGER NOT NULL, 
					FOREIGN KEY (`category_id`) REFERENCES `Category`(`category_id`),
					CONSTRAINT name_unique UNIQUE (name)
					
					)
				""")
			cursor.execute(""" 
			INSERT INTO Products VALUES (null, "{}", "{}", "{}", "{}", "{}")
				""".format(
								product.get_name(), 
								product.get_price(), 
								product.get_description(), 
								product.get_qty(), 
								product.get_category()
								)
							)
	# Use update to allow multiples of a single product, with the quantity field 
	# reflecting the update -ps
	def update_product(self, name, qty): 
		with sqlite3.connect("bangazon_cli.db") as bang: 
			cursor = bang.cursor() 
			# Specify the table to update, set the field to change (and tell it to add'1',
			# each time) and give a condition "WHERE" 
			cursor.execute("""
				UPDATE Products
				SET qty = qty + 1
				WHERE name = name
				""")
					
