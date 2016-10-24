import numpy as np
import matplotlib.colors as colors
import unittest
import sys

class TestColorMethods(unittest.TestCase):
	color = None
	expectedRGBA = None
	
	def test_to_rgba(self):		
		
		self.assertEqual(str(colors.to_rgba(self.color)), self.expectedRGBA)
		

if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestColorMethods.color = sys.argv.pop()
		TestColorMethods.expectedRGBA = sys.argv.pop()
        	
	unittest.main()
