"""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

Constraints:

    m == arrays.length
    2 <= m <= 105
    1 <= arrays[i].length <= 500
    -104 <= arrays[i][j] <= 104
    arrays[i] is sorted in ascending order.
    There will be at most 105 integers in all the arrays.
"""
import unittest
from typing import List


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:

        Input: arrays = [[1,2,3],[4,5],[1,2,3]]
        Output: 4
        Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
        """
        inp = [[1, 2, 3], [4, 5], [1, 2, 3]]
        expected_output = 4
        self.assertEqual(expected_output, self.solution.maxDistance(inp))

    def test_example_2(self):
        """
        Example 2:
        Input: arrays = [[1],[1]]
        Output: 0
        """
        inp = [[1], [1]]
        expected_output = 0
        self.assertEqual(expected_output, self.solution.maxDistance(inp))

    def test_example_3(self):
        """
        Example 3:
        Output: 0
        """
        inp = [[1, 2], [3, 4], [5, 6]]
        expected_output = 5
        self.assertEqual(expected_output, self.solution.maxDistance(inp))

    def test_example_4(self):
        inp = [[1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1],
               [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2], [1], [2],
               [1], [2], [1]]
        expected_output = 1
        self.assertEqual(expected_output, self.solution.maxDistance(inp))

    def test_example_5(self):
        inp = [[3, 4], [1, 5], [2, 2]]
        expected_output = 3
        self.assertEqual(expected_output, self.solution.maxDistance(inp))

    def test_example_6(self):
        inp = [[1, 5], [3, 4]]
        expected_output = 3
        self.assertEqual(expected_output, self.solution.maxDistance(inp))

    def test_example_7(self):
        inp = [[-10,-9,-9,-3,-1,-1,0],[-5],[4],[-8],[-9,-6,-5,-4,-2,2,3],[-3,-3,-2,-1,0]]
        expected_output = 14
        self.assertEqual(expected_output, self.solution.maxDistance(inp))



class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize minimum and maximum using the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        # Iterate through the remaining arrays
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            # Calculate possible distances using current array's values with min and max from previous arrays
            max_distance = max(max_distance, current_max - min_val, max_val - current_min)

            # Update the overall min and max
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance
