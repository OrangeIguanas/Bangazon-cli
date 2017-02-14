import sqlite3

'''
Creating Customer Class that will be tied to active customer
'''

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

	'''
	Getters for retreiving customer information
	'''

	def get_full_name(self):
		return "{} {}".format(self.__first_name, self.__last_name)

	def get_first_name(self):
		return self.__first_name

	def get_last_name(self):
		return self.__last_name

	def get_email(self):
		return self.__email
		
	def get_address(self):
		return self.__address

	def get_city(self):
		return self.__city

	def get_state(self):
		return self.__state

	def get_postal_zip(self):
		return self.__postalZip

	def get_active_status(self):
		return self.__is_active

	def get_phone_number(self):
		return self.__phone_number


# Added method to set an active customer, with which the user can create new orders -ps
	def set_active_customer(self): 
		self.__is_active = True
		return self.__is_active
   
#Method to set an inactive customer for logging out
	def set_logout_customer(self):
		self.__is_active = False
		return self.__is_active


	def save(self, customer):
		"""Method To Create A Table and Add Customer Information to The Rows"""
		
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("SELECT * FROM Customers")
				customers = cursor.fetchall()
			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `Customers`
					(
						customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						first_name TEXT NOT NULL,
						last_name TEXT NOT NULL,
						email TEXT NOT NULL,
						phone_number TEXT NOT NULL,
						city TEXT NOT NULL,
						state TEXT NOT NULL,
						postal_zip INTEGER NOT NULL,
						address TEXT NOT NULL,
						is_active BOOLEAN NOT NULL,
						CONSTRAINT name_unique UNIQUE (first_name, last_name, email, phone_number, city, state, postal_zip, address)
					)
				""")

			cursor.execute("""
			INSERT INTO Customers VALUES (null, "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")
			""".format(
						customer.get_first_name(), 
						customer.get_last_name(), 
						customer.get_email(), 
						customer.get_phone_number(),
						customer.get_city(),
						customer.get_state(),
						customer.get_postal_zip(),
						customer.get_address(),
						customer.get_active_status()
						)
					)
		

	def customer_is_registered(customer):
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("""
					SELECT * FROM Customers 
					WHERE first_name="{}"
					AND last_name="{}"
					AND email="{}"
					AND phone_number="{}"
					AND city="{}"
					AND state="{}"
					AND postal_zip="{}"
					AND address="{}"
					AND is_active="{}"
				""".format(customer.get_first_name(), 
							customer.get_last_name(), 
							customer.get_email(), 
							customer.get_phone_number(),
							customer.get_city(),
							customer.get_state(),
							customer.get_postal_zip(),
							customer.get_address(),
							customer.get_active_status()))
			except sqlite3.OperationalError:
				return False

			selected_customer = cursor.fetchall()
			return len(selected_customer) == 1



	def get_customer_id(self, customer):
		"""Method To return the Customer's ID"""

		# connect to the database
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				# select customer_id that matches the customer's phone number
				cursor.execute("SELECT customer_id FROM Customers c WHERE c.phone_number ='{}'".format(customer.get_phone_number()))

				# return the data
				data = cursor.fetchall()
				
				print("Customer_id", data[0][0])
				return data[0][0]
				

			except sqlite3.OperationalError:
				print("NOPE.")

	def get_customers(): 
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("SELECT * FROM Customers")
				data = cursor.fetchall()
				# print("RETURNING CUSTOMER FROM FETCHALL", data)
				# print("RETURNING CUSTOMER FROM FETCHALL", data)
				return data
				

			except sqlite3.OperationalError:
				print("NOPE.")




