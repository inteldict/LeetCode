"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106


"""
import unittest
from idlelib.run import get_message_lines
from statistics import median
from typing import List


class TestTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_0(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(median(sorted(nums1 + nums2)), self.solution.findMedianSortedArrays(nums1, nums2))

    def test_example_1(self):
        nums1 = [1]
        nums2 = []
        expected_output = 1.00000
        self.assertEqual(expected_output, self.solution.findMedianSortedArrays(nums1, nums2))

    def test_example_2(self):
        nums1 = []
        nums2 = []
        expected_output = 0.00000
        self.assertEqual(expected_output, self.solution.findMedianSortedArrays(nums1, nums2))

    def test_example3(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected_output = 2.50000
        self.assertEqual(expected_output, self.solution.findMedianSortedArrays(nums1, nums2))

    def test_example4(self):
        nums1 = []
        nums2 = [2, 3]
        expected_output = (2 + 3) / 2.0
        self.assertEqual(expected_output, self.solution.findMedianSortedArrays(nums1, nums2))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    nums1, nums2 = nums2, nums1  # swap variables so nums1 < nums2
            else:  # edge case, we look for median in nums1
                return get_median(nums1)
        elif nums2:  # edge case, we look for median in nums2
            return get_median(nums2)
        else:
            return 0.0  # edge case: both arrays are empty

        # both arrays are not empty

        # total_len = len(nums1) + len(nums2)
        # do_average = total_len % 2 == 0
        # median_ind = total_len // 2
        #
        # n1s = 0, n1e = len(nums1)
        # n2s = 0, n2e = len(nums2)
        # i1 = len(nums1) - 1
        # i = i1
        # i2 = 0
        # while True:
        #     if nums1[i1] < nums2[i2]:
        #
        #     else:

        return get_median(sorted(nums1 + nums2))


def get_median(arr: List[int]) -> float:
    total_len = len(arr)
    median_ind = total_len // 2
    if total_len % 2 == 0:
        return (arr[median_ind - 1] + arr[median_ind]) / 2.0
    else:
        return arr[median_ind]

# TODO try to understand this

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         a, b = nums1, nums2
#         total = len(a) + len(b)
#         half = total // 2
#
#         if len(a) > len(b):
#             a, b = b, a
#
#         l, r = 0, len(a) - 1
#         while True:
#             i = (l + r) >> 1
#             j = half - i - 2
#
#             al = a[i] if i >= 0 else -inf
#             ar = a[i + 1] if i + 1 < len(a) else inf
#
#             bl = b[j] if j >= 0 else -inf
#             br = b[j + 1] if j + 1 < len(b) else inf
#
#             if al <= br and bl <= ar:
#                 if total & 1:
#                     return min(ar, br)
#                 else:
#                     return 0.5 * (min(ar, br) + max(al, bl))
#             elif al > br:
#                 r = i - 1
#             else:
#                 l = i + 1
