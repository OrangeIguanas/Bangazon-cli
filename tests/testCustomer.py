import unittest
import sys
sys.path.append("../")


from Methods.CreateCustomer import Customer

class TestCreateCustomer(unittest.TestCase):

	def test_can_register_to_database(self):
		"""
		Test that we can Create database and Add users to a dataBase

		"""

		bob = Customer(first_name = "Bob", last_name="Bobbins", email="d@d.com", phone_number="615-999-1111",city = "Smyrna" , state = "Tennessee", postalZip = 37167, address = "111 Front Street")
		Joe = Customer(first_name = "Joe", last_name="Mammy", address = "222 Back", city = "Smyrna", state = "Tennessee", postalZip = 38933, phone_number="625-444-4444", email="joe@mammy.com")

		'''
		To test, use the "save" method to add to DB. You will need to Delete the function due to the Unique constraint before you assert true below. 
		'''

		self.assertTrue(Customer.customer_is_registered(bob))

	def test_can_create_account(self):
		self.bob = Customer(first_name = "Bob", last_name="Bobbins", email="d@d.com", phone_number="615-999-1111",city = "Smyrna" , state = "Tennessee" , postalZip = 37167, address = "111 Front Street")
		print(self.bob.get_full_name())
		
		self.assertIsInstance(self.bob, Customer)

		'''
		Test that Clients full name gets returned correctly
		'''
	def test_customer_has_properties(self):

		self.bob = Customer(first_name = "Bob", last_name="Bobbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")

		print(self.bob.get_full_name())

		self.assertIn("Bob Bobbins", self.bob.get_full_name())
		self.assertIsNotNone(self.bob.get_first_name())
		self.assertIsNotNone(self.bob.get_last_name())
		self.assertIsNotNone(self.bob.get_address())
		self.assertIsNotNone(self.bob.get_city())
		self.assertIsNotNone(self.bob.get_state())
		self.assertIsNotNone(self.bob.get_postal_zip())
		self.assertIsNotNone(self.bob.get_phone_number())
		self.assertIsNotNone(self.bob.get_email())

		'''
		Test that customer is not active upon creation.
		'''

	def test_user_is_not_active(self):

		self.bob = Customer(first_name = "Bob", last_name="Bobbins", address = "111 Front Street", city = "Smyrna" , state = "Tennessee" , postalZip = 37167, phone_number="615-999-1111", email="d@d.com")

		self.assertFalse(self.bob.get_active_status())
		

if __name__ == "__main__":
	unittest.main()
