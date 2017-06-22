import string

#Asks for your csv location.

fname=raw_input("Enter filename: ")

#open the datafile
infile = open(fname, 'r')
infile = infile.readlines()[1:]

#open for a write
outfile = open("sqlinputvalues.csv", 'w')

for line in infile:
	lfields = string.split(line, ",")
	line="'%s' " %"', '".join(lfields)
	line="("+line+")\n"
	line = line[:-4] + line[-2:]
	line = line[:-3] + "'),\n"
	outfile.write(line)

outfile.close()
	

#	line = line.replace("", "")