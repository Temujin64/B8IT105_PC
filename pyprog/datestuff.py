# datestuff.py
#
# Input the date as American format mm/dd/yyyy
#
#	eg 09/14/2017
#
# Output the date as dd monthname, year
#
#	eg 14 September, 2017
#

import string
import datevalidation as dv

#Now run the code
def main():
	dob = dv.GetAndValidateDate("Please enter birthdy: ")
	dol = dv.GetAndValidateDate("PLease enter leaving date: ")
	doa = dv.GetAndValidateDate("Please enter anniversary date: ")
	
	print "Returned values ",dob,dol,doa

main()


