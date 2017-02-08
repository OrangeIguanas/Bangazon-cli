import unittest
from CreateCustomer import *

class TestCreateCustomer(unittest.TestCase):

    def test_can_create_account(self):
    	bob = Customer(first_name = "Bob", last_name="Bobbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")
    	
    	print(bob.get_address())
        self.assertIsInstance(bob, Customer)
        self.assertIn("Bob Bobbins", bob.get_full_name())
        

if __name__ == "__main__":
    unittest.main()
