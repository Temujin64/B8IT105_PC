a=input("Please input a number: ")
b=input("Please input another number: ")
c=input("Please input one more number: ")

maxi=a
if b>maxi:
	maxi=b
if c>maxi:
	maxi=c
	
print "The largest number is", maxi, "."