# This creates a 'category' class to add to our products table, which will allow them to be 
# easily sorted by category 

import sqlite3 

class Category(): 
	def __init__(self, category_name): 
		self.__category_name = category_name 
	
	def get_category_name(self):
		return self.__category_name

	def save_category(self, category):
		"""Method To Create A Table and Add Customer Information to The Rows"""
		
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("SELECT * FROM Categories")
				categories = cursor.fetchall()
			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `Categories`
					(
						category_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						category_name TEXT NOT NULL,

						CONSTRAINT name_unique UNIQUE (category_name)
					)
				""")

			cursor.execute("""
			INSERT INTO Categories VALUES (null, '{}')
			""".format(category.get_category_name()))
		

	def category_is_registered(category):
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("""
					SELECT * FROM Categories 
					WHERE category_name='{}'
				""".format(category.get_category_name()))
			except sqlite3.OperationalError:
				return False

			selected_category = cursor.fetchall()
			return len(selected_category) == 1
