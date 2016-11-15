import numpy as np
import matplotlib.dates as dates
import unittest
import sys

class TestDatesMethods(unittest.TestCase):
	
	seconds = None
	expectedDays = None
	
	def test_seconds(self):
		
		self.assertEqual(dates.seconds(self.seconds),float(self.expectedDays))


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestDatesMethods.seconds = sys.argv.pop()
		TestDatesMethods.expectedDays = sys.argv.pop()
	
unittest.main()
