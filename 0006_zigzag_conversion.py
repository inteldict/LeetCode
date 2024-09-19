"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000


"""
import unittest


class TestConversion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        s = "PAYPALISHIRING"
        numRows = 3
        expected_output = "PAHNAPLSIIGYIR"
        self.assertEqual(expected_output, self.solution.convert(s, numRows))

    def test_example_2(self):
        """
        Example 2:
        Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        """
        s = "PAYPALISHIRING"
        numRows = 4
        expected_output = "PINALSIGYAHRPI"
        self.assertEqual(expected_output, self.solution.convert(s, numRows))

    def test_example_3(self):
        """
        Example 3:
        Input: s = "A", numRows = 1
        Output: "A"
        """
        s = "A"
        numRows = 1
        expected_output = "A"
        self.assertEqual(expected_output, self.solution.convert(s, numRows))


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         rows = [[] for _ in range(numRows)]
#         i = 0
#         while i < len(s):
#             for j in range(numRows):
#                 if i >= len(s):
#                     break
#                 rows[j].append(s[i])
#                 i += 1
#
#             for j in range(numRows - 2, 0, -1):
#                 if i >= len(s):
#                     break
#                 rows[j].append(s[i])
#                 i += 1
#
#
#         return "".join("".join(row) for row in rows)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Initialize an array of strings to hold characters for each row
        rows = [''] * numRows

        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char
            # Change direction at the top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            # Change row
            curr_row += 1 if going_down else -1

        return ''.join(rows)
