"""
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.



Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).

Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.



Constraints:

    arr.length == n
    1 <= n <= 105
    n is even.
    -109 <= arr[i] <= 109
    1 <= k <= 105
"""

import unittest
from collections import Counter
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
        k = 5
        out = True
        self.assertEqual(out, self.solution.canArrange(nums, k))

    def test_2(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 7
        out = True
        self.assertEqual(out, self.solution.canArrange(nums, k))

    def test_3(self):
        nums = arr = [1, 2, 3, 4, 5, 6]
        k = 10
        out = False
        self.assertEqual(out, self.solution.canArrange(nums, k))

    def test_4(self):
        nums = [2,2,2,2,2,2]
        k = 3
        out = False
        self.assertEqual(out, self.solution.canArrange(nums, k))


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        if n % 2 != 0:
            return False
        map = Counter(((x % k) + k) % k for x in arr)
        if 0 in map:
            if map[0] % 2 != 0:
                return False
            del map[0]

        for i, v in map.items():
            if i < k and v != map[k - i]:
                return False
        return True
