#Car Rental App.
print
print ' ________ __________ _________     _________                 __________               __          __   '
print ' \______ \\______   \/   _____/     \_   ___ \_____ _______   \______   \ ____   _____/  |______  |  |  '
print '  |    |  \|    |  _/\_____  \      /    \  \/\__  \\_  __ \   |       _// __ \ /    \   __\__  \ |  |  '
print '  |    `   \    |   \/        \     \     \____/ __ \|  | \/  |    |   \  ___/|   |  \  |  / __ \|  |__'
print ' /_______  /______  /_______  /      \______  (____  /__|     |____|_  /\___  >___|  /__| (____  /____/'
print '         \/       \/        \/              \/     \/                \/     \/     \/          \/        '
print

#Imports Dealership from custom library and pandas.
from car import Dealership
import pandas as pd
#Sets the display width on pandas dataframe so columns aren't dropped down.
pd.set_option('display.width', 1000)
#Reads in the cars.csv file as a pandas dataframe.
carsdf = pd.read_csv('cars.csv', index_col = 0)

#Instantiates the Dealership.
dealership = Dealership()
#This uses the create_current_stock function which is explained in the library.
dealership.create_current_stock(carsdf)

#This commences a loop. Once the user is finished, the loop will end and the program will close.
proceed = 'y'
while proceed == 'y':
	#The user menu.
	print 'Please select one of the following options: \n'
	print '1: Car Rental.'
	print '2: Car Return.\n'
	answer = raw_input('Please select one of the above options 1/2: ')
	#The below if statement runs a different method depending on the user's choice.
	if answer == '1':
		dealership.process_rental()
	elif answer == '2':
		dealership.process_return()
	#This gives the user the option to close the loop.
	proceed = raw_input('\nWould you like to continue? y/n:')
	
print "\nThanks for using DBS Car Rental. Please come again.\n"
	


