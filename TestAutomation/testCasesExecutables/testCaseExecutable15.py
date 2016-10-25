import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys

class TestLineMethods(unittest.TestCase):
	
	edge_width = None
	expectedEdge_width = None
	
	def setUp(self):
		line, = plt.plot([1,2,3,4])

	
	def test_set_line_edge_color(self):
		line, = plt.plot([1,2,3,4])
		line.set_markeredgewidth(self.edge_width)

		self.assertEqual(line.get_markeredgewidth(),self.expectedEdge_width)


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestLineMethods.edge_width = sys.argv.pop()
		TestLineMethods.expectedEdge_width = sys.argv.pop()
	
	unittest.main()
