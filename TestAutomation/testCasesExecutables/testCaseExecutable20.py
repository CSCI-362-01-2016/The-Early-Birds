import numpy as np
import matplotlib.dates as dates
import unittest
import sys

class TestDatesMethods(unittest.TestCase):
    hours = None
    expectedDays = None
	
    def test_hours(self):	
				
        self.assertEqual(dates.hours(int(self.hours)), float(self.expectedDays))
		

if __name__=='__main__':
    #import sys
	
    if len(sys.argv) > 1:
        TestDatesMethods.hours = sys.argv.pop()
        TestDatesMethods.expectedDays = sys.argv.pop()
        	
    unittest.main()
