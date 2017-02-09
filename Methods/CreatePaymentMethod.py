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

		


