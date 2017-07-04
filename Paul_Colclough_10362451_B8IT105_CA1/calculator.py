#Runfile for calculator.
#Imports the custom library containing the functions for calculating.
import test_calculator as tc

#This sets up a while loop to catch an EOF error. In other words it gives the user the option to quit the program manually.
quit = 1
while quit == 1:
	quit = 0
	try:
		#This while loop allows for the user to return to this menu when they have completed the calculation.
		invalid = 1
		while invalid == 1:
			#This presents the user with the list of options as well as informing them of the escape option.
			print "\n%40s\n" % ("C A L C U L A T O R    M E N U")
			print "Enter CTRL+z to quit at any time\n."
			print "Please choose from one of the following options:\n"
			print "1: Addition"
			print "2: Subtraction"
			print "3: Multiplication"
			print "4: Division"
			print "5: Exponentiation"
			print "6: Factorisation"
			print "7: Combinations Rule"
			print "8: Average"
			print "9: Variance"
			print "10: Standard Deviation"
			print
			
			#The choice is determined by a function called from the library which validates the user's choice.
			choice = tc.menuchoice()
			
			#The following if statements run certain functions/calculations depending on the user's chosen input.
			#The calculation inputs are determined by one or two functions which validate the user's choice.
			if choice == 1:
				first = tc.firstinput()
				second = tc.secondinput()
				sum = tc.addit(first, second)
				print first, "+", second, "= ", sum

			elif choice == 2:
				first = tc.firstinput()
				second = tc.secondinput()
				sub = tc.subit(first, second)
				print first, "-", second, "= ", sub
					
			elif choice == 3:
				first = tc.firstinput()
				second = tc.secondinput()
				mult = tc.multit(first, second)
				print first, "*", second, "= ", mult
					
			elif choice == 4:
				first = tc.firstinput()
				second = tc.secondinput()
				div = tc.divit(first, second)
				print first, "/", second, "= ", float(div)
					
			elif choice == 5:
				first = tc.firstinput()
				second = tc.secondinput()
				exp = tc.expit(first, second)
				print "%s^%s = %s" % (first, second, exp)
					
			elif choice == 6:
				#This calculation just calls for one number to be inputted and validated.
				first = tc.firstinput()
				fact = tc.factit(first)
				print "%s! = %s" % (first, fact)
					
			elif choice == 7:
				#The formula for this calculation is displayed below for the user's convenience.
				print "\nnCr\n"
				n = tc.firstinput()
				r = tc.secondinput()
				comb = tc.combit(n, r)
				print "%sC%s = %s" % (n,r,comb)

			#The remaining three calculations are statistical in nature, therefore they require the data input instead.
			elif choice == 8:
				data = tc.statdata()
				print "The average of this dataset =", tc.avit(data)

			elif choice == 9:
				data = tc.statdata()
				print data
				sampop = tc.sampop()
				print "The variance of this dataset =", tc.varit(data, sample=sampop)
				
			elif choice == 10:
				data = tc.statdata()
				sampop = tc.sampop()
				print "The standard deviation of this dataset =", tc.sdevit(data, sample=sampop)
			
			#This section of code gives the user the opportunity to either quit the program or return to the menu above.
			returntonmenu = raw_input("\nEnter R to return to main menu or any other character to exit: ")
			if returntonmenu == "R" or returntonmenu == "r":
				pass
			else:
				print "\nGoodbye!"
				invalid = 0
	
	#This is the prompt given to a user who manually quits the program.
	except EOFError:
		print "You have manually terminated the program."			
