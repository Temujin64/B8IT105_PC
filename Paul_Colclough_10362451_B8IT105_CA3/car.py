# Define a class for my car.

class Car(object):
# implement the car object.
	
	def __init__(self):
		self.__make = ''
		self.__model = ''
		self.__type = ''
		self.__colour = ''
		self.__reg = ''
		self.__mileage = 0
		self.__fuel = 0
		self.__condition = ''
		self.__available = ''
		self.distance = 0
		self.consumption = 0
		self.user_damage = False

#Get Methods.
		
	def getMake(self):
		return self.__make
		
	def getModel(self):
		return self.__model
		
	def getType(self):
		return self.__type

	def getColour(self):
		return self.__colour

	def getReg(self):
		return self.__reg
		
	def getMileage(self):
		return self.__mileage
		
	def getFuel(self):
		return self.__fuel
		
	def getCondition(self):
		return self.__condition	
		
	def getAvailability(self):
		return self.__available

#SetMethods.
		
	def setMake(self, make):
		self.__make = make
	
	def setModel(self, model):
		self.__model = model	
		
	def setType(self, type):
		self.__type = type
	
	def setColour(self, colour):
		self.__colour = colour
		
	def setReg(self, reg):
		self.__reg = reg

	def setMileage(self, mileage):
		self.__mileage = mileage
		
	def setFuel(self, fuel):
		self.__fuel = fuel
		
	def setCondition(self, condition):
		self.__condition = condition
		
	def setAvailability(self, available):
		self.__available = available

#From here I must import pandas as some of following methods take a pandas dataframe as an argument.
import pandas as pd
carsdf = pd.read_csv('cars.csv', index_col = 0)

