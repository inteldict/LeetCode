"""
# 440. K-th Smallest in Lexicographical Order

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

Example 2:

Input: n = 1, k = 1
Output: 1

Constraints:

    1 <= k <= n <= 109
"""
import unittest
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        n = 13
        k = 2
        out = 10
        self.assertEqual(out, self.solution.findKthNumber(n, k))

    def test_2(self):
        n = 1
        k = 1
        out = 1
        self.assertEqual(out, self.solution.findKthNumber(n, k))

    def test_3(self):
        n = 681692778
        k = 351251360
        out = 416126219
        self.assertEqual(out, self.solution.findKthNumber(n, k))


# class Solution:
#     def findKthNumber(self, n: int, k: int) -> int:
#         num = 1
#         for _ in range(k - 1):
#             # adding zeros to the right
#             if num * 10 <= n:
#                 num *= 10
#             else:
#                 while num % 10 == 9 or num + 1 > n:
#                     num //= 10
#                 num += 1
#         return num

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix: int, n: int) -> int:
            """Count the steps between prefix and the next number lexicographically within the range [1, n]."""
            steps = 0
            first = prefix
            next_prefix = prefix + 1
            while first <= n:
                steps += min(n + 1, next_prefix) - first
                first *= 10
                next_prefix *= 10
            return steps

        num = 1
        k -= 1  # since the first number (1) is already the first lexicographical number

        while k > 0:
            steps = count_steps(num, n)
            if steps <= k:
                # If the number of steps is less than or equal to k, skip this prefix
                num += 1
                k -= steps
            else:
                # Otherwise, go deeper in the current prefix
                num *= 10
                k -= 1
        return num
