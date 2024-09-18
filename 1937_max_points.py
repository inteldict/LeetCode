"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

    x for x >= 0.
    -x for x < 0.

Example 1:

Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.

Example 2:

Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.

Constraints:

    m == points.length
    n == points[r].length
    1 <= m, n <= 105
    1 <= m * n <= 105
    0 <= points[r][c] <= 105

Time Complexity $O(N*M)$
"""
import unittest
from typing import List


class TestMaxPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        inp = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
        expected_output = 9
        self.assertEqual(expected_output, self.solution.maxPoints(inp))

    def test_example_2(self):
        """
        Example 1:
        """
        inp = [[1, 5], [2, 3], [4, 2]]
        expected_output = 11
        self.assertEqual(expected_output, self.solution.maxPoints(inp))

    def test_example_3(self):
        """
        Example 1:
        """
        inp = [[1,5],[3,2],[4,2]]
        expected_output = 11
        self.assertEqual(expected_output, self.solution.maxPoints(inp))


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Get the number of rows (n) and columns (m)
        n = len(points)
        m = len(points[0])
        # copy first row of points
        total_points = points[0].copy()

        for i in range(n - 1):
            # Store the max points for the current row
            row_points = [total_points[0]]

            # Calculate maximum points up to each column j
            for j in range(1, m):
                # Calculate the max points for the current column considering moving left
                row_points.append(max(row_points[-1] - 1, total_points[j]))

            # Adjust maximum points up to each column j
            for j in range(m - 2, -1, -1):
                # Update row_points[j] with the maximum considering moving right
                row_points[j] = max(row_points[j], row_points[j + 1] - 1)

            # maximum points for the current row plus the points of the next row
            for j in range(m):
                total_points[j] = row_points[j] + points[i + 1][j]

        return max(total_points)