class Dealership(object):
	#Bear with me hear, I'm fairly sure that I mix up my OOP terminology quite a lot here.
	def __init__(self):
		self.car_list = []

	def create_current_stock(self, carsdf):
		#This creates a dictionary of variables which for now are all equal to the empty object Car().
		#Since it is based off the length of carsdf, there is a unique variable for each car.
		#This was a solution to a problem where I had a list of 40 identical car objects.
		#Now each object in the list self.car_list represents each car in carsdf.
		d={}
		cars = []
		for i in range(len(carsdf)):
			d['car{0}'.format(i)] = Car()
			cars.append(d['car{0}'.format(i)])

		#This for loop assigns unique values to the objects assigned to the variables in the cars list.
		#Now each car in carsdf has its own object in the list self.car_list.
		for i in range(len(carsdf)):
			cars[i].setMake(carsdf['Make'].loc[i+1])
			cars[i].setModel(carsdf['Model'].loc[i+1])
			cars[i].setType(carsdf['Type'].loc[i+1])
			cars[i].setColour(carsdf['Colour'].loc[i+1])
			cars[i].setReg(carsdf['Registration'].loc[i+1])
			cars[i].setMileage(carsdf['Odometer'].loc[i+1])
			cars[i].setFuel(carsdf['Fuel %'].loc[i+1])
			cars[i].setCondition(carsdf['Condition'].loc[i+1])
			cars[i].setAvailability(carsdf['Available'].loc[i+1])
			self.car_list.append(cars[i])
		
		#This returns self.car_list so that it can be tested in test_car.py.
		return self.car_list

	#This method takes stock of the cars
	def stock_count(self):
		#The different car types are first assigned a variable to represent their quantity.
		pstock = 0
		dstock = 0
		hstock = 0
		estock = 0
		#The loop goes through each object in self.car_list.
		#It reads the type and then adds 1 to the corresponding stock variable if the car's availability is True.
		for i in self.car_list:
			if i.getAvailability() == True and i.getType() == 'Petrol':
				pstock = pstock + 1
			elif i.getAvailability() == True and i.getType() == 'Diesel':
				dstock = dstock + 1
			elif i.getAvailability() == True and i.getType() == 'Hybrid':
				hstock = hstock + 1
			elif i.getAvailability() == True and i.getType() == 'Electric':
				estock = estock + 1
		print 'Petrol cars in stock:', pstock
		print 'Diesel cars in stock: ', dstock
		print 'Hybrid cars in stock: ', hstock
		print 'Electric cars in stock: ', estock
		
		#The stock variables are assigned to a list so that they can be returned as one variable.
		stock_list = [pstock, dstock, hstock, estock]

		return stock_list

	#This is the function that performs the renting
	def process_rental(self):
		#First a loop is created that repeats as long as the user wishes to continue renting cars.
		selecting = 'y'
		while selecting == 'y':
			stock_list = self.stock_count()
			#Skips the renting process if there are no cars available.
			if stock_list == [0,0,0,0]:
				print "Sorry, nothing to rent, please try again."
				selecting = 'n'
			else:
				#The dataframe is printed so the user can see the available cars.
				print carsdf
				#The user selects their prefered car
				answer = input('\nPlease enter the ID of the car you would like:')
				#The following if statements provide some validation.
				#This ensures that the user doesn't select a number not represented in the dataframe. This avoids an indexing error.
				if answer > 40 or answer <=0:
					print '\nNo car with this ID. Please try again\n.'
				#This ensures that the user does not select a car that is not available to rent.
				elif carsdf['Available'].loc[answer] == False:
					print '\nThis car is not available to rent. Please try again\n.'
				else:
					#This sets the chosen car as unavailable in self.car_list.
					self.car_list[answer-1].setAvailability(False)
					#This does the same in the carsdf dataframe
					carsdf.ix[answer, 'Available'] = False
					#This simply slices out the user's selected car.
					print carsdf.loc[[answer]]
				#This gives the user the option to end the while loop.
				selecting = raw_input('\nWould you like to rent another car? y/n: ')	
				#This displays the stock account which will have changed if the user rents any cars.
				self.stock_count()
		#This writes out the dataframe, replacing the old one. This ensures the data is updated after the program closes.
		carsdf.to_csv('cars.csv')
	
	def process_return(self):
		#First a loop is created that repeats as long as the user wishes to continue returning cars.
		selecting = 'y'
		while selecting == 'y':
			#The dataframe is printed so the user can see the available cars.
			print carsdf
			#The user selects the car that they are returning.
			answer = input('\nPlease enter the ID of the car you are returning: ')
			#1 is subtracted from the answer becuase of Python's 0 indexing.
			answer = answer - 1
			#This ensures that the user doesn't select a number not represented in the dataframe. This avoids an indexing error.
			if answer > 39 or answer <0:
				print '\nNo car with this ID. Please try again\n'
			#This ensures that the user does not select a car which has not been rented out.
			elif self.car_list[answer].getAvailability() == True:
				print '\nThis car has not been rented out.'
			else:
				#This sets the chosen car as available in self.car_list.
				self.car_list[answer].setAvailability(True)
				#This does the same in the carsdf dataframe. 1 is added because pandas dataframes are 1 indexed.
				carsdf.ix[(answer+1), 'Available'] = True
				#This asks the user for the odometer reading.
				odometer = int(raw_input('\nPlease enter the current reading on the odometer: '))
				#This calculates the distance driven by the user
				self.distance = odometer - self.car_list[answer].getMileage()
				#This updates self.car_list to show the new odometer reading.
				self.car_list[answer].setMileage(odometer)
				#This does the same for the dataframe.
				carsdf.ix[(answer+1), 'Odometer'] = odometer
				#This shows the user how much they drove.
				print "\nYou drove %skm." % (self.distance)
				#This asks the user for the reading on the fuel gauge.
				fuel_gauge = int(raw_input('\nPlease enter the current reading on the fuel gauge (%): '))
				#This calculates the fuel consumption. Neither the list nor dataframe are updated since the car is automatically refilled.
				self.consumption = self.car_list[answer].getFuel() - fuel_gauge
				#This tells the user how much fuel they consumed.
				print "\nYou used " + str(self.consumption) + "% of the fuel."
				#This asks the user if there's any damage on the car.
				damage = raw_input('\nIs there any damange on the car y/n: ')
				#These if statements update the damage status determine whether or not it was the user who damaged the car.
				if damage == 'y' and self.car_list[answer].getCondition() == 'Damaged':
					self.user_damage = False
					print "\nDon't worry, the car was damaged when you got it!"
				elif damage == 'y' and self.car_list[answer].getCondition() == 'Undamaged':
					self.user_damage = True
					print "\nYou damaged the car! You'll pay for this... literally."
				elif damage == 'n' and self.car_list[answer].getCondition() == 'Undamaged':
					self.user_damage = False
					print "\nYou returned the car without any damage, thanks!"
				elif damage == 'n' and self.car_list[answer].getCondition() == 'Damaged':
					self.user_damage = False
					print "\nIt appears as though you fixed the car for us, thanks!"
					print "\nBut if you're lying about the damange, don't worry, it was there before.\n"
			#This gives the user the option to exit the loop.	
			selecting = raw_input('\nWould you like to return another car? y/n: ')	
		#This shows the updated stock count.
		self.stock_count()
		#This writes out the dataframe, replacing the old one. This ensures the data is updated after the program closes.
		carsdf.to_csv('cars.csv')