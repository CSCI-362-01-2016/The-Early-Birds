import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys

class TestLineMethods(unittest.TestCase):
	#color = None
	width = None
	#expectedColor = 'red'
	expectedWidth = None
	
	def setUp(self):
		line, = plt.plot([1,2,3,4])

	
	"""def test_line_color(self):
		line, = plt.plot([1,2,3,4])
		line.set_color(self.color)
		#line.set_linewidth(5)
		self.assertEqual(line.get_color(),self.color)"""

	def test_line_width(self):
		line, = plt.plot([1,2,3,4])
		#line.set_color('red')
		#line, = plt.plot([1,2,3,4])
		line.set_linewidth(self.width)
		temp = line.get_linewidth()
		self.assertEqual(int(temp),int(self.expectedWidth))


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	#TestLineMethods.color = sys.argv.pop()
        	TestLineMethods.width = sys.argv.pop()
		TestLineMethods.expectedWidth = sys.argv.pop()
	
	unittest.main()
