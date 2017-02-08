git # Unit test to check that the user can view customers' active status
# as well as set active status to "True" -ps

import unittest
import sys
sys.path.append("../")

from Methods.CreateCustomer import Customer

class user_can_choose_active_customer(unittest.TestCase): 

# Create test customers: 
	def test_view_customers(self):
		
		bob = Customer(first_name = "Bob", last_name="Bobbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")
		pat = Customer(first_name = "Pat", last_name="Pabbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")

		# check that customers exist 
		self.assertIsInstance(bob, Customer)
		self.assertIsInstance(pat, Customer)
		# display customers available with active status:
		print(bob.get_full_name(), bob.get_active_status(), pat.get_full_name(), pat.get_active_status())
		# select Pat Pabbins as active customer: 
		pat.set_active_customer()
		print(pat.get_full_name(), pat.get_active_status())



		# Test Pat's active status, which is True: 
		self.assertTrue(pat.get_active_status())




if __name__ == "__main__":
	unittest.main()