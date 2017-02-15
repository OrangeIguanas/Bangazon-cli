import sqlite3


class ProductOrders():
	
	def __init__(self, product, order):
		self.__product = product
		self.__order = order

	def get_product(self):
		return self.__product

	def get_order(self):
		return self.__order  

	def save_productorders(self, productorders, order, product, customer):

		
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("SELECT * FROM ProductOrders")
				productorders = cursor.fetchall()
			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `ProductOrders`
					(
						productorders_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						product_id INTEGER NOT NULL,
						order_id INTEGER NOT NULL,
						FOREIGN KEY(product_id) REFERENCES `Products`(product_id),
						FOREIGN KEY (order_id) REFERENCES `CustomerOrder` (customer_order_id)                        )
					""")

			cursor.execute("""
			INSERT INTO ProductOrders VALUES (null, "{}", "{}")
			""".format(
					order.get_order_id(order, customer),
					product.get_product(product_id)
				)
			)

	def productorders_are_registered(self, productorders):
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("""
					SELECT * FROM ProductOrders
					WHERE product_id = {}
					AND order_id = {}

					""".format(productorders.get_productorders(1),
						productorders.get_product(),
						productorders.get_order()
					)
				)

			except	sqlite3.OperationalError:
				return False

	def get_productorders(self, productorders):

		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("SELECT product_id, order_id FROM ProductOrders ")
				productorders = cursor.fetchall()
				print("Product and Order number", productorders)
				return productorders

			except sqlite3.OperationalError:
				print("Operational Error")
