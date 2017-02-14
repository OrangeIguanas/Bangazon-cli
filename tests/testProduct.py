import unittest
import sys
sys.path.append("../")

from Methods.CreateProduct import Product
'''
Tests that verify that product exists in the state that we expect
'''


class ProductTest(unittest.TestCase):
	'''
	Test for creation of product
	'''

	# Test to show Product table is built with required fields -ps 
	def test_can_register_product_to_database(self): 
		george_foreman_grill = Product(name = "George Foreman Grill", price = 2.00, description = "The evolution of home grilling.", qty = 1,  category = "Home Appliance" )
		george_foreman_grill.register_product(george_foreman_grill)

	# Test to demonstrate that adding a duplicate product will update the qty of the 
	# original, rather than add a new row -ps 
	
	def test_can_update_product_qty_when_duplicate(self): 
		george_foreman_grill = Product(name = "George Foreman Grill", price = 2.00, description = "The evolution of home grilling.", qty = 2,  category = "Home Appliance" )
		Product.update_product(self, "George Foreman Grill", 6)


	def test_can_create_product(self):


		lazer = Product(name = "lazer", price = 13.00, qty = 15, description = "You already know" , category = "Lazer" , customer = "")
		
		self.assertIsInstance(lazer, Product)

		print(lazer.get_price())
	'''
	Testing that properties exist on product
	'''

	def test_product_has_properties(self):

		lazer = Product(name = "High Powered Lazer", price = 13.00, qty = 15, description = "You already know" , category = "Lazers")

		self.assertIsNotNone(lazer.get_name())
		self.assertIsNotNone(lazer.get_price())
		self.assertIsNotNone(lazer.get_qty())
		self.assertIsNotNone(lazer.get_description())
		self.assertIsNotNone(lazer.get_category())



if __name__ == '__main__':
	unittest.main()