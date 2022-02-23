import unittest

from leet_code import removedups
from leet_code import convert
from leet_code import maxArea


class testRemovedups(unittest.TestCase):
    def test_ordered_array(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        output = removedups(nums)

        self.assertEqual(output, (5, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]))

class testConvert(unittest.TestCase):
    def test_convert_string(self):
        s = "PAYPALISHIRING"
        rows = 3
        output = convert(s,rows)

        self.assertEqual(output,'PAHNAPLSIIGYIR')

class testMaxArea(unittest.TestCase):
    def test_maxArea_array(self):
        height = [4,3,2,1,4]
        output = maxArea(height)

        self.assertEqual(output, 16)
        
if __name__ == '__main__':
    unittest.main()
