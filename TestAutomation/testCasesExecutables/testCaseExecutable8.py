import numpy as np
import matplotlib.dates as dates
import unittest
import sys

class TestDatesMethods(unittest.TestCase):
	days = None
	expectedDate = None
	
	def test_date2num(self):
			
		x = dates.num2date(self.days)
		self.assertEqual(str(dates.date2num(x)), self.expectedDate)
		

if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestDatesMethods.days = sys.argv.pop()
		TestDatesMethods.expectedDate = sys.argv.pop()
        	
	unittest.main()
