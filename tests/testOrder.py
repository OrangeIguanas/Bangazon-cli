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
		test_order_has_customerId
		test_order_has_orderId
		test_order_has_customer
		test_order_complete
		test_set_order_to_complete
	"""

	@classmethod
	def setUpClass(self):
		self.suzy = Customer(
			first_name = "Suzy", 
			last_name="Bishop", 
			email = "s@s.com",
			phone_number="555-999-4444",
			city = "New Penzance" ,
			state = "Rhode Island" ,
			postalZip = "52801",
			address = "300 Summer's End", 
			)

		self.payment = PaymentMethod(
			card_number = "123456789",
			card_type = "Visa",
			exp_date = "04/20",
			cvv = "123",
			name_on_card = "Suzy B. Bishop",
			customer = self.suzy #foreign-key to customer
			)


		self.order = Order(
			customer = self.suzy, #foreign-key to customer
			payment = self.payment, #foreign-key to payment
			order_complete = False
			)
	


	#ADD SUZY TO DB
		#self.suzy.save(self.suzy)

	#ADD NEW ORDER
	# def test_create_order_database(self):
	# 	self.order.create_order(self.order, self.suzy)

	def test_order_has_customerId(self):
		# Test to see if Suzy's customer_id is 1
		self.assertEqual(1, self.suzy.get_customer_id(self.suzy))

	def test_order_has_orderId(self):
		# Test to see if Suzy's order_id is 1
		self.assertEqual(1, self.order.get_order_id(self.order, self.suzy))

	def test_order_has_customer(self):
		# Test to see if get_customer_full_name returns the full name
		self.assertEqual("Suzy Bishop", self.order.get_customer_full_name()) #Returns Suzy Bishop
		print("Customer", self.order.get_customer_full_name()) 

	def test_order_is_not_complete(self):
		# Test to see if the order is complete
		self.assertFalse(self.order.get_order_complete())
		print("Order Not Complete", self.order.get_order_complete())

	def test_set_order_to_complete(self):
		#self.order.order_is_complete(self.order, self.suzy)
		self.assertTrue(self.order.order_is_complete(self.order, self.suzy)) 
		print("Order Complete")

		

if __name__ == "__main__":
	unittest.main()