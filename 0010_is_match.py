"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".



Constraints:

    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
import unittest
from functools import cache


class TesIsMatch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_2(self):
        s = "aa"
        p = "a*"
        out = True
        self.assertEqual(out, self.solution.isMatch(s, p))


class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:

        @cache
        def dp(i: int, j: int) -> bool:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], "."}
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)
            return ans

        return dp(0, 0)
