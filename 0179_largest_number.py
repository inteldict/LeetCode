import unittest
from functools import cmp_to_key
from typing import List


class TestLargestNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        nums = [10, 2]
        expected_output = "210"
        self.assertEqual(expected_output, self.solution.largestNumber(nums))

    def test_example_2(self):
        """
        Example 2:
        """

        nums = [3, 30, 34, 5, 9]
        expected_output = "9534330"
        self.assertEqual(expected_output, self.solution.largestNumber(nums))

    def test_example_3(self):
        """
        Example 3:
        """
        nums = [34323, 3432]
        expected_output = "343234323"
        self.assertEqual(expected_output, self.solution.largestNumber(nums))

    def test_example_4(self):
        """
        Example 3:
        """
        nums = [34321, 3432]
        expected_output = "343234321"
        self.assertEqual(expected_output, self.solution.largestNumber(nums))


# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         if not nums:
#             return '0'
#         nums_str = [str(num) for num in nums]
#         result = ''.join(sorted(nums_str, key=cmp_to_key(reverse_compare)))
#         if result[0] == '0':
#             return '0'
#         return result
#
#
# def reverse_compare(num1, num2):
#     num1_len = len(num1)
#     num2_len = len(num2)
#     min_len = min(num1_len, num2_len)
#
#     for i in range(min_len):
#         if num1[i] > num2[i]:
#             return -1
#         elif num1[i] < num2[i]:
#             return 1
#
#     if num1_len == num2_len:
#         return 0
#
#     num1num2 = num1 + num2
#     num2num1 = num2 + num1
#
#     for i in range(min_len, num1_len + num2_len):
#         if num1num2[i] > num2num1[i]:
#             return -1
#         elif num1num2[i] < num2num1[i]:
#             return 1
#
#     return 0
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def reverse_compare(num1, num2):
            a = int(num1 + num2)
            b = int(num2 + num1)
            if a > b:
                return -1
            if b > a:
                return 1
            return 0

        nums = sorted(nums, key=cmp_to_key(reverse_compare))
        res = "".join(nums)
        if res[0] == '0':
            return '0'
        return res
