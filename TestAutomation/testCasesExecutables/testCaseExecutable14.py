import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys

class TestLineMethods(unittest.TestCase):
	
	edge = None
	expectedEdge = None
	
	def setUp(self):
		line, = plt.plot([1,2,3,4])

	
	def test_set_line_edge_color(self):
		line, = plt.plot([1,2,3,4])
		line.set_markeredgecolor(self.edge)

		self.assertEqual(line.get_markeredgecolor(),self.expectedEdge)


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestLineMethods.edge = sys.argv.pop()
		TestLineMethods.expectedEdge = sys.argv.pop()
	
	unittest.main()
