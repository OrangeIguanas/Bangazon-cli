import unittest
import sys
sys.path.append("../")
from Methods.CreateOrder import Order
from Methods.CreateProduct import Product
from Methods.CreateProductOrders import ProductOrders


class TestProductOrders(unittest.TestCase):

	"""
	Test ProductOrders for access to product or order ids. 
	"""

	def test_productorders_has_product(self):

		wonkavator = ProductOrders(product = '3', order = '5')

		self.assertIsInstance(wonkavator, ProductOrders)
		print(wonkavator.get_product())  # Returns as product

	def test_productorders_has_order(self):

		wonkavator = ProductOrders( product = '3', order = '5')

		self.assertIsInstance(wonkavator, ProductOrders)
		print(wonkavator.get_order())

if __name__ == "__main__":
	unittest.main()
