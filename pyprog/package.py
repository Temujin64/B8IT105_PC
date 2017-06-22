express = raw_input("Is this express post (Y/N): ")

packageweight = input("What is the package weight?: ")

regular = raw_input("Is this a regular customer (Y/N): ")


if express == "Y":
	rate = 10

elif express ==  "N":
	rate = 5
	
if packageweight <= 100:
	surcharge = packageweight * 0.03
	
elif packageweight <= 900:
	surcharge = 100 * 0.03
	surcharge = surcharge + ((packageweight -100)* 0.02)
	
else:
	surcharge = 100 * 0.03
	surcharge = surcharge + (900* 0.02)
	surcharge = surcharge + ((packageweight - 1000) * 0.01)
	
subtotal =  rate + surcharge

if regular == "Y":
	discount = 0.9
	discounted = 0.1 * subtotal

elif regular == "N":
	discount = 1
	
discounttotal = subtotal * discount


print "Express rate: %0.2f" % (rate)
print "Weight surcharge: %0.2f" % (surcharge)
print "Subtotal %0.2f" % (subtotal)
print "Discount %0.2f" % (discounted)
print "Total due %0.2f" % (discounttotal)