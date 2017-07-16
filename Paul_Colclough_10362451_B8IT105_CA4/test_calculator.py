#This imports a library used for testing the functions.
import unittest as ut
import calculator as cl

class TestCalculations(ut.TestCase):
#I wanted to test the input validation functions but couldn't since the input was within the function as opposed to an argument.
	
	#This tests the addition calculation.		
	def testaddit(self):
		self.assertEqual(12, cl.addit(8,4))

	#This tests the subtraction calculation.		
	def testsubit(self):
		self.assertEqual(4, cl.subit(8,4))

	#This tests the multiplication calculation.				
	def testmultit(self):
		self.assertEqual(32, cl.multit(8,4))

	#This tests the division calculation.				
	def testdivit(self):
		self.assertEqual(2.5, cl.divit(10,4))

	#This tests the exponentiation calculation.		
	def testexpit(self):
		self.assertEqual(4096, cl.expit(8,4))

	#This tests the factorisation calculation.			
	def testfactit(self):
		self.assertEqual(1, cl.factit(0))
		self.assertEqual(1, cl.factit(1))
		self.assertEqual(120, cl.factit(5))
		self.assertEqual(720, cl.factit(6))
		self.assertEqual(3628800, cl.factit(10))

	#This tests the combinations rule calculation.		
	def testcombit(self):
		self.assertEqual(15, cl.combit(6,4))

	#This tests the average	calculation.		
	def testavit(self):
		self.assertEqual(11.25, cl.avit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0]))

	#This tests the variance calculation.
	#Once for sample and once for population but using the same dataset.
	def testvarit(self):
		self.assertEqual(2.7857142857142856, cl.varit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=True))
		self.assertEqual(2.4375, cl.varit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=False))

	#This tests the standard deviation calculation.	
	#Once for sample and once for population but using the same dataset.
	def testsdevit(self):
		self.assertEqual(1.6690459207925603, cl.sdevit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=True))
		self.assertEqual(1.5612494995995996, cl.sdevit([10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0], sample=False))
	
	def testminit(self):
		self.assertEqual(2, cl.minit([2,5,6, 7, 7, 10]))
	
	def testmaxit(self):
		self.assertEqual(10, cl.maxit([2,5,6, 7, 7, 10]))
	
	def testprimeit(self):
		self.assertEqual([2, 3, 5, 7], cl.primeit(2,10))

#This ensures that the class methods are only being used if this program is running them.
#i.e. These methods can't be called from another program by importing this file as a library.
if __name__ == '__main__':
	ut.main()
	


