import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys
import matplotlib.dates as dates
import datetime
import matplotlib

class TestLineMethods(unittest.TestCase):
	
	seconds = None
	expected_days = None
	
	def setUp(self):
		line, = plt.plot([1,2,3,4])

	
	def test_matplotlib_dates_seconds(self):
		
		
		self.assertEqual(float(self.expected_days),float(matplotlib.dates.seconds(self.seconds)))

	"""def test_line_width(self):
		#line, = plt.plot([1,2,3,4])
		#line.set_color('red')
		line, = plt.plot([1,2,3,4])
		line.set_linewidth(self.width)
		self.assertEqual(int(line.get_linewidth()),int(self.width))"""


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestLineMethods.seconds = sys.argv.pop()
		TestLineMethods.expected_days = sys.argv.pop()
        	#TestLineMethods.width = sys.argv.pop()
	unittest.main()
