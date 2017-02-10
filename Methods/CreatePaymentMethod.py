import sqlite3


class PaymentMethod():


	"""Create A Payment Method the listed properties"""

	def __init__(self, card_number, card_type, exp_date, cvv, name_on_card, customer):
		self.__name_on_card = name_on_card
		self.__card_type = card_type
		self.__card_number = card_number
		self.__exp_date = exp_date
		self.__cvv = cvv
		self.__customer= customer

	def get_name_on_card(self):

		"""return the name on the payment method"""

		return self.__name_on_card

	def get_card_type(self):

		"""return the type(visa, mastercard, amex) of credit card on the payment method"""

		return self.__card_type

	def get_card_number(self):

		"""return the card number on the payment method"""

		return self.__card_number

	def get_exp_date(self):

		"""return the expiration date on the payment method"""

		return self.__exp_date

	def get_cvv(self):
		
		"""return the cvv number on the back of the card on the payment method"""

		return self.__cvv

	def get_customer(self):

		'''return the client using the payment method'''

		return self.__customer


	def get_customer_name(self):
		return self.__customer.get_full_name()

	'''
	Creates database table with payment method properties
	'''

	def save(self, payment):
	
		
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try: 
				cursor.execute("SELECT * FROM PaymentMethods")
				payments = cursor.fetchall()
			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `PaymentMethods`
					(
						payment_method_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						name_on_card TEXT NOT NULL,
						card_type TEXT NOT NULL,
						card_number TEXT NOT NULL,
						exp_date TEXT NOT NULL,
						cvv TEXT NOT NULL,
						customer_fk INTEGER NOT NULL,
						FOREIGN KEY(customer_fk) REFERENCES `Customers`(customer_id),
						CONSTRAINT name_unique UNIQUE (name_on_card, card_type, card_number, exp_date, cvv)
						)
					""")

			cursor.execute("""
			INSERT INTO PaymentMethods VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}')
			""".format(
						payment.get_name_on_card(), 
						payment.get_card_type(), 
						payment.get_card_number(), 
						payment.get_exp_date(),
						payment.get_cvv(),
						payment.get_customer(),
						)
					)
		
	'''
	Check if information is stored in database
	'''
	
	def payment_is_registered(self, payment):
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("""
					SELECT * FROM PaymentMethods 
					WHERE name_on_card="{}"
					AND card_type="{}"
					AND card_number="{}"
					AND exp_date="{}"
					AND cvv="{}"
					
				""".format(payment.get_name_on_card(), 
						payment.get_card_type(), 
						payment.get_card_number(), 
						payment.get_exp_date(),
						payment.get_cvv(),
						payment.get_customer()))
			except sqlite3.OperationalError:
				return False

			selected_payment = cursor.fetchall()
			return len(selected_payment) == 1
