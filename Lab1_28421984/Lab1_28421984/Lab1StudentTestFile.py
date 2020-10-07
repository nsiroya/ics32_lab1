import unittest
import Lab1_28421984 as test

class Test_Lab1StudentTestFile(unittest.TestCase):
	def test1(self):        
		self.assertEqual(test.isValid(13, 3, 2019), False)
		self.assertEqual(test.isValid(9, 26, 2019), True)
	def test2(self):
		self.assertEqual(test.isLeapYear(2019), False)        
		self.assertEqual(test.isLeapYear(2020), True)    
	def test3(self):        
		self.assertEqual(test.isValidMonth(0), False)        
		self.assertEqual(test.isValidMonth(2), True)    
	def test4(self):        
		self.assertEqual(test.getDayOfWeek(9, 26, 2019), 'Thursday')  
		self.assertEqual(test.getDayOfWeek(1, 29, 2019), 'Tuesday')
		self.assertEqual(test.getDayOfWeek(1, 30, 2019), 'Wednesday')
		self.assertEqual(test.getDayOfWeek(1, 31, 2019), 'Thursday')
		self.assertEqual(test.getDayOfWeek(1, 29, 2020), 'Wednesday')
		self.assertEqual(test.getDayOfWeek(1, 30, 2020), 'Thursday')
		self.assertEqual(test.getDayOfWeek(1, 31, 2020), 'Friday')
		self.assertEqual(test.getDayOfWeek(2, 28, 2019), 'Thursday')
		self.assertEqual(test.getDayOfWeek(2, 28, 2020), 'Friday')
		self.assertEqual(test.getDayOfWeek(2, 29, 2020), 'Saturday')
		self.assertEqual(test.getDayOfWeek(3, 1, 2019), 'Friday')
		self.assertEqual(test.getDayOfWeek(3, 1, 2020), 'Sunday')
	def test5(self):        
		self.assertEqual(test.getThanksgivingDate(2019), 28)

if __name__ == '__main__':
    unittest.main()


#import unittest
# You must import your script name (ex: Lab1_12345678), no file extension, followed by 'as test'
# example: import Lab1_12345678 as test

#class Test_Lab1StudentTestFile(unittest.TestCase):  
#	def test1(self):        
#		self.assertEqual(test.isValid(13, 3, 2019), False)   
#		self.assertEqual(test.isValid(9, 26, 2019), True)    
#	def test2(self):        
#		self.assertEqual(test.isLeapYear(2019), False)        
#		self.assertEqual(test.isLeapYear(2020), True)    
#	def test3(self):        
#		self.assertEqual(test.isValidMonth(0), False)        
#		self.assertEqual(test.isValidMonth(2), True)    
#	def test4(self):        
#		self.assertEqual(test.getDayOfWeek(9, 26, 2019), 'Thursday')    
#	def test5(self):        
#		self.assertEqual(test.getThanksgivingDate(2019), 28)
	
#if __name__ == "__main__":    
#	unittest.main()
