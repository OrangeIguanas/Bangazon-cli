import unittest
import sys
sys.path.append("../")

from Methods.CreateCustomer import Customer
from Methods.CreateOrder import Order
from Methods.CreatePaymentMethod import PaymentMethod

class TestOrder(unittest.TestCase):
	"""
    Purpose: Test Orders
    Author: Abby
    Tests: 
    	test_order_has_customer
    	test_order_complete
    	test_set_order_to_complete
    """

	@classmethod
	def setUpClass(self):
		self.suzy = Customer(
			first_name = "Suzy", 
			last_name="Bishop", 
			address = "300 Summer's End", 
			city = "New Penzance" , 
			state = "Rhode Island" , 
			postalZip = "02801", 
			phone_number="555-999-4444", 
			email="suzy@bishop.com", 
		)

		self.order = Order(
			customer = self.suzy, #foreign-key to customer
			order_complete = False
			)

		self.payment = PaymentMethod(
			card_number = "123456789",
			card_type = "Visa",
			exp_date = "04/20",
			cvv = "123",
			name_on_card = "Suzy B. Bishop",
			customer = self.suzy
			)

	
	def test_order_has_customer(self):
		self.assertEqual("Suzy Bishop", self.order.get_customer_full_name()) #Returns Suzy Bishop
		print(self.order.get_customer_full_name()) 


	def test_order_complete(self):
		self.assertFalse(self.order.get_order_complete())
		print("The order is not complete")


	def test_set_order_to_complete(self):
		self.order.set_order_to_completed()
		self.assertTrue(self.order.get_order_complete()) 
		print("The order is complete", self.order.get_order_complete())
		

	def test_payment_has_customer(self):
		self.assertEqual("Suzy Bishop", self.payment.get_customer_name()) #Return Suzy Bishop
		print("Payment has Customer", self.payment.get_customer_name()) 


	def test_customer_has_payment_card(self):
		self.assertEqual("Visa", self.payment.get_card_type()) #Return Visa
		print("Customer has Payment", self.payment.get_card_type()) 





if __name__ == "__main__":
	unittest.main()