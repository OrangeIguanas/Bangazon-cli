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

	def test_can_create_product(self):


		lazer = Product(name = "lazer", price = 13.00, qty = 15, description = "You already know" , category = "Lazer")
		
		self.assertIsInstance(tampon, Product)

		print(tampon.get_price())
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