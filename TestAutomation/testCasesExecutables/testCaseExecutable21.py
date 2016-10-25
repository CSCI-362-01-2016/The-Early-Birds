import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import unittest
import sys

class TestLineMethods(unittest.TestCase):
    color = None
	
    expectedColor = None
	
	
    def setUp(self):
        line, = plt.plot([1,2,3,4])

	
    def test_get_line_color(self):
        line, = plt.plot([1,2,3,4])
        line.set_color(self.color)
        temp = line.get_color()
        self.assertEqual(temp,self.expectedColor)

	

if __name__=='__main__':
    #import sys
    if len(sys.argv) > 1:
        TestLineMethods.color = sys.argv.pop()
        TestLineMethods.expectedColor = sys.argv.pop()
        	
unittest.main()
