print "This calculates compound interest."
print

principal = input("Please input the principal: ")
rate = input("Please input the interest rate as a whole number: ")
years = input("Please input the number of years: ")

principal=float(principal)
rate=float(rate)
rate=rate/100

sum=0.0

for i in range(years):
	interest=principal*rate
	principal=principal+interest
	sum=sum+interest
	print "Year", i+1, "earned ", interest, "interest."
		
print "The total amount of compound interest is: ", sum
print "The total compound interest including initial principal is: ", principal