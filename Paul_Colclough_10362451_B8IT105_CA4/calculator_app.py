#Runfile for calculator.
#Imports the custom library containing the functions for calculating.
import calculator as cl

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
			print "11: Minimum Value"
			print "12: Maximum Value"
			print "13: List of Primes"
			print
			
			#The choice is determined by a function called from the library which validates the user's choice.
			choice = cl.menuchoice()
			
			#The following if statements run certain functions/calculations depending on the user's chosen input.
			#The calculation inputs are determined by one or two functions which validate the user's choice.
			if choice == 1:
				first = cl.firstinput()
				second = cl.secondinput()
				sum = cl.addit(first, second)
				print first, "+", second, "= ", sum

			elif choice == 2:
				first = cl.firstinput()
				second = cl.secondinput()
				sub = cl.subit(first, second)
				print first, "-", second, "= ", sub
					
			elif choice == 3:
				first = cl.firstinput()
				second = cl.secondinput()
				mult = cl.multit(first, second)
				print first, "*", second, "= ", mult
					
			elif choice == 4:
				first = cl.firstinput()
				second = cl.secondinput()
				div = cl.divit(first, second)
				print first, "/", second, "= ", float(div)
					
			elif choice == 5:
				first = cl.firstinput()
				second = cl.secondinput()
				exp = cl.expit(first, second)
				print "%s^%s = %s" % (first, second, exp)
					
			elif choice == 6:
				#This calculation just calls for one number to be inputted and validated.
				first = cl.firstinput()
				fact = cl.factit(first)
				print "%s! = %s" % (first, fact)
					
			elif choice == 7:
				#The formula for this calculation is displayed below for the user's convenience.
				print "\nnCr\n"
				n = cl.firstinput()
				r = cl.secondinput()
				comb = cl.combit(n, r)
				print "%sC%s = %s" % (n,r,comb)

			#The remaining three calculations are statistical in nature, therefore they require the data input instead.
			elif choice == 8:
				data = cl.statdata()
				print "The average of this dataset =", cl.avit(data)

			elif choice == 9:
				data = cl.statdata()
				print data
				sampop = cl.sampop()
				print "The variance of this dataset =", cl.varit(data, sample=sampop)
				
			elif choice == 10:
				data = cl.statdata()
				sampop = cl.sampop()
				print "The standard deviation of this dataset =", cl.sdevit(data, sample=sampop)
				
			elif choice == 11:
				data = cl.statdata()
				print "The minimum value in the dataset =", cl.minit(data)
			
			elif choice == 12:
				data = cl.statdata()
				print "The maximum value in the dataset =", cl.maxit(data)
				
			elif choice == 13:
				first = cl.firstinput()
				second = cl.secondinput()
				print "The prime numbers of the dataset =\n", cl.primeit(first, second)
			
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
