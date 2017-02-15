import unittest 
import sys 
sys.path.append('../') 


from Methods.CreateCategory import Categories

class TestCategory(unittest.TestCase): 

	"""
	Purpose: Test Category
	Author: Zach
	Tests: 
		test_can_create_a_category
		test_can_register_category_to_database

	"""

	@classmethod
	def setUpClass(self):
		self.food = Categories(
			category_name = "Food")


	def test_can_create_a_category(self):
		# Test is food a type of Category
		self.assertIsInstance(self.food, Categories)

	def test_can_register_category_to_database(self):
		# Test if Food can be added to the database
		# Test if Food is in the Database
		self.food.save_category(self.food)
		self.assertTrue(Category.category_is_registered(self.food))


	

		


		

# run unittest 
if __name__ == "__main__":
    unittest.main()