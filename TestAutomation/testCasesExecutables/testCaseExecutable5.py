import numpy as np
import matplotlib.colors as colors
import unittest
import sys

class TestColorMethods(unittest.TestCase):
	color = None
	expectedRGB = None
	
	def test_hex2color(self):		
		
		self.assertEqual(str(colors.hex2color(self.color)), self.expectedRGBA)
		

if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestColorMethods.color = sys.argv.pop()
		TestColorMethods.expectedRGBA = sys.argv.pop()
        	
	unittest.main()
