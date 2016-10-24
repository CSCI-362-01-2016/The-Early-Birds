import numpy as np
import matplotlib.colors as colors
import unittest
import sys

class TestColorMethods(unittest.TestCase):
	color = None
	expectedBoolean = None
	
	def test_is_color_like(self):		
		
		self.assertEqual(str(colors.is_color_like(self.color)), self.expectedBoolean)
		

if __name__=='__main__':
	#import sys
	
	if len(sys.argv) > 1:
        	TestColorMethods.color = sys.argv.pop()
		TestColorMethods.expectedBoolean = sys.argv.pop()
        	
	unittest.main()
