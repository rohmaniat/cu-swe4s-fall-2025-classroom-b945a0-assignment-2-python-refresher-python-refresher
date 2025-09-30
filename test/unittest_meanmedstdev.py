# Here I'll be testing the functions for mean, median, and standard deviation

import sys

sys.path.append('src/') # noqa

import unittest
import random
import numpy as np
import my_utils

print sys.path 

class TestMean(unittest.TestCase):
	
	def MeanCalcs(self):
		self.assertEqual (my_utils.mean(1, 2, 3, 4, 5), 3)
		# tests to see if the mean of 1-5 is 3
		self.assertEqual (my_utils.mean(10, 20, 30, 40, 50), 30)
		
    def MeanCalcsRandints(self):
		for i in range(1000):
            a = random.randint(1,100)
	        b = random.randint(1,100)
            c = random.randint(1,100)
            d = random.randint(1,100)
            e = random.randint(1,100)
	
        self.assertTrue(my_utils.mean(a,b,c,d,e) <= max(a,b,c,d,e))
	    self.assertTrue(my_utils.mean(a,b,c,d,e) >= min(a,b,c,d,e))
        # compare the mean of any random 5 numbers with the min and the max
		# the mean should be greater than or equal to the min and less than or equal to the max
			
    def MeanCalcNumpy(self):
        for i in range(1000):
            a = random.randint(1,100)
	        b = random.randint(1,100)
            c = random.randint(1,100)
            d = random.randint(1,100)
            e = random.randint(1,100)

        self.assertAlmostEqual(my_utils.mean(a,b,c,d,e), np.average(a,b,c,d,e))
            # compare my mean function with the one in the numpy library
			
class TestMedian(unittest.TestCase):
	
    def MedianCalcEasy(self):
	
	
if __name__ == '__main__':
    unittest.main()
	