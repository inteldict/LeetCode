"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        num = 3749
        s = 'MMMDCCXLIX'
        self.assertEqual(num, self.solution.romanToInt(s))

    def test_2(self):
        num = 58
        s = "LVIII"
        self.assertEqual(num, self.solution.romanToInt(s))

    def test_3(self):
        num = 1994
        s = "MCMXCIV"
        self.assertEqual(num, self.solution.romanToInt(s))

    def test_4(self):
        s = "III"
        num = 3
        self.assertEqual(num, self.solution.romanToInt(s))


# class Solution:
#
#     def romanToInt(self, s: str) -> int:
#         n = len(s)
#         ans = 0
#         i = 0
#         while i < n:
#             match s[i]:
#                 case 'M':
#                     ans += 1000
#                 case 'D':
#                     ans += 500
#                 case 'C':
#                     if i + 1 < n:
#                         match s[i + 1]:
#                             case 'D':
#                                 ans += 400
#                                 i += 2
#                                 continue
#                             case 'M':
#                                 ans += 900
#                                 i += 2
#                                 continue
#                     ans += 100
#                 case 'L':
#                     ans += 50
#                 case 'X':
#                     if i + 1 < n:
#                         match s[i + 1]:
#                             case 'C':
#                                 ans += 90
#                                 i += 2
#                                 continue
#                             case 'L':
#                                 ans += 40
#                                 i += 2
#                                 continue
#                     ans += 10
#                 case 'V':
#                     ans += 5
#                 case 'I':
#                     if i + 1 < n:
#                         match s[i + 1]:
#                             case 'V':
#                                 ans += 4
#                                 i += 2
#                                 continue
#                             case 'X':
#                                 ans += 9
#                                 i += 2
#                                 continue
#                     ans += 1
#             i += 1
#         return ans

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        n = len(s)
        for i in range(n - 1):
            # If the next numeral is larger, subtract the current one (subtractive notation)
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                ans -= roman_map[s[i]]
            else:
                ans += roman_map[s[i]]

        return ans + roman_map[s[n - 1]]
