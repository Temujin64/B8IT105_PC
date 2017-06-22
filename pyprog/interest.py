print "This calculates the total payment on a loan including interest"
print

print "Firstly, the initial principle must be entered."
principle = input("Please input the amount to the nearest whole number here: ")								#The user enters the principle.
print
print "Secondly, the interest rate as a fraction of 1 must be entered, for example, 10% becomes 0.10."
rate = input("Please input the interest rate here: ")														#The user enters the interest rate .
print
print "Lastly, the number of years the loan will last must be entered."
years = input("Please input the number of years here: ")													#The user enters the number of years.
print
total = principle+(principle*rate*years)
print
if total >= 500000:
	 print "The total loan repayment amount is: Too much"
else:
	print  "The total loan repayment amount is:",total,"Euro"												#The calculation is returned.