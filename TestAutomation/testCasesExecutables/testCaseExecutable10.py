import numpy as np
import matplotlib.dates as dates
import datetime
import unittest
import sys

class TestDatesMethods(unittest.TestCase):
	temp = None
	temp2 = None
	expectedValue = 735731.0416666666
	
	def test_drange(self):
		temp = self.temp
		temp2 = self.temp2
		temp = temp.split(" ")
		temp2 = temp2.split(" ")	
		x = datetime.datetime(int(temp[0]), int(temp[1]), int(temp[2]))
		y = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]))
		delta = datetime.timedelta(hours = 5)		
		self.assertEqual(dates.drange(x,y,delta)[5], self.expectedValue)
		

if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestDatesMethods.temp = sys.argv.pop()
		TestDatesMethods.temp2 = sys.argv.pop()	
		       	
	unittest.main()
