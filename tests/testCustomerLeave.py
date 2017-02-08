# Test to check if the user can leave bangazon


import unittest 
import sys 
sys.path.append('../')
from Methods.CreateCustomer import Customer 

class test_customer_logout(unittest.TestCase):
#Create test customers for logout:
	def test_customer_logout(self):


		bob = Customer(first_name = "Bob", last_name="Bobbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")
		#stewart = Customer (first_name = "Stewart", last_name = "Stewbins", address = "111 Back Ave.", city = "Green Hills", state = "Tennessee" , postalZip = 37130, phone_number = "112-223-3334", email = "c@d.com" )
		
		bob.set_active_customer()
		self.assertTrue(bob.get_active_status())
		print (bob.get_active_status())

		bob.set_logout_customer()
		self.assertFalse(bob.get_active_status())
		print(bob.get_active_status())


if __name__ == "__main__":
	unittest.main()
		
