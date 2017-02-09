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


		tampon = Product(name = "Tampax Tampon", price = 1.00, qty = 15, description = "You already know" , category = "Hygene")
		
		self.assertIsInstance(tampon, Product)

		print(tampon.get_price())
	'''
	Testing that properties exist on product
	'''

	def test_product_has_properties(self):

		tampon = Product(name = "Tampax Tampon", price = 1.00, qty = 15, description = "You already know" , category = "Hygene")

		self.assertIsNotNone(tampon.get_name())
		self.assertIsNotNone(tampon.get_price())
		self.assertIsNotNone(tampon.get_qty())
		self.assertIsNotNone(tampon.get_description())
		self.assertIsNotNone(tampon.get_category())



if __name__ == '__main__':
	unittest.main()