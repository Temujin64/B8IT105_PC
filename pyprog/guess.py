#This program makes the user guess a random number.
#The user will keep on guessing until they get it right or rage quit.

#Imports the random library, can be referred to as rd instead of random.
import random as rd

#The function that defines the random number.
randomnumber = rd.randint(1,100)

#The number that the user inputs.
usernumber = input("Please pick a number between 1 and 100: ")

#This determines when to end the loop.
#If the user guesses incorrectly tryagian remains True.
#When the user guesses correctly it changes to False and the loop ends.
tryagain = True

#This is the loop.
#If the user's guess is too high or too low they are told so and they are told to guess again. This new guess overwrites the usernumber variable.
#When the user guesses incorrectly the tryagain variable does not change.
#If the user guesses correctly they are told so. The tryagain variable changes to false and the loop ends.
while tryagain == True:
	if usernumber > randomnumber:
		print "Too high."
		usernumber=input("Try again: ")
	elif usernumber < randomnumber:
		print "Too low."
		usernumber=input("Try again: ")
	else:
		print "You guessed correctly!"
		tryagain = False