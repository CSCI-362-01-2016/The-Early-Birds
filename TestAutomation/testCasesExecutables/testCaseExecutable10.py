import numpy as np
import matplotlib.dates as dates
import datetime
import unittest
import sys

class TestDatesMethods(unittest.TestCase):
	temp = None
	expectedValue = None
	
	def test_drange(self):
		temp = self.temp		
		temp = temp.split(" ")			
		x = datetime.datetime(int(temp[0]), int(temp[1]), int(temp[2]))
		y = datetime.datetime(int(temp[3]), int(temp[4]), int(temp[5]))
		delta = datetime.timedelta(hours = 5)		
		self.assertEqual(dates.drange(x,y,delta)[5], float(self.expectedValue))
		

if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestDatesMethods.temp = sys.argv.pop()
		TestDatesMethods.expectedValue = sys.argv.pop()	
		       	
	unittest.main()
