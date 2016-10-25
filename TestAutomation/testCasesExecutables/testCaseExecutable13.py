import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys

class TestLineMethods(unittest.TestCase):
	
	style = None
	expectedStyle = None
	
	def setUp(self):
		line, = plt.plot([1,2,3,4])

	
	def test_set_line_style(self):
		line, = plt.plot([1,2,3,4])
		line.set_linestyle(self.style)

		#print "hello!!@@@@" + line.get_linestyle()
		self.assertEqual(line.get_linestyle(),self.expectedStyle)


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestLineMethods.style = sys.argv.pop()
		TestLineMethods.expectedStyle = sys.argv.pop()
	
	unittest.main()
