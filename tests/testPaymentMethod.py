import unittest
import sys
sys.path.append("../")

from Methods.CreatePaymentMethod import PaymentMethod
from Methods.CreateCustomer import Customer

"""Tests For Payment Method"""

class TestPaymentMethod(unittest.TestCase):

	"""Test if we can create a payment method"""

	def test_can_create_payment_method(self):
		
		
		self.visa_card = PaymentMethod(card_number="4267520023493346", 
									   card_type="Visa", 
									   exp_date="07/20", 
									   cvv="333", 
									   name_on_card="Bob Bobbins", 
									   customer="name"

									   )
		
		self.assertIsInstance(self.visa_card, PaymentMethod)


	def test_payment_method_required_properties(self):

		"""Test if our payment method has required properties"""

		self.visa_card = PaymentMethod(card_number="4267520023493346", 
									   card_type="Visa", 
									   exp_date="07/20", 
									   cvv="333", 
									   name_on_card="Bob Bobbins", 
									   customer="Joe Mammy"

									   )

		self.assertIsNotNone(self.visa_card.get_card_number())
		self.assertIsNotNone(self.visa_card.get_name_on_card())
		self.assertIsNotNone(self.visa_card.get_card_type())
		self.assertIsNotNone(self.visa_card.get_exp_date())
		self.assertIsNotNone(self.visa_card.get_cvv())
		self.assertIsNotNone(self.visa_card.get_customer())


		
	def test_can_get_value_from_customer_class(self):

		"""Test if our payment method contains a specific value (last name) from the customer class"""

		self.bob = Customer(first_name = "Bob", 
							last_name="Bobbins", 
							address = "111 Front Street", 
							city = "Smyrna" , 
							state = "Tennessee" , 
							postalZip = 37167, 
							phone_number="615-999-1111", 
							email="d@d.com"
							)

		self.visa_card = PaymentMethod(card_number="4267520023493346", 
							   card_type="Visa", 
							   exp_date="07/20", 
							   cvv="333", 
							   name_on_card="Bob Bobbins", 
							   customer=self.bob.get_last_name()
							   )

		print(self.visa_card.get_customer())

	def test_payment_method_is_added_to_database(self):

		self.bob = Customer(first_name = "Bob", 
							last_name="Bobbins", 
							address = "111 Front Street", 
							city = "Smyrna" , 
							state = "Tennessee" , 
							postalZip = 37167, 
							phone_number="615-999-1111", 
							email="d@d.com"
							)		

		self.visa_card = PaymentMethod(card_number="4267520023493346", 
							   card_type="Visa", 
							   exp_date="07/20", 
							   cvv="333", 
							   name_on_card="Bob Bobbins", 
							   customer=self.bob.get_last_name()
							   )
		# self.visa_card.save(self.visa_card)
		self.assertTrue(self.visa_card.payment_is_registered(self.visa_card))			

if __name__ == "__main__":
	unittest.main()
