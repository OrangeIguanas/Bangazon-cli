import unittest
import sys
sys.path.append("../")

from Methods.CreateCustomer import Customer
from Methods.CreateOrder import Order

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


	
	def test_order_has_customer(self):
		self.assertIsInstance(self.order, Order)
		print(self.order.get_customer()) #Returns Customer Name (Suzy)


	def test_order_complete(self):
		self.assertFalse(self.order.get_order_complete())
		print("The order is not complete")


	def test_set_order_to_complete(self):
		self.order.set_order_to_completed()
		self.assertTrue(self.order.get_order_complete()) 
		print("The order is complete", self.order.get_order_complete())
		



if __name__ == "__main__":
	unittest.main()