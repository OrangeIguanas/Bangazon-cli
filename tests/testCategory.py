# This is a test to ensure that categories is being created with required properties
import unittest 
import sys 
sys.path.append('../') 
# import the Category class for testing
from Methods.CreateCategory import Category 

class TestCategory(unittest.TestCase): 
# Test for an instance of category with a name value 
	def test_can_create_a_category(self): 

		food = Category(category_name= "Food")
		self.assertIsInstance(food, Category)
		# print the result 
		print(food.get_category_name())

	def test_can_register_category_to_database(self):
		food = Category(category_name = "Food")
		food.save_category(food)
		self.assertTrue(Category.category_is_registered(food))


	def test_category_has_product(self):
		pass


		

# run unittest 
if __name__ == "__main__":
    unittest.main()