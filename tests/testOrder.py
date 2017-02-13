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
			customer = self.suzy
			)


		self.order = Order(
			customer = self.suzy, #foreign-key to customer
			payment = self.payment, #foreign-key to payment
			order_complete = False
			)


	# double check to make sure Suzy is going to the database
	# create a getter that returns Suzy's customer_id in Customer
	# write a method that makes a call to the database and returns the row
	# print the returned data
	# to check what type isInstance types.TypeType
	# when entering values into the database, double quotes "{}" are needed, not single quotes '{}'
	

	# ADD SUZY TO DB
	# def test_customer_to_database(self):
	# 	self.suzy.save(self.suzy)
	
	def test_order_has_customerId(self):
		self.assertEqual(2, self.suzy.get_customer_id(self.suzy))

	def test_order_has_customer(self):
		self.assertEqual("Suzy Bishop", self.order.get_customer_full_name()) #Returns Suzy Bishop
		print("Customer: ", self.order.get_customer_full_name()) 

	def test_order_complete(self):
		self.assertFalse(self.order.get_order_complete())
		print("The order is not complete")

	def test_set_order_to_complete(self):
		self.order.set_order_to_completed()
		self.assertTrue(self.order.get_order_complete()) 
		print("The order is complete", self.order.get_order_complete())

	# def test_create_order(self):
	# 	self.order.create_order()
	# 	self.assertEqual()



if __name__ == "__main__":
	unittest.main()