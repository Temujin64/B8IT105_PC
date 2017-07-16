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
#This function introduces lambda
def addit(first, second):
	addit = lambda x,y: x+y
	return addit(first, second)

#Function for the subtraction calculation.	
def subit(first, second):
	subit = lambda x,y: x-y
	return subit(first, second)

#Function for the multiplication calculation.	
def multit(first, second):
	multit = lambda x,y: x*y
	return multit(first, second)

#Function for the division calculation.
#These inputs must be converted to floats to ensure that the answer is not rounded when two integers are entered.
def divit(first, second):
	first = float(first)
	second = float(second)
	divit = lambda x,y: x/y
	return divit(first, second)

#Function for the exponentiation calculation.		
def expit(first, second):
	expit = lambda x,y: x**y
	return expit(first, second)

#Function for the factorisation calculation.	
def factit(n):
	factit = lambda x: 1 if x == 0 else x * factit(x-1)
	return factit(n)

#Function for the combinations rule calculation.		
def combit(n, r):
	combit = lambda x,y: factit(x)/(factit(y)*factit(x-y))
	return combit(n, r)

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

#Function for the average calculation.
def avit(data):
	return (reduce(lambda x,y:x+y, data))/((len(data)))
	

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
#This function introduces map and reduce.
def varit(data, sample=True):
	sumdata = reduce(lambda x,y:x+y, data)
	n = len(data)
	sumsq = sumdata**2
	averagesq = sumsq/(n)
	sumdataexp = reduce(lambda x,y:x+y, (map(lambda x: x*x, data)))
	if sample == True:
		varit = (sumdataexp - averagesq)/(n-1)
	elif sample == False:
		varit = (sumdataexp - averagesq)/(n)
	return varit

#Function for the standard deviation calculation.
#This function introduces list comprehension.
#It would be simpler to call the varit function and get the square root, but I kept the steps involved in order to showcase list comprehension.
def sdevit(data, sample=True):
	sumdata = sum(data)
	n = len(data)
	sumsq = sumdata**2
	averagesq = sumsq/(n)
	sumdataexp = reduce(lambda x,y:x+y, ([x*x for x in data]))
	#The if statement has two different calculations depending on whether the dataset was a sample or not.
	if sample == True:
		sdevit = ((sumdataexp - averagesq)/(n-1))**0.5
	elif sample == False:
		sdevit = ((sumdataexp - averagesq)/(n))**0.5
	return sdevit

#Function for the standard deviation calculation.
#This function introduces filter.
def minit(data):
	min = lambda a,b: a if (a<b) else b
	return reduce(min, data)
	
#Function for the standard deviation calculation.
def maxit(data):
	max = lambda a,b: a if (a>b) else b
	return reduce(max, data)
	
#Function for the standard deviation calculation.
def primeit(first, second):
	primes = range(first, (second+1)) 
	for i in range(2, 8): 
		 primes = filter(lambda x: x == i or x % i, primes)
	return primes

	