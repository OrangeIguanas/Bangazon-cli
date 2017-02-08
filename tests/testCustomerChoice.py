import unittest
import sys
sys.path.append("../")

from Methods.CreateCustomer import Customer



class user_can_choose_active_customer(unittest.TestCase): 

	def test_view_customers(self):
		
		bob = Customer(first_name = "Bob", last_name="Bobbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")
		pat = Customer(first_name = "Pat", last_name="Pabbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")


		self.assertIsInstance(bob, Customer)
		self.assertIsInstance(pat, Customer)
		print(bob.get_full_name(), pat.get_full_name())

		self.assertFalse(bob.get_active_status())
		pat.set_active_customer()
		print(pat.get_active_status())

		self.assertTrue(pat.get_active_status())

		


if __name__ == "__main__":
	unittest.main()