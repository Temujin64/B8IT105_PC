#months is a list used as a lookup table
months=['January','February','March','April','May','June','July','August','September','October','November','December']

n=input("Please enter a month from 1-12: ")

ind=n-1

mon=months[ind]

print "The month is", mon+"."
