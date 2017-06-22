print "This calculates the least amount of coins needed to make change of any amount of money"		#This tells the user what the program does.
print
value = input("Please input the amount of money here: ")											#This asks the user to input their desired amount of money.



intvalue = int(value*100)																			#This changes the amount the user inputs into an integer.



twoeuro = intvalue/200																				#This gives us the amount of E2 coins.
intvalue = intvalue%200																				#This changes this variable so it excludes the number of E2 for the following equations.
if twoeuro > 0: 																					#This hides the answer if it is 0.
	print "The number of E2 coins is: ", twoeuro													#This displays the answer to the user.	


oneeuro = intvalue/100																				#This gives us the amount of E1 coins.
intvalue = intvalue%100																				#This changes this variable so it excludes the number of E1 for the following equations.
if oneeuro > 0: 																					#This hides the answer if it is 0.
	print "The number of E1 coins is: ", oneeuro													#This displays the answer to the user.	



fiftycent = intvalue/50																				#This gives us the amount of 50c coins.
intvalue = intvalue%50																				#This changes this variable so it excludes the number of 50c for the following equations.
if fiftycent > 0: 																					#This hides the answer if it is 0.
	print "The number of 50c coins is: ", fiftycent													#This displays the answer to the user.


twentycent = intvalue/20																			#This gives us the amount of 20c coins.
intvalue = intvalue%20																				#This changes this variable so it excludes the number of 20c for the following equations.
if twentycent > 0: 																					#This hides the answer if it is 0.
	print "The number of 20c coins is: ", twentycent												#This displays the answer to the user.

	
	
tencent = intvalue/10																				#This gives us the amount of 10c coins.
intvalue = intvalue%10																				#This changes this variable so it excludes the number of 10c for the following equations.
if tencent > 0: 																					#This hides the answer if it is 0.
	print "The number of 10c coins is: ", tencent


fivecent = intvalue/5																				#This gives us the amount of 5c coins.
intvalue = intvalue%5																				#This changes this variable so it excludes the number of 5c for the following equations.
if fivecent > 0: 																					#This hides the answer if it is 0.
	print "The number of 5c coins is: ", fivecent													#This displays the answer to the user.


twocent = intvalue/2																				#This gives us the amount of 2c coins.
intvalue = intvalue%2																				#This changes this variable so it excludes the number of 2c for the following equations.
if twocent > 0: 																					#This hides the answer if it is 0.
	print "The number of 2c coins is: ", twocent													#This displays the answer to the user.


	
onecent = intvalue/1																				#This gives us the amount of 1c coins.
intvalue = intvalue%1																				#This changes this variable so it excludes the number of 1c for the following equations.
if onecent > 0: 																					#This hides the answer if it is 0.
	print "The number of 1c coins is: ", onecent													#This displays the answer to the user.