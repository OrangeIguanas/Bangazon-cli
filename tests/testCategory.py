# This is a test to ensure that categories is being created with required properties
import unittest 
import sys 
sys.path.append('../') 
# import the Category class for testing
from Methods.CreateCategory import Category 

class TestCategory(unittest.TestCase): 
# Test for an instance of category with a name value 
	def test_category_creation(self): 

		food = Category(name = "Cooler Ranch Doritos")
		self.assertIsInstance(food, Category)
		# print the result 
		print(food.get_category_name())

# run unittest 
if __name__ == "__main__":
    unittest.main()