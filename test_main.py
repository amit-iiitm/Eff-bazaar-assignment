import unittest
from main import Products

#Inherit the unittest.TestCase class for testing our functions
class TestMethods(unittest.TestCase):
	
	#setup the product instance that all testing functions will use
	def setUp(self):
		#create an instance of Products class
		self.products_inst=Products('products.csv')

	#test the get_products_names function
	def test_get_products_names(self):
		#reference list of products that should be given by function
		ref_names=['Coriander Leaves (April-Nov)', 'Mint Leaves 500 Gm', 'Ginger 500 Gm', 'Lemon 500 Gm', 'Green Chilly', 'Coconut Brown (Husk)', 'Garlic Whole', 'Capsicum Green', 'Lemon', 'Chinese Cucumber 1 Kg', 'Pumpkin Red', 'Bottleguard (Lauki)', 'Cabbage (April-November)', 'Brinjal (Small)', 'CHICKEN BONELESS BREST', 'CHICKEN TANDOOR 700-800', 'Tomato Table / Salad', 'Coriander Leaves (April-Nov) 500 Gm', 'Carrot (April-November) 500 Gm', 'Brinjal (Big) Bharta', 'Cucumber', 'Ginger', 'Carrot (April-November)', 'Green Chilly 500 Gm']
		self.assertEqual(self.products_inst.get_products_names(),ref_names)

	#test the get_products_codes function
	def test_get_products_codes(self):
		#reference list of products codes
		ref_codes=[3736, 4371, 4356, 4365, 3732, 3646, 3746, 3725, 3759, 4681, 3777, 3719, 3723, 3722, 2565, 3593, 3790, 4345, 4340, 3720, 3740, 3748, 3727, 4341]
		#assert the functions output with reference
		self.assertEqual(self.products_inst.get_products_codes(),ref_codes)

	#test the get_vendors function that gives list of vendor for a product
	def test_get_vendors(self):
		#reference list of vendors
		vendors=['Vendor1', 'Vendor2', 'Vendor3']
		#assert the function output with list of vendors 
		self.assertEqual(self.products_inst.get_vendors(3736),vendors)
		self.assertEqual(self.products_inst.get_vendors(3777),vendors)
		self.assertEqual(self.products_inst.get_vendors(3727),vendors)

	#test the get_cheapest_prices that gives list of cheapest prices
	def test_get_cheapest_prices(self):
		#reference output of first few products
		cheapest_products=[[3, 'Vendor1', 'Ginger 500 Gm', 4356, 'Grams', 500.0, 29.5, 59.0], [7, 'Vendor1', 'Garlic Whole', 3746, 'Kg', 1.0, 105.0, 105.0], [8, 'Vendor1', 'Capsicum Green', 3725, 'Kg', 1.5, 78.0, 52.0], [10, 'Vendor1', 'Chinese Cucumber 1 Kg', 4681, 'Kg', 1.0, 60.0, 60.0], [11, 'Vendor1', 'Pumpkin Red', 3777, 'Kg', 1.5, 20.0, 13.333333333333334], [13, 'Vendor1', 'Cabbage (April-November)', 3723, 'Kg', 4.0, 30.0, 7.5]]
		
		#assert the output returned by cheapest price function with refernce here
		self.assertEqual(self.products_inst.get_cheapest_prices()[5],cheapest_products[5])
		self.assertEqual(self.products_inst.get_cheapest_prices()[1],cheapest_products[1])
		self.assertEqual(self.products_inst.get_cheapest_prices()[4],cheapest_products[4])
		self.assertEqual(self.products_inst.get_cheapest_prices()[3],cheapest_products[3])

	#test the get_expensive_prices that gives list of expensive prices
	def test_get_expensive_prices(self):
		#reference output of first few products
		expensive_products=[[1, 'Vendor1', 'Coriander Leaves (April-Nov)', 3736, 'Kg', 3.0, 90.0, 30.0], [2, 'Vendor1', 'Mint Leaves 500 Gm', 4371, 'Grams', 500.0, 27.5, 55.0], [6, 'Vendor1', 'Coconut Brown (Husk)', 3646, 'Kg', 1.0, 20.0, 20.0], [7, 'Vendor1', 'Garlic Whole', 3746, 'Kg', 1.0, 105.0, 105.0], [8, 'Vendor1', 'Capsicum Green', 3725, 'Kg', 1.5, 78.0, 52.0], [9, 'Vendor1', 'Lemon', 3759, 'Kg', 1.0, 65.0, 65.0]]

		#assert the output returned by expensive price function with refernce here
		self.assertEqual(self.products_inst.get_expensive_prices()[5],expensive_products[5])
		self.assertEqual(self.products_inst.get_expensive_prices()[1],expensive_products[1])
		self.assertEqual(self.products_inst.get_expensive_prices()[4],expensive_products[4])
		self.assertEqual(self.products_inst.get_expensive_prices()[3],expensive_products[3])

	#test the get_specific_prices that returns cheapest prices of given products
	def test_get_specific_prices(self):
		#reference output for list [3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341] product codes
		specific_prod_prices=[[25, 'Vendor2', 'Coriander Leaves (April-Nov)', 3736, 'Kg', 3.0, 80.0, 26.666666666666668], [3, 'Vendor1', 'Ginger 500 Gm', 4356, 'Grams', 500.0, 29.5, 59.0], [29, 'Vendor2', 'Green Chilly', 3732, 'Kg', 1.0, 37.5, 37.5], [7, 'Vendor1', 'Garlic Whole', 3746, 'Kg', 1.0, 105.0, 105.0], [33, 'Vendor2', 'Lemon', 3759, 'Kg', 1.0, 63.0, 63.0], [60, 'Vendor3', 'Bottleguard (Lauki)', 3719, 'Kg', 1.5, 22.0, 14.666666666666666], [45, 'Vendor2', 'Cucumber', 3740, 'Kg', 3.0, 23.0, 7.666666666666667], [24, 'Vendor1', 'Green Chilly 500 Gm', 4341, 'Grams', 500.0, 20.0, 40.0]]

		self.assertEqual(self.products_inst.get_specific_prices([3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]), specific_prod_prices)


if __name__ == '__main__':
	unittest.main()
