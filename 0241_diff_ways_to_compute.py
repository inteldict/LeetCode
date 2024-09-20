"""
# 241. Different Ways to Add Parentheses
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

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = {'+', '-', '*'}

        @cache  # this makes python3 do automatic memoization based on input arguments and output results
        def recursiveCompute(expression) -> List[int]:
            if len(expression) == 0:
                return []

            if expression.isnumeric():
                return [int(expression)]
            results = []
            for i, c in enumerate(expression):
                if c in operators:
                    for left in recursiveCompute(expression[:i]):
                        for right in recursiveCompute(expression[i + 1:]):
                            match c:
                                case '-':
                                    results.append(left - right)
                                case '+':
                                    results.append(left + right)
                                case '*':
                                    results.append(left * right)
            return results

        return recursiveCompute(expression)
