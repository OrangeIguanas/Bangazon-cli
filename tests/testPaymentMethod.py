import unittest 
import sys 
sys.path.append('../') 

from Methods.CreatePaymentMethod import PaymentMethod 
from Methods.CreateCustomer import Customer 


class TestPaymentMethod(unittest.TestCase): 

	"""
	Purpose: Test PaymentMethod
	Author: Zach
	Tests: 
	test_can_create_a_payment_method
	test_can_save_to_database
	test_payment_has_properties
	test_can_get_payment_id


	"""

	@classmethod
	def setUpClass(self):

		self.zach = Customer(
		first_name = "Zachary", 
		last_name="Cline", 
		email = "z@s.com",
		phone_number="555-999-4444",
		city = "Nah Penzance" ,
		state = "Rhode Island" ,
		postalZip = "52801",
		address = "300 Winter's End"
		)

		self.visa = PaymentMethod(
		name_on_card = "Zachary A Cline",
		card_type = "Visa",
		card_number = "2224-333-3344",
		exp_date = "08/20",
		cvv = 111,
		customer= 10)


	def test_can_create_a_payment_method(self):
		# Test is visa a type of PaymentMethod
		self.assertIsInstance(self.visa, PaymentMethod)


	def test_can_save_to_database(self):
		# self.visa.save(self.visa)
		self.assertTrue(PaymentMethod.payment_is_registered(self.visa))
		print(self.visa.get_card_type())

	def test_payment_has_properties(self):
		# Testing if visa Has All Required Field Properties
		self.assertIsNotNone(self.visa.get_name_on_card())
		self.assertIsNotNone(self.visa.get_card_type())
		self.assertIsNotNone(self.visa.get_card_number())
		self.assertIsNotNone(self.visa.get_exp_date())
		self.assertIsNotNone(self.visa.get_cvv())
		self.assertIsNotNone(self.visa.get_customer())

	def test_can_get_payment_id(self):
		self.assertEqual(1, self.visa.get_payment_id(self.visa)) 



# run unittest 
if __name__ == "__main__":
    unittest.main()