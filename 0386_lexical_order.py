"""
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:

Input: n = 2
Output: [1,2]

Constraints:

    1 <= n <= 5 * 104

"""
import unittest
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        n = 13
        out = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(out, self.solution.lexicalOrder(n))

    def test_2(self):
        n = 100
        out = [1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 7, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 8, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 9, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        self.assertEqual(out, self.solution.lexicalOrder(n))


# Submitted one-liner solution
# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         return list(int(x) for x in sorted(str(x) for x in range(1, n+1)))
# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         return sorted(range(1, n + 1), key=str)
#
# with open("user.out", "w") as f:
#     inputs = map(loads, stdin)
#     for nums in inputs:
#         print(str(Solution().lexicalOrder(nums)).replace(" ", ""), file=f)
# exit(0)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        num = 1
        for _ in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return res
