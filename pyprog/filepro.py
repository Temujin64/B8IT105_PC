fname=raw_input("Enter filename: ")

infile = open(fname, 'r')
for i in range(infile):
	line = infile.readline()
	print line[:-1]