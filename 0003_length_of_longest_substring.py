"""
Given a string s, find the length of the longest
substring
without repeating characters.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""
import unittest


class TestLemonadeChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        """
        s = "abcabcbb"
        expected_output = 3
        self.assertEqual(expected_output, self.solution.lengthOfLongestSubstring(s))

    def test_example_2(self):
        """
        Example 2:

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        """
        s = "bbbbb"
        expected_output = 1
        self.assertEqual(expected_output, self.solution.lengthOfLongestSubstring(s))

    def test_example_3(self):
        """
        Example 3:

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        """
        s = "pwwkew"
        expected_output = 3
        self.assertEqual(expected_output, self.solution.lengthOfLongestSubstring(s))

    def test_example_4(self):
        """
        Example 3:

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        """
        s = "abba"
        expected_output = 2
        self.assertEqual(expected_output, self.solution.lengthOfLongestSubstring(s))



class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        char_index = {}
        max_len = last_len = 0
        last_match_index = 0
        for i,ch in enumerate(s):
            if ch not in char_index:
                last_len += 1
            else:
                if last_len > max_len:
                    max_len = last_len
                last_match_index = max(last_match_index, char_index[ch]) # Update the last occurrence
                last_len = i - last_match_index
            char_index[ch] = i # Update the character's latest index

        if last_len > max_len:
            max_len = last_len

        return max_len

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     char_index = {}
    #     max_len = 0
    #     start = 0
    #
    #     for i, ch in enumerate(s):
    #         # If the character is already in the map and its index is within the current window
    #         if ch in char_index and char_index[ch] >= start:
    #             start = char_index[ch] + 1  # Move the start right after the last occurrence
    #
    #         char_index[ch] = i  # Update the character's latest index
    #         max_len = max(max_len, i - start + 1)  # Calculate the maximum length
    #
    #     return max_len
