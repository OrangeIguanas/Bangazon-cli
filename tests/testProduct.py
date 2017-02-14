import unittest
import sys
sys.path.append("../")

from Methods.CreateProduct import Product
from Methods.CreateCategory import Category


class ProductTest(unittest.TestCase):
	"""
	Purpose: Test Products
	Author: Peter, Zach
	Tests: 
		test_can_register_product_to_database
		test_can_create_product
		test_can_update_product_qty_when_a_user_adds_to_their_cart
		test_product_has_properties
	"""
	@classmethod
	def setUpClass(self):

		self.weapons =Category(
			category_name = "Weapons")


		self.Bazooka = Product(
			name = "Bazooka",
			price = 100.00,
			description = "Goes Boom",
			qty = 5,
			category_id = self.weapons)

	def test_can_create_product(self):
		#Testing if the bazooka object is a Product
		self.assertIsInstance(self.Bazooka, Product)
		print(self.Bazooka.get_description())
		print(self.Bazooka.get_category_id())

	def test_can_register_product_to_database(self):
		#Testing if the Bazooka object contains the foreign key for the weapons category
		# Bazooka(Product) is reliant upon weapons(Category) so it must be created to the database first
		self.weapons.save_category(self.weapons)
		self.Bazooka.register_product(self.Bazooka)

	
	def test_can_update_product_qty_when_a_user_adds_to_their_cart(self):
		# Test if Bazooka quantity decreases by one each time it is added to a customer cart.
		self.Bazooka.update_product(self.Bazooka, 1)
		

	def test_product_has_properties(self):
		# Testing if Bazooka Has All Required Field Properties
		self.assertIsNotNone(self.Bazooka.get_name())
		self.assertIsNotNone(self.Bazooka.get_price())
		self.assertIsNotNone(self.Bazooka.get_qty())
		self.assertIsNotNone(self.Bazooka.get_description())
		self.assertIsNotNone(self.Bazooka.get_category_id())



if __name__ == '__main__':
	unittest.main()