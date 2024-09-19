import unittest


class TesIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        x = 11
        y = True
        self.assertEqual(y, self.solution.isPalindrome(x))

    def test_example_2(self):
        """
        Example 1:
        """
        x = 121
        y = True
        self.assertEqual(y, self.solution.isPalindrome(x))


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # elif x < 10:
        #     return True
        # digits = []
        # while x:
        #     x, res = divmod(x, 10)
        #     digits.append(res)
        #
        # i = 0
        # j = len(digits) - 1
        # while i < j:
        #     if digits[i] != digits[j]:
        #         return False
        #     i += 1
        #     j -= 1
        #
        # return True
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
