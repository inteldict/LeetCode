"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1



Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""
import unittest
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        out = 49
        self.assertEqual(out, self.solution.maxArea(height))

    def test_2(self):
        height = [1, 1]
        out = 1
        self.assertEqual(out, self.solution.maxArea(height))


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0  # left index to the beginning of array
        j = len(height) - 1  # right index to the end of array
        max_area = 0
        while i < j:  # while lines do not meet
            if height[i] <= height[j]:  # choose the least tall line
                area = height[i] * (j - i)  # area is calculated by shortest of two lines x distance
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            if area > max_area: # check if a new max_area is found
                max_area = area
        return max_area

# This version minimizes execution runtime
# def maxArea(height: List[int]) -> int:
#     i = 0
#     j = len(height) - 1
#     max_area = 0
#     while i < j:
#         if height[i] <= height[j]:
#             area = height[i] * (j - i)
#             i += 1
#         else:
#             area = height[j] * (j - i)
#             j -= 1
#         if area > max_area:
#             max_area = area
#     return max_area
#
# f = open('user.out', 'w')
# for case in map(loads, stdin):
#     f.write(f"{maxArea(case)}\n")
# f.flush()
# exit(0)