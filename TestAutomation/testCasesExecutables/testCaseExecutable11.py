import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys

class TestLineMethods(unittest.TestCase):
	color = None
	#width = None
	expectedColor = None
	#expectedWidth = 5
	
	def setUp(self):
		line, = plt.plot([1,2,3,4])

	
	def test_get_line_color(self):
		line, = plt.plot([1,2,3,4])
		line.set_color(self.color)
		#line.set_linewidth(5)
		temp = line.get_color()
		self.assertEqual(temp,self.expectedColor)

	"""def test_line_width(self):
		#line, = plt.plot([1,2,3,4])
		#line.set_color('red')
		line, = plt.plot([1,2,3,4])
		line.set_linewidth(self.width)
		self.assertEqual(int(line.get_linewidth()),int(self.width))"""


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestLineMethods.color = sys.argv.pop()
		TestLineMethods.expectedColor = sys.argv.pop()
        	#TestLineMethods.width = sys.argv.pop()
	unittest.main()
