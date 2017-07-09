import unittest

from car import Car, Dealership

#Tests the car functionality.
class TestCar(unittest.TestCase):

	def test_car_make(self):
		self.car = Car()
		self.assertEqual('', self.car.getMake())
		self.car.setMake('BMW')
		self.assertEqual('BMW', self.car.getMake())

	def test_car_model(self):
		self.car = Car()
		self.assertEqual('', self.car.getModel())
		self.car.setModel('M3')
		self.assertEqual('M3', self.car.getModel())

	def test_car_Type(self):
		self.car = Car()
		self.assertEqual('', self.car.getType())
		self.car.setType('Petrol')
		self.assertEqual('Petrol', self.car.getType())
		
	def test_car_colour(self):
		self.car = Car()
		self.assertEqual('', self.car.getColour())
		self.car.setColour('Yellow')
		self.assertEqual('Yellow', self.car.getColour())

	def test_car_Reg(self):
		self.car = Car()
		self.assertEqual('', self.car.getReg())
		self.car.setReg('172-G-1')
		self.assertEqual('172-G-1', self.car.getReg())
		
	def test_car_mileage(self):
		self.car = Car()
		self.assertEqual(0, self.car.getMileage())
		self.car.setMileage(45)
		self.assertEqual(45, self.car.getMileage())

	def test_car_Fuel(self):
		self.car = Car()
		self.assertEqual(0, self.car.getFuel())
		self.car.setFuel(88)
		self.assertEqual(88, self.car.getFuel())
		
	def test_car_Condition(self):
		self.car = Car()
		self.assertEqual('', self.car.getCondition())
		self.car.setCondition('Damaged')
		self.assertEqual('Damaged', self.car.getCondition())
		
	def test_car_Availability(self):
		self.car = Car()
		self.assertEqual('', self.car.getAvailability())
		self.car.setAvailability('True')
		self.assertEqual('True', self.car.getAvailability())

#Tests the dealship functionality.
class TestDealership(unittest.TestCase):

	def test_import_stock(self):
		import pandas as pd
		carsdf = pd.read_csv('cars.csv', index_col = 0)
		dealership = Dealership()
		self.car_list = dealership.create_current_stock(carsdf)
		#The actual test sees if the list of car instances match the dataframe
		self.assertEqual(carsdf['Registration'].loc[16], self.car_list[15].getReg())

	def test_stock_count(self):
		dealership = Dealership()
		stock_list = dealership.stock_count()
		#Becuase this function doesn't take any arguments we can only test to see if it works with an empty list. Still works though.
		self.assertEqual([0,0,0,0], stock_list)
		
	#There are two remaining class methods, however, since these contain user inputs, I am unsure of how to test them here.
	
if __name__ == '__main__':
	unittest.main()
