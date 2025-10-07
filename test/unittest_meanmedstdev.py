# Here I'll be testing the functions for mean, median, and standard deviation

# python -m unittest test/unittest_meanmedstdev

import sys

sys.path.append('src') # noqa

import unittest
import random
import numpy as np
import my_utils
import string

print(sys.path)

class TestMean(unittest.TestCase):
	
    def MeanCalcs(self):

        self.assertEqual (my_utils.mean(1, 2, 3, 4, 5), 3)
		# tests to see if the mean of 1-5 is 3
        self.assertEqual (my_utils.mean(10, 20, 30, 40, 50), 30)
        
    def MeanCalcsRandints(self):

        for i in range(1000):
            a = random.randint(-100,100)
            b = random.randint(-100,100)
            c = random.randint(-100,100)
            d = random.randint(-100,100)
            e = random.randint(-100,100)
	
            self.assertTrue(my_utils.mean(a,b,c,d,e) <= max(a,b,c,d,e))
            self.assertTrue(my_utils.mean(a,b,c,d,e) >= min(a,b,c,d,e))
        # compare the mean of any random 5 numbers with the min and the max
		# the mean should be greater than or equal to the min 
        # and less than or equal to the max
			
    def MeanCalcNumpy(self):

        for i in range(1000):
            a = random.randint(-100,100)
            b = random.randint(-100,100)
            c = random.randint(-100,100)
            d = random.randint(-100,100)
            e = random.randint(-100,100)

            self.assertAlmostEqual(my_utils.mean(a,b,c,d,e), np.average(a,b,c,d,e))
            # compare my mean function with the one in the numpy library

    def MeanCalcErrors(self):

        self.assertRaises(TypeError, my_utils.mean("string", "non_number", True))
        self.assertRaises(TypeError, my_utils.mean(1, 2, 3, 4, random.choices(string.ascii_letters, k=10)))
        # will raise an error because you can't calculate the mean of a string
			
class TestMedian(unittest.TestCase):
	
    def MedianCalcs(self):

        self.assertEqual (my_utils.median(1, 2, 3, 4, 5), 3)
		# tests to see if the median of 1-5 is 3
        self.assertEqual (my_utils.median(10, 20, 30, 40, 50), 30)
        self.assertEqual (my_utils.median(-3, 8, 13, 16, 999), 13)

    def MedianCalcsRandints(self):

        for i in range(1000):
            a = random.randint(-100,100)
            b = random.randint(-100,100)
            c = random.randint(-100,100)
            d = random.randint(-100,100)
            e = random.randint(-100,100)
	
            self.assertTrue(my_utils.median(a,b,c,d,e) <= max(a,b,c,d,e))
            self.assertTrue(my_utils.median(a,b,c,d,e) >= min(a,b,c,d,e))
        # compare the median of any random 5 numbers with the min and the max
		# the median should also be greater than or equal to the min 
        # and less than or equal to the max

    def MedianCalcNumpy(self):

        # compare my median function with numpy
        for i in range(1000):
            a = random.randint(-100,100)
            b = random.randint(-100,100)
            c = random.randint(-100,100)
            d = random.randint(-100,100)
            e = random.randint(-100,100)

            self.assertAlmostEqual(my_utils.median(a,b,c,d,e), np.median(a,b,c,d,e))

    def MedianCalcErrors(self):
        self.assertRaises(TypeError, my_utils.median("string", "non_number", True))
        self.assertRaises(TypeError, my_utils.median(1, 2, 3, 4, random.choices(string.ascii_letters, k=10)))
        # will raise an error because you can't calculate the median of a string

class TestStandardDeviation(unittest.TestCase):

    def StdDevCalcs(self):

        self.assertAlmostEqual (my_utils.stdev(1, 2, 3, 4, 5, 6, 7), 2)
        self.assertAlmostEqual (my_utils.stdev(2, 4, 6, 8, 10, 12, 14), 4)

    def StdDevRandInts(self):

        for i in range(1000):
            a = random.randint(-100,100)
            b = random.randint(-100,100)
            c = random.randint(-100,100)
            d = random.randint(-100,100)
            e = random.randint(-100,100)
	
            # the standard deviation should be greater than or equal to zero
            self.assertTrue(my_utils.stdev(a,b,c,d,e) >= 0)

    def StdDevNumpy(self):
        
        for i in range(1000):
            a = random.randint(-100,100)
            b = random.randint(-100,100)
            c = random.randint(-100,100)
            d = random.randint(-100,100)
            e = random.randint(-100,100)

            self.assertAlmostEqual(my_utils.stdev(a,b,c,d,e), np.std(a,b,c,d,e))

if __name__ == '__main__':
    unittest.main()
	