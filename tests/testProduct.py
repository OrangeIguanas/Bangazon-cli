import unittest
import sys
sys.path.append("../")

from Methods.CreateProduct import Product
from Methods.CreateCategory import Category


class ProductTest(unittest.TestCase):

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


	def test_can_register_product_to_database(self):
		self.weapons.save_category(self.weapons)
		self.Bazooka.register_product(self.Bazooka)

	
	def test_can_update_product_qty_when_a_user_adds_to_their_cart(self):
		self.Bazooka.update_product(self.Bazooka, 1)
		
	def test_can_create_product(self):
		self.assertIsInstance(self.Bazooka, Product)
		print(self.Bazooka.get_description())
		print(self.Bazooka.get_category_id())

	def test_product_has_properties(self):

		self.assertIsNotNone(self.Bazooka.get_name())
		self.assertIsNotNone(self.Bazooka.get_price())
		self.assertIsNotNone(self.Bazooka.get_qty())
		self.assertIsNotNone(self.Bazooka.get_description())
		self.assertIsNotNone(self.Bazooka.get_category_id())



if __name__ == '__main__':
	unittest.main()