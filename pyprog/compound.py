print "This calculates compound interest."															#This tells the user what the program does.
print
principal = input("Please input the principal: ")													#This asks the user to input their desired amount of money.
rate = input("Please input the interest rate as a whole number: ")												#This asks the user to input their desired amount of money.
years = input("Please input the number of years: ")													#This asks the user to input their desired amount of money.

principal=float(principal)
rate=float(rate)
rate=rate/100

compound=principal*(1+rate)**years

print "Your total amount with compound interest is: ", compound