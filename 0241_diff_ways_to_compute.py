"""
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Constraints:

    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
    All the integer values in the input expression are in the range [0, 99].
    The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
"""
from functools import cache
from typing import List
import unittest


class TesIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        expression = "2-1-1"
        out = [0, 2]
        self.assertEqual(sorted(out), sorted(self.solution.diffWaysToCompute(expression)))

    def test_example_2(self):
        expression = "2*3-4*5"
        out = [-34, -14, -10, -10, 10]
        self.assertEqual(sorted(out), sorted(self.solution.diffWaysToCompute(expression)))

    # def test_example_3(self):
    #     expression = "2*3-4*5"
    #     out = [-34, -14, -10, -10, 10]
    #     self.assertEqual(out, self.solution.diffWaysToCompute(expression))


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = {'+', '-', '*'}

        @cache
        def recursiveCompute(expression) -> List[int]:
            if len(expression) == 0:
                return []

            if expression.isnumeric():
                return [int(expression)]
            results = []
            for i, c in enumerate(expression):
                if c in operators:
                    left_results = recursiveCompute(expression[:i])
                    right_results = recursiveCompute(expression[i + 1:])
                    for left in left_results:
                        for right in right_results:
                            match c:
                                case '-':
                                    results.append(left - right)
                                case '+':
                                    results.append(left + right)
                                case '*':
                                    results.append(left * right)
            return results

        return recursiveCompute(expression)
