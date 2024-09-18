"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.



Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:

Input: n = 1
Output: 0

Test Cases:
69
1
1000
911
12
267
677
128


Constraints:

    1 <= n <= 1000



"""
import unittest


class TestMaxPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        n = 3
        expected_output = 3
        self.assertEqual(expected_output, self.solution.minSteps(n))

    def test_example_2(self):
        n = 1
        expected_output = 0
        self.assertEqual(expected_output, self.solution.minSteps(n))

    def test_example_3(self):
        n = 1000
        expected_output = 21
        self.assertEqual(expected_output, self.solution.minSteps(n))


class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
        return steps
