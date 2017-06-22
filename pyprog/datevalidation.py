import string

def GetAndValidateDate(prompt):
	months = ["January","February","March","April","May","June","July",
				"August","September","October","November","December"]

	# Validate Input String

	invalid = 1								# Set invalid to 1 so loop executes

	while invalid == 1:
		invalid = 0							# Assume validation passes

		inputDate = raw_input(prompt)
		
	# Normalise the string

	#	print "Before ", inputDate
	#	splitDate = string.split(inputDate," ")
	#	inputDate = string.join(splitDate,"")
	#	print "After ",inputDate
		
		inputDate = string.replace(inputDate, " ", "")
		inputDate = string.replace(inputDate, chr(9), "") # Its a TAB!!

		
	# Validate that the string only contains "0"-"9"or "/"

		mm,dd,yyyy = string.split(inputDate, "/")

		
		for ch in inputDate:
			if (ord(ch) < 47 or ord(ch) >59):
				invalid = 1
				print "Invalid character : ",ch

	# Now check the others

		if invalid != 1:
			imm, idd, iyyyy = int(mm), int(dd), int(yyyy)
			
			if len(inputDate) != 10:
				print "Wrong length - 10 chars only"
				invalid = 1
			elif string.count(inputDate,"/") != 2:
				print "Must have two slashes"
				invalid = 1
			elif imm < 1 or imm > 12:
				print "Invalid month (1-12)"
				invalid = 1
			elif idd <1 or idd > 31:
				print "Invalid day (1-31)"
				invalid = 1
				
	# End of validation routine
	# If we get here the field is valid
	
	
	# First way - difficult to read

	#splitDate = string.split(inputDate, "/")

	#print "The date is",splitDate[1],months[int(splitDate[0])-1],",",splitDate[2]

	#Second way - easier to read

	if idd==1 or idd==21 or idd==31:
		dd=str(idd)
		dd=dd+"st of"
	elif idd==2 or idd==22:
		dd=str(idd)
		dd=dd+"nd of"
	elif idd==3 or idd==23:
		dd=str(idd)
		dd=dd+"rd of"
	else:
		dd=str(idd)
		dd=dd+"th of"

	mm=months[imm-1]

	eudate=[dd, mm, yyyy]

	eudate=string.join(eudate)

	print "The date is the", eudate+"."
	
	return inputDate
