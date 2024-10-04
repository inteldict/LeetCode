"""
# 1590. Make Sum Divisible by P
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.



Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= p <= 109
"""
import unittest
from bisect import bisect_right

from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [3, 1, 4, 2]
        p = 6
        out = 1
        self.assertEqual(out, self.solution.minSubarray(nums, p))

    def test_2(self):
        nums = [6, 3, 5, 2]
        p = 9
        out = 2
        self.assertEqual(out, self.solution.minSubarray(nums, p))

    def test_3(self):
        nums = [1, 2, 3]
        p = 3
        out = 0
        self.assertEqual(out, self.solution.minSubarray(nums, p))

    def test_4(self):
        nums = [17, 3, 16, 12, 3, 19, 1, 8, 5, 8]
        p = 54
        out = -1
        self.assertEqual(out, self.solution.minSubarray(nums, p))


# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#         total = sum(nums)
#         if total < p:
#             return -1
#         remaining = total % p
#         if remaining == 0:
#             return 0
#         # now we just have to distract remaining elements from array
#         # we need to find all elements that would
#         nums.sort()
#
#         def sum_up_to_target(arr, target):
#             n = len(arr)
#
#             # DP array to track if a sum is possible and how many items are used to achieve it
#             dp = [None] * (target + 1)
#             dp[0] = (True, 0)  # Sum 0 is possible with 0 elements
#
#             # Iterate over each number in the array
#             for num in arr:
#                 # Update the DP array from right to left to avoid using the same number more than once
#                 for i in range(target, num - 1, -1):
#                     if dp[i - num] is not None:
#                         used_elements = dp[i - num][1] + 1
#                         if dp[i] is None or used_elements < dp[i][1]:
#                             dp[i] = (True, used_elements)
#
#             # If target sum is achievable, return number of excluded items, otherwise return -1
#             if dp[target] is not None:
#                 return dp[target][1]  # Number of elements used to achieve the target
#             else:
#                 return -1
#
#         j = bisect_right(nums, remaining)
#
#         return sum_up_to_target(nums[:j], remaining)


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = 0

        # Step 1: Calculate total sum and target remainder
        for num in nums:
            total_sum = (total_sum + num) % p

        target = total_sum % p
        if target == 0:
            return 0  # The array is already divisible by p

        # Step 2: Use a dict to track prefix sum mod p
        mod_map = {
            0: -1
        }  # To handle the case where the whole prefix is the answer
        current_sum = 0
        min_len = n

        # Step 3: Iterate over the array
        for i in range(n):
            current_sum = (current_sum + nums[i]) % p

            # Calculate what we need to remove
            needed = (current_sum - target + p) % p

            # If we have seen the needed remainder, we can consider this subarray
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            # Store the current remainder and index
            mod_map[current_sum] = i

        # Step 4: Return result
        return -1 if min_len == n else min_len
