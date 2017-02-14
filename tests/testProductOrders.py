import unittest
import sys
sys.path.append("../")
from Methods.CreateCustomer import Customer
from Methods.CreateOrder import Order
from Methods.CreateCategory import Category
from Methods.CreateProduct import Product
from Methods.CreateProductOrders import ProductOrders
from Methods.CreatePaymentMethod import PaymentMethod


class TestProductOrders(unittest.TestCase):


	@classmethod
	def setUpClass(self):

		self.suzy = Customer(

			first_name="Suzy",
			last_name="Bishop",
			email="s@s.com",
			phone_number="555-999-4444",
			city="New Penzance",
			state="Rhode Island",
			postalZip="52801",
			address="300 Summer's End"
		)

		self.payment = PaymentMethod(
			card_number="123456789",
			card_type="Visa",
			exp_date="04/20",
			cvv="123",
			name_on_card="Suzy B. Bishop",
			customer= self.suzy
		)

		self.category_name = Category(
			category_name= "Factories"
		)

		self.product = Product(
			name='wonkavator',
			price =5,
			description='up way and side ways',
			qty = 1,
			category = self.category_name,
			customer = self.suzy
		)

		self.order = Order(
			customer=self.suzy,
			payment=self.payment,
			order_complete = False
		)

		self.productorders = ProductOrders(
			product = self.product,
			order = self.order 
		)

	"""
	Test ProductOrders for access to product or order ids which are FOREIGN KEYS .  
	"""
	"""
	#def test_productorders_has_product(self):

		#wonkavator = ProductOrders(product=3, order=5)
		# check if the product foreign key is an instance of ProductOrders
		# table.
		self.assertIsInstance(wonkavator, ProductOrders)
		print(wonkavator.get_product())  # Returns as product

	def test_productorders_has_order(self):

		wonkavator = ProductOrders(product=3, order=5)
		# check if the product foreign key is an instance of ProductOrders
		# table
		self.assertIsInstance(wonkavator, ProductOrders)
		print(wonkavator.get_order())

	def test_save_productorders_to_db(self):
		wonkavator = ProductOrders(product=3, order=5)
		self.assertTrue(wonkavator)
		print("working")

	def test_get_productorders(self):

		wonkavator = ProductOrders(product=3, order=5)
		self.assertTrue(wonkavator.get_productorders(wonkavator))
	
	"""

	def test_save_all_to_db(self):
		self.suzy.save(self.suzy),
		self.payment.payment_is_registered(self.payment),
		self.category_name.save_category(self.category),
		self.product.register_product(self.product),
		self.order.create_order(self.order)
		#self.productorders.get_productorders(self.productorders)


if __name__ == "__main__":
	unittest.main()