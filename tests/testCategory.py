import unittest 
import sys 
sys.path.append('../') 


from Methods.CreateCategory import Category 

class TestCategory(unittest.TestCase): 

	@classmethod
	def setUpClass(self):
		self.food = Category(
			category_name = "Food")


	def test_can_create_a_category(self): 
		self.assertIsInstance(self.food, Category)

	def test_can_register_category_to_database(self):
		self.food.save_category(self.food)
		self.assertTrue(Category.category_is_registered(self.food))


	def test_category_has_product(self):
		pass


		

# run unittest 
if __name__ == "__main__":
    unittest.main()