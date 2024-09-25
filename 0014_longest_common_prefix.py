"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""
import unittest
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        strs = ["flower", "flow", "flight"]
        out = "fl"
        self.assertEqual(out, self.solution.longestCommonPrefix(strs))

    def test_2(self):
        strs = ["dog", "racecar", "car"]
        out = ""
        self.assertEqual(out, self.solution.longestCommonPrefix(strs))


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        n = len(strs)
        prefix = []
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for j in range(1, n):
                if i == len(strs[j]) or strs[j][i] != c:
                    return ''.join(prefix)
            prefix.append(c)
            i += 1
        return ''.join(prefix)
