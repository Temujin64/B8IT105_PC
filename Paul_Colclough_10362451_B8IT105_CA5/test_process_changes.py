#This imports a library used for testing the functions.
import unittest as ut
import process_changes as pc

class TestCalculations(ut.TestCase):
#I wanted to test the input validation functions but couldn't since the input was within the function as opposed to an argument.
	
	#This tests the addition calculation.		
	def testfind_between(self):
		self.assertEqual('test', pc.find_between('|test:','|',':'))

#This ensures that the class methods are only being used if this program is running them.
#i.e. These methods can't be called from another program by importing this file as a library.
if __name__ == '__main__':
	ut.main()
	


