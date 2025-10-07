# Here I'll be testing the functions for mean, median, and standard deviation

# python -m unittest discover -s test

import sys

sys.path.append('src')  # noqa

import unittest
import random
import numpy as np
import my_utils
import string


class TestMean(unittest.TestCase):

    def test_mean_calcs(self):
        self.assertEqual(my_utils.mean([1, 2, 3, 4, 5]), 3)
        # tests to see if the mean of 1-5 is 3
        self.assertEqual(my_utils.mean([10, 20, 30, 40, 50]), 30)

    def test_mean_calcs_randints(self):
        for i in range(1000):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            d = random.randint(-100, 100)
            e = random.randint(-100, 100)

            self.assertTrue(
                my_utils.mean([a, b, c, d, e]) <= max([a, b, c, d, e]))
            self.assertTrue(
                my_utils.mean([a, b, c, d, e]) >= min([a, b, c, d, e]))
        # compare the mean of any random 5 numbers with the min and max
        # the mean should be >= min and <= max

    def test_mean_calc_numpy(self):
        for i in range(1000):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            d = random.randint(-100, 100)
            e = random.randint(-100, 100)

            self.assertAlmostEqual(
                my_utils.mean([a, b, c, d, e]),
                np.average([a, b, c, d, e]))
        # compare my mean function with numpy's average

    def test_mean_calc_errors(self):
        self.assertRaises(TypeError, my_utils.mean,
                          ["string", "non_number", True])
        self.assertRaises(TypeError, my_utils.mean,
                          [1, 2, 3, 4,
                           random.choices(string.ascii_letters, k=10)])
        # raise error because mean can't be calculated on strings


class TestMedian(unittest.TestCase):

    def test_median_calcs(self):
        self.assertEqual(my_utils.median([1, 2, 3, 4, 5]), 3)
        # tests to see if median of 1-5 is 3
        self.assertEqual(my_utils.median([10, 20, 30, 40, 50]), 30)
        self.assertEqual(my_utils.median([-3, 8, 13, 16, 999]), 13)

    def test_median_calcs_randints(self):
        for i in range(1000):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            d = random.randint(-100, 100)
            e = random.randint(-100, 100)

            self.assertTrue(
                my_utils.median([a, b, c, d, e]) <= max([a, b, c, d, e]))
            self.assertTrue(
                my_utils.median([a, b, c, d, e]) >= min([a, b, c, d, e]))
        # median of 5 random integers >= min and <= max

    def test_median_calc_numpy(self):
        for i in range(1000):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            d = random.randint(-100, 100)
            e = random.randint(-100, 100)

            self.assertAlmostEqual(
                my_utils.median([a, b, c, d, e]),
                np.median([a, b, c, d, e]))
        # compare median function with numpy median

    def test_median_calc_errors(self):
        self.assertRaises(TypeError, my_utils.median,
                          ["string", "non_number", True])
        self.assertRaises(TypeError, my_utils.median,
                          [1, 2, 3, 4,
                           random.choices(string.ascii_letters, k=10)])
        # raise error because median can't be calculated on strings


class TestStandardDeviation(unittest.TestCase):

    def test_std_dev_calcs(self):
        self.assertAlmostEqual(my_utils.stdev([1, 2, 3, 4, 5, 6, 7]), 2)
        self.assertAlmostEqual(my_utils.stdev([2, 4, 6, 8, 10, 12, 14]), 4)

    def test_std_dev_rand_ints(self):
        for i in range(1000):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            d = random.randint(-100, 100)
            e = random.randint(-100, 100)

            # the standard deviation should be >= 0
            self.assertTrue(my_utils.stdev([a, b, c, d, e]) >= 0)

    def test_std_dev_numpy(self):
        for i in range(1000):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            d = random.randint(-100, 100)
            e = random.randint(-100, 100)

            self.assertAlmostEqual(
                my_utils.stdev([a, b, c, d, e]),
                np.std([a, b, c, d, e]))


if __name__ == '__main__':
    unittest.main()
