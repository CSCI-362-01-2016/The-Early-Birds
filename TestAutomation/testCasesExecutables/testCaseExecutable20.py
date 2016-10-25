s np
import matplotlib.colors as colors
import unittest
import sys

class TestColorMethods(unittest.TestCase):
    color = None
    expectedHex = None
	
    def test_to_hex(self):
				
        self.assertEqual(colors.to_hex(self.color), self.expectedHex)
		

if __name__=='__main__':
    #import sys
	
    if len(sys.argv) > 1:
        TestColorMethods.color = sys.argv.pop()
        TestColorMethods.expectedHex = sys.argv.pop()
        	
    unittest.main()
