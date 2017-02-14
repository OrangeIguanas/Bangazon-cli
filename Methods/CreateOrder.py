import sqlite3


class Order():
	"""
	Purpose: Allow a Customer to create an order
	Author: Abby
	Methods: 
		get_customer_full_name,
		get_order_complete, 
		set_order_to_completed
	"""

	def __init__(self, customer, payment, order_complete):
		self.__customer = customer
		self.__payment = payment
		self.__order_complete = False

	def get_customer_full_name(self):
		return self.__customer.get_full_name()

	def get_order_complete(self):
		return self.__order_complete

	def set_order_to_completed(self):
		self.__order_complete = True
		return self.__order_complete


	def create_order(self, customer):
		# customer - is this a class or a tuple?
		# when a product has been added, an order is created
		# select active customer, on customer class - we need to know the id
		# getters for primary key 

		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("SELECT * FROM Order")
				orders = cursor.fetchall()
			   
			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXSISTS `Order`
					(
						order_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
						customer_id INTEGER NOT NULL,
						order_complete BOOLEAN NOT NULL,
						FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`)
					)
				""")

				cursor.execute("""
				INSERT INTO Order VALUES(null, "{}", "{}")
					""".format(
						customer.get_customer_id(), #there needs to be a getter for the FK
						customer.get_payment_id(), #there needs to be a getter for the FK
						customer.get_order_complete()))