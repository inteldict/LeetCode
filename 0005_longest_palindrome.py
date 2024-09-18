"""
# Longest Palindromic Substring

Given a string s, return the longest
palindromic
substring
in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""
import unittest


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "babad"
        expected_output = "bab"
        self.assertEqual(expected_output, self.solution.longestPalindrome(s))

    def test_example_2(self):
        s = "cbbd"
        expected_output = "bb"
        self.assertEqual(expected_output, self.solution.longestPalindrome(s))

    def test_example_3(self):
        s = " "
        expected_output = " "
        self.assertEqual(expected_output, self.solution.longestPalindrome(s))

    def test_example_4(self):
        s = "babcbabcbaccba"
        expected_output = "abcbabcba"
        self.assertEqual(expected_output, self.solution.longestPalindrome(s))

    def test_example_5(self):
        s = "ac"
        expected_output = "a"
        self.assertEqual(expected_output, self.solution.longestPalindrome(s))

    def test_example_6(self):
        s = "bb"
        expected_output = "bb"
        self.assertEqual(expected_output, self.solution.longestPalindrome(s))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        An Implementation of Manacher’s Algorithm
        :param s: string to look for palindromes
        :return: longest palindromic substring
        """
        n = len(s)
        if n <= 1:
            return s
        n = 2 * n + 1  # Position count
        l = [0] * n
        l[0] = 0
        l[1] = 1
        c = 1  # centerPosition
        r = 2  # centerRightPosition

        max_lps_length = 1
        max_lps_center_position = 1

        # 'i' is currentRightPosition
        for i in range(2, n):

            # get currentLeftPosition i_mirror for currentRightPosition i
            i_mirror = 2 * c - i
            l[i] = 0
            diff = r - i
            # If currentRightPosition i is within centerRightPosition r
            if diff > 0:
                l[i] = min(l[i_mirror], diff)

            # Attempt to expand palindrome centered at currentRightPosition i
            # Here for odd positions, we compare characters and
            # if match then increment LPS Length by ONE
            # If even position, we just increment LPS by ONE without
            # any character comparison
            # Expanding the palindrome centered at index i
            try:
                while ((i + l[i]) < n and (i - l[i]) > 0) and \
                        (((i + l[i] + 1) % 2 == 0) or \
                         (s[(i + l[i] + 1) // 2] == s[(i - l[i] - 1) // 2])):
                    l[i] += 1
            except Exception as e:
                pass

            if l[i] > max_lps_length:  # Track maxLPSLength
                max_lps_length = l[i]
                max_lps_center_position = i

            # If palindrome centered at currentRightPosition i
            # expand beyond centerRightPosition r,
            # adjust centerPosition c based on expanded palindrome.
            if i + l[i] > r:
                c = i
                r = i + l[i]

        start = (max_lps_center_position - max_lps_length) // 2
        end = start + max_lps_length - 1
        return s[start:end + 1]
