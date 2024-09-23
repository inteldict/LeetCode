"""
# 2707. Extra Characters in a String

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

Constraints:

    1 <= s.length <= 50
    1 <= dictionary.length <= 50
    1 <= dictionary[i].length <= 50
    dictionary[i] and s consists of only lowercase English letters
    dictionary contains distinct words

"""
import unittest
from functools import cache
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        s = "leetscode"
        dictionary = ["leet", "code", "leetcode"]
        out = 1
        self.assertEqual(out, self.solution.minExtraChar(s, dictionary))

    def test_2(self):
        s = "sayhelloworld"
        dictionary = ["hello", "world"]
        out = 3
        self.assertEqual(out, self.solution.minExtraChar(s, dictionary))

    def test_3(self):
        s = "aakodubkrlauvfkzje"
        dictionary = ["ix", "qoqw", "ax", "ar", "v", "hxpl", "nxcg", "thr", "kod", "pns", "cdo", "euy", "es", "rf",
                      "bxcx", "xe", "ua", "vws", "vumr", "zren", "bzt", "qwxn", "ami", "rrbk", "ak", "uan", "g", "vfk",
                      "jxmg", "fhb", "nqgd", "fau", "rl", "h", "r", "jxvo", "tv", "smfp", "lmck", "od"]
        out = 9
        self.assertEqual(out, self.solution.minExtraChar(s, dictionary))

    def test_4(self):
        s = "dwmodizxvvbosxxw"
        dictionary = ["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e", "wmo", "cehy", "tskz", "ds",
                      "kzbu"]
        out = 7
        self.assertEqual(out, self.solution.minExtraChar(s, dictionary))

    def test_5(self):
        s = "metzeaencgpgvsckjrqafkxgyzbe"
        dictionary = ["zdzz", "lgrhy", "r", "ohk", "zkowk", "g", "zqpn", "anoni", "ka", "qafkx", "t", "jr", "xdye",
                      "mppc", "bqqb", "encgp", "yf", "vl", "ctsxk", "gn", "cujh", "ce", "rwrpq", "tze", "zxhg", "yzbe",
                      "c", "o", "hnk", "gv", "uzbc", "xn", "kk", "ujjd", "vv", "mxhmv", "ugn", "at", "kumr", "ensv",
                      "x", "uy", "gb", "ae", "jljuo", "xqkgj"]
        out = 5
        self.assertEqual(out, self.solution.minExtraChar(s, dictionary))

# class Solution:
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#         for word in sorted(dictionary, key=len):
#             s = s.replace(word, '')
#         return len(s)

# class Solution:
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#         n = len(s)
#         root = self.buildTrie(dictionary)
#
#         @cache
#         def dp(start):
#             if start == n:
#                 return 0
#             # To count this character as a left over character
#             # move to index 'start + 1'
#             ans = dp(start + 1) + 1
#             node = root
#             for c in range(start, n):
#                 if s[c] not in node.children:
#                     break
#                 node = node.children[s[c]]
#                 if node.is_word:
#                     ans = min(ans, dp(c + 1))
#             return ans
#
#         return dp(0)
#
#     def buildTrie(self, dictionary):
#         root = TrieNode()
#         for word in dictionary:
#             node = root
#             for char in word:
#                 if char not in node.children:
#                     node.children[char] = TrieNode()
#                 node = node.children[char]
#             node.is_word = True
#         return root


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

# This not DP implementation fails on test:  Wrong Answer # 2007 / 2028 testcases passed
# In order to fix it one probably should be able to ignore some words

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if not s:
            return 0
        n = len(s)
        root = self.buildTrie(dictionary)

        def num_word_chars(i) -> List[int]:
            j = i
            node = root
            ans = []
            while j < n and s[j] in node.children:
                node = node.children[s[j]]
                j += 1
                if node.is_word:
                    # here are the following possibilities
                    # 1. The matching word can be longer
                    # 2. there is another word starting from j + 1
                    ans.append(j - i)

            return ans

        @cache
        def dp(i) -> int:
            num_left_over = 0
            while i < n:
                ans = num_word_chars(i)
                if not ans:
                    # print(i, s[i])
                    num_left_over += 1
                    i += 1
                else:  # there are several alternatives
                    min_nlo = n
                    for a in ans:
                        lo = dp(i + a)
                        if lo < min_nlo:
                            min_nlo = lo
                    if 1 not in ans: # skip a character is always a valid alternative
                        min_nlo = min(min_nlo, dp(i+1) + 1)
                    return num_left_over + min_nlo
            return num_left_over
        return dp(0)

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root
