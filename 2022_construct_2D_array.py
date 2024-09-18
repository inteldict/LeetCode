"""
2022. Convert 1D Array Into 2D Array
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.



Example 1:

Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

Example 2:

Input: original = [1,2,3], m = 1, n = 3
Output: [[1,2,3]]
Explanation: The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.

Example 3:

Input: original = [1,2], m = 1, n = 1
Output: []
Explanation: There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.



Constraints:

    1 <= original.length <= 5 * 104
    1 <= original[i] <= 105
    1 <= m, n <= 4 * 104


"""
import json
import sys
import unittest
from typing import List


class TestArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        inp = [1, 2, 3, 4]
        m = 2
        n = 2
        expected_output = [[1, 2], [3, 4]]
        self.assertEqual(expected_output, self.solution.construct2DArray(inp, m, n))

    def test_example_2(self):
        inp = [1, 2, 3]
        m = 1
        n = 3
        expected_output = [[1, 2, 3]]
        self.assertEqual(expected_output, self.solution.construct2DArray(inp, m, n))

    def test_example_3(self):
        inp = [1, 2]
        m = 1
        n = 1
        expected_output = []
        self.assertEqual(expected_output, self.solution.construct2DArray(inp, m, n))


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        return [original[n * i:(i + 1) * n] for i in range(m)]


def format_output(result):
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'


def pplovrlkmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()

    num_test_cases = len(lines) // 3
    results = []

    for i in range(num_test_cases):
        original = json.loads(lines[i * 3])
        m = int(lines[i * 3 + 1])
        n = int(lines[i * 3 + 2])

        result = Solution().construct2DArray(original, m, n)
        formatted_result = format_output(result)
        results.append(formatted_result)

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")


if __name__ == "__main__":
    pplovrlkmain()
    exit(0)
