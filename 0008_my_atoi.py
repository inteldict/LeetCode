"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.



Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^

Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^

Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^

Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^

Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.



Constraints:

    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

"""

import unittest


class TestMyAtoi(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        Input: s = " -042"

        Output: -42

        Explanation:
        Step 1: "   -042" (leading whitespace is read and ignored)
        Step 2: "   -042" ('-' is read, so the result should be negative)
        Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
        """
        s = " -042"
        y = -42
        self.assertEqual(y, self.solution.myAtoi(s))

    def test_example_2(self):
        """
        Example 2:
        Input: s = "42"

        Output: 42

        Explanation:

        The underlined characters are what is read in and the caret is the current reader position.
        Step 1: "42" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "42" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "42" ("42" is read in)
                   ^
        """
        s = "42"
        y = 42
        self.assertEqual(y, self.solution.myAtoi(s))

    def test_example_3(self):
        """
        Example 3:

        Input: s = "1337c0d3"

        Output: 1337

        Explanation:

        Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
                     ^
        """
        s = "1337c0d3"
        y = 1337
        self.assertEqual(y, self.solution.myAtoi(s))

    def test_example_4(self):
        """
        Example 4:
        Input: s = "0-1"

        Output: 0

        Explanation:

        Step 1: "0-1" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
                  ^
        """
        s = "0-1"
        y = 0
        self.assertEqual(y, self.solution.myAtoi(s))

    def test_example_5(self):
        """
        Example 5:

        Input: s = "words and 987"

        Output: 0

        Explanation:

        Reading stops at the first non-digit character 'w'.
        """
        s = s = "words and 987"
        y = 0
        self.assertEqual(y, self.solution.myAtoi(s))

    def test_example_6(self):
        """
        Example 6:

        Input: s = "words and 987"

        Output: 0

        Explanation:

        Reading stops at the first non-digit character 'w'.
        """
        s = "-+12"
        y = 0
        self.assertEqual(y, self.solution.myAtoi(s))


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        result = ""
        if s[0] == '-':
            sign = -1
        elif s[0] == "+":
            pass
        elif not s[0].isdigit():
            return 0
        else:
            result += s[0]
        for c in s[1:]:
            if not c.isdigit():
                break
            result += c
        if not result:
            return 0
        iresult = int(result) * sign
        max = 2147483647  # 2 ** 31 - 1
        min = -2147483648  # -2 ** 31
        if iresult > max:
            return max
        elif iresult < min:
            return min
        else:
            return iresult
