"""
17. Letter Combinations of a Phone Number
Medium
Topics
Companies

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]



Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""

import unittest
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        digits = "23"
        out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(out, sorted(self.solution.letterCombinations(digits)))

    def test_2(self):
        digits = "2"
        out = ["a", "b", "c"]
        self.assertEqual(out, self.solution.letterCombinations(digits))

    def test_3(self):
        digits = ""
        out = []
        self.assertEqual(out, self.solution.letterCombinations(digits))


# class Solution:
#
#     def __init__(self):
#         self.map = {'2': 'abc', '3': 'def', '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
#
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#
#         digit = digits[0]
#         result = []
#         tail = digits[1:]
#         if tail:
#             for rest in self.letterCombinations(tail):
#                 for c in self.map[digit]:
#                     result.append(c + rest)
#         else:
#             for c in self.map[digit]:
#                 result.append(c)
#         return result

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        queue = ['']

        for digit in digits:
            letters = digit_to_letters[digit]
            new_queue = []

            for combination in queue:
                for letter in letters:
                    new_queue.append(combination + letter)

            queue = new_queue

        return queue
