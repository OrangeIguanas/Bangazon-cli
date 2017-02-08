import unittest
import sys
sys.path.append("../")

from Methods.CreatePaymentMethod import PaymentMethod
from Methods.CreateCustomer import Customer


class TestPaymentMethod(unittest.TestCase):

	def test_can_create_payment_method(self):
		
		
		self.visa_card = PaymentMethod(card_number="4267520023493346", card_type="Visa", exp_date="07/20", cvv="333", name_on_card="Bob Bobbins", client="name")
		
		self.assertIsInstance(self.visa_card, PaymentMethod)


	def test_payment_method_required_properties(self):

		self.bob = Customer(first_name = "Bob", last_name="Bobbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")
		self.visa_card = PaymentMethod(card_number="4267520023493346", card_type="Visa", exp_date="07/20", cvv="333", name_on_card="Bob Bobbins", client=self.bob.get_last_name())
		self.assertIsNotNone(self.visa_card.get_card_number())
		self.assertIsNotNone(self.visa_card.get_name_on_card())
		self.assertIsNotNone(self.visa_card.get_card_type())
		self.assertIsNotNone(self.visa_card.get_exp_date())
		self.assertIsNotNone(self.visa_card.get_cvv())
		self.assertIsNotNone(self.visa_card.get_client())
		print(self.visa_card.get_client())
if __name__ == "__main__":
	unittest.main()
