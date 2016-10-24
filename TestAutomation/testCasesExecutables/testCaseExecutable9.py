import numpy as np
import matplotlib.dates as dates
import unittest
import sys

class TestDatesMethods(unittest.TestCase):
	days = None
	expectedDate = None
	
	def test_num2epoch(self):	
		x = self.days		
		self.assertEqual(str(dates.num2epoch(int(x))), self.expectedDate)
		

if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestDatesMethods.days = sys.argv.pop()
		TestDatesMethods.expectedDate = sys.argv.pop()
        	
	unittest.main()
