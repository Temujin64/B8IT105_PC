import string

#months is a list used as a lookup table
months=['January','February','March','April','May','June','July','August','September','October','November','December']

invalid=1

while invalid==1:
	invalid=0
	usdate=raw_input("Please enter the date in the following format mm/dd/yyyy: ")
	mm,dd,yyyy=string.split(usdate,"/")
	for ch in usdate:
		if (ord(ch) < 47 or ord(ch) > 59):
			print "Invalid character selected: ",ch
			invalid=1
	if invalid !=1:
		imm,idd,iyyyy=int(mm),int(dd),int(yyyy)
	elif len(usdate)!=10:
		print "Wrong length, 10 characters only."
		invalid=1
	elif string.count(usdate, "/") != 2:
		print "Please yse / to seperate day, month and year."
	elif imm<1 or imm>12:
		print "Invalid number of months selected."
		invalid=1
	elif idd<1 or idd>31:
		print "Invalid number of months selected."
		invalid=1
		

	
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
