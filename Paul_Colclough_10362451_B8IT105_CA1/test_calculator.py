#This functions validates the menu option so that only an integer or float will be accepted.
def menuchoice():
	invalid = 1
	while invalid == 1:
		try:
			invalid = 0
			choice = input("Please enter your choice: ")
		#This what happens when a non-numeric value is entered.
		except NameError:
			print "\nNumerical values only please.\n"
			invalid = 1
		#This code was the only way I could prevent the program from crashing if the user hit enter without entering a value.
		except SyntaxError:
			invalid = 1
	return choice

#Similar input validation for the first entry into the calculation.
def firstinput():
	invalid = 1
	while invalid == 1:
		try:
			invalid = 0
			first = input("Please enter the first number: ")
		except NameError:
			print "\nNumerical values only please.\n"
			invalid = 1
		except SyntaxError:
			invalid = 1
	return first

#Same code as above but changes the print statement to reflect that this is the second number being input.	
def secondinput():
	invalid = 1
	while invalid == 1:
		try:
			invalid = 0
			second = input("Please enter the second number: ")
		except NameError:
			print "\nNumerical values only please.\n"
			invalid = 1
		except SyntaxError:
			invalid = 1
	return second

#Function for the addition calculation.	
def addit(first, second):
	return first + second

#Function for the subtraction calculation.	
def subit(first, second):
	return first - second

#Function for the multiplication calculation.	
def multit(first, second):
	return first * second

#Function for the division calculation.
#These inputs must be converted to floats to ensure that the answer is not rounded when two integers are entered.
def divit(first, second):
	first = float(first)
	second = float(second)
	return first / second

#Function for the exponentiation calculation.		
def expit(first, second):
	return first ** second

#Function for the factorisation calculation.	
def factit(n):
	if n > 1:
		return n * factit(n - 1)
	if n < 0:
		return 'inf'
	return 1

#Function for the combinations rule calculation.		
def combit(n, r):
	return factit(n)/(factit(r)*factit(n-r))

#This prompts the user to enter a series of numbers for a dataset.
def statdata():

	#This defines the data as an empty list.
	data = []
	#The user is given instructions.
	print "\nPlease enter the elements of the dataset below. Enter a non-numeric character when you are done.\n"
	
	#The while loop continues until it's broken by the user entering in a non-numeric character.
	invalid = 1
	while invalid == 1:
		try:
			element = input()
		#This what happens when a non-numeric value is entered.
		except NameError:
			invalid = 0
		#This code was the only way I could prevent the program from crashing if the user hit enter without entering a value.
		except SyntaxError:
			invalid = 0
		
		if invalid == 1:
			element = float(element)
			data.append(element)
	
	return data
	
	#This original code required that the user provide the value for n before entering the numbers.
	#I changed it for the above code because fora  longer dataset, first counting the number of elements can be tedious.
	
	#num = raw_input("Please enter the number of elements in the dataset")
	#for i in range(num):
		#invalid = 0
		#element = float(raw_input("Please enter the value for this element: "))
		#data.append(element)

#Function for the average calculation.
def avit(data):
	sumdata = sum(data)
	n = len(data)
	average = sumdata / n
	return average

#This asks the user whether the previously entered dataset is a sample or population.
def sampop():
	invalid = 1

	while invalid == 1:
		invalid = 0
		sampop = raw_input("\nIs this a sample or population (S/P): ")
		print
		if sampop == "S" or sampop == "s" or sampop == "Sample" or sampop == "sample":
			sampop = True
		elif sampop == "P" or sampop == "p" or sampop == "Population" or sampop == "population":
			sampop = False
		else:
			print "Incorrect response, please type S for sample or P for population."
			invalid = 1
	return sampop
	
#Function for the variance calculation.
def varit(data, sample=True):
	sumdata = sum(data)
	n = len(data)
	sumsq = sumdata**2
	averagesq = sumsq/(n)
	sumdataexp = 0
	for i in data:
		exp = i**2
		sumdataexp = sumdataexp + exp
	invalid = 1
	if sample == True:
		varit = (sumdataexp - averagesq)/(n-1)
	elif sample == False:
		varit = (sumdataexp - averagesq)/(n)
	return varit

#The last calculation requires the square root calculation so it is imported from the math library.
from math import sqrt
	
#Function for the standard deviation calculation.	
def sdevit(data, sample=True):
	sumdata = sum(data)
	n = len(data)
	sumsq = sumdata**2
	averagesq = sumsq/(n)
	sumdataexp = 0
	for i in data:
		exp = i**2
		sumdataexp = sumdataexp + exp
	#The if statement has two different calculations depending on whether the dataset was a sample or not.
	if sample == True:
		sdevit = sqrt((sumdataexp - averagesq)/(n-1))
	elif sample == False:
		sdevit = sqrt((sumdataexp - averagesq)/(n))
	return sdevit
	
#This imports a library used for testing the functions.
import unittest as ut

class TestCalculations(ut.TestCase):
#I wanted to test the input validation functions but couldn't since the input was within the function as opposed to an argument.
	
	#This tests the addition calculation.		
	def testaddit(self):
		self.assertEqual(12, addit(8,4))

	#This tests the subtraction calculation.		
	def testsubit(self):
		self.assertEqual(4, subit(8,4))

	#This tests the multiplication calculation.				
	def testmultit(self):
		self.assertEqual(32, multit(8,4))

	#This tests the division calculation.				
	def testdivit(self):
		self.assertEqual(2.5, divit(10,4))

	#This tests the exponentiation calculation.		
	def testexpit(self):
		self.assertEqual(4096, expit(8,4))

	#This tests the factorisation calculation.			
	def testfactit(self):
		self.assertEqual(1, factit(0))
		self.assertEqual(1, factit(1))
		self.assertEqual(120, factit(5))
		self.assertEqual(720, factit(6))
		self.assertEqual(3628800, factit(10))
		self.assertEqual('inf', factit(-3))

	#This tests the combinations rule calculation.		
	def testcombit(self):
		self.assertEqual(15, combit(6,4))

	#This tests the average	calculation.		
	def testavit(self):
		self.assertEqual(11.25, avit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0]))

	#This tests the variance calculation.
	#Once for sample and once for population but using the same dataset.
	def testvarit(self):
		self.assertEqual(2.7857142857142856, varit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=True))
		self.assertEqual(2.4375, varit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=False))

	#This tests the standard deviation calculation.	
	#Once for sample and once for population but using the same dataset.
	def testsdevit(self):
		self.assertEqual(1.6690459207925603, sdevit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=True))
		self.assertEqual(1.5612494995995996, sdevit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=False))

#This ensures that the class methods are only being used if this program is running them.
#i.e. These methods can't be called from another program by importing this file as a library.
if __name__ == '__main__':
	ut.main()
	


