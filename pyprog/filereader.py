import string

infile = open("testdata.csv", 'r') 	#open the datafile
outfile = open("testoutput.csv", 'w')	#open for a write
country = raw_input("Which country would you like to view :")
counter = 0
for line in infile:
	counter = counter+1
	if counter%10 == 0:
		print "Processed",counter,"records."
	lfields = string.split(line, ",")
	if lfields[3] == country:
		outfile.write(line)