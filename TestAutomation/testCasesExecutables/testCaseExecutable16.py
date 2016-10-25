import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys

class TestLineMethods(unittest.TestCase):
	
	marker_size = None
	expected_marker_size = None
	
	def setUp(self):
		line, = plt.plot([1,2,3,4])

	
	def test_line_update_from(self):
		line, = plt.plot([1,2,3,4])
		line.set_markersize(self.marker_size)
		

		self.assertEqual(int(line.get_markersize()),int(self.expected_marker_size))


if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestLineMethods.marker_size = sys.argv.pop()
		TestLineMethods.expected_marker_size = sys.argv.pop()
	
	unittest.main()
