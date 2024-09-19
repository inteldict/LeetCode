"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21



Constraints:

    -231 <= x <= 231 - 1
"""

import unittest


class TestReverse(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:

        Input: x = 123
        Output: 321
        """
        x = 123
        y = 321
        self.assertEqual(y, self.solution.reverse(x))

    def test_example_2(self):
        """
        Example 2:
        """
        x = -123
        y = -321
        self.assertEqual(y, self.solution.reverse(x))

    def test_example_3(self):
        """
        Example 3:

        Input: x = 120
        Output: 21
        """
        x = 120
        y = 21
        self.assertEqual(y, self.solution.reverse(x))

    def test_example_4(self):
        """
        Example 4:

        Input: x = 120
        Output: 21
        """
        x = 1534236469
        y = 0
        self.assertEqual(y, self.solution.reverse(x))


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        result = 0
        while x:
            x, res = divmod(x, 10)
            result = result * 10 + res

        # max = 2147483647  # 2 ** 31 - 1
        # min = -2147483648  # -2 ** 31
        result *= sign
        return 0 if result < -2147483648 or result > 2147483647 else result
