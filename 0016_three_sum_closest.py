"""
# 16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:

    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104
"""
import unittest
from bisect import bisect_right, bisect_left
from typing import List, Counter


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [-1, 2, 1, -4]
        target = 1
        out = 2
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))

    def test_2(self):
        nums = [0, 0, 0]
        target = 1
        out = 0
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))

    def test_3(self):
        nums = [1, 1, 1, 0]
        target = -100
        out = 2
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))

    def test_4(self):
        nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
        target = -2
        out = -2
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))

    def test_5(self):
        nums = [0, 3, 97, 102, 200]
        target = 300
        out = 300
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))

    def test_6(self):
        nums = [0, 1, 2]
        target = 0
        out = 3
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))

    def test_7(self):
        nums = [-4, 2, 2, 3, 3, 3]
        target = 0
        out = 0
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))

    def test_8(self):
        nums = [1, 3, 4, 7, 8, 9]
        target = 15
        out = 15
        self.assertEqual(out, self.solution.threeSumClosest(nums, target))


# This solution doesn't work
# class Solution:
#     def threeSumClosest(self, nums: List[int], target) -> int:
#         if len(nums) <= 3:
#             return sum(nums)
#
#         nums.sort()  # Sort the array
#
#         # edge cases
#         if nums[0] + nums[1] + nums[2] > target:
#             return nums[0] + nums[1] + nums[2]
#         if nums[-1] + nums[-2] + nums[-3] < target:
#             return nums[-1] + nums[-2] + nums[-3]
#
#         n = len(nums)
#
#         closest = float('-inf')
#         min_diff = float('inf')
#         j = len(nums) - 1
#         for i in range(n - 2):
#             t = target - nums[i] - nums[j]
#             c = bisect_right(nums, t)
#             if c > j and j < len(nums) - 1:
#                 j += 1
#                 continue
#             if c < i and i > 0:
#                 i -= 1
#                 continue
#             if c >= j:
#                 c = j - 1
#             elif c <= i:
#                 c = i + 1
#             if c == i or c == j:
#                 break
#             diff = t - nums[c]
#             if diff == 0:
#                 return target
#             abs_diff = abs(diff)
#             if abs_diff < min_diff:
#                 min_diff = abs_diff
#                 closest = nums[i] + nums[j] + nums[c]
#             elif abs_diff == min_diff:
#                 closest = max(closest, nums[i] + nums[j] + nums[c])
#
#             if diff > 0:
#                 i += 1
#             else:  # diff < 0 here
#                 j -= 1
#         return closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            return sum(nums)

        nums.sort()  # Sort the array

        # edge cases that significantly improve performance
        if nums[0] + nums[1] + nums[2] > target:
            return nums[0] + nums[1] + nums[2]
        if nums[-1] + nums[-2] + nums[-3] < target:
            return nums[-1] + nums[-2] + nums[-3]

        n = len(nums)
        closest_sum = float('inf')  # Initialize closest sum to a large value

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for 'i' to avoid repeated work

            # Two pointers
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Early exit if the sum exactly matches the target
                if current_sum == target:
                    return current_sum

                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers based on the comparison with the target
                if current_sum < target:
                    left += 1
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return closest_sum

# def threeSumClosest(nums: List[int], target: int) -> int:
#     if len(nums) <= 3:
#         return sum(nums)
#
#     nums.sort()  # Sort the array
#
#     # edge cases
#     if nums[0] + nums[1] + nums[2] > target:
#         return nums[0] + nums[1] + nums[2]
#     if nums[-1] + nums[-2] + nums[-3] < target:
#         return nums[-1] + nums[-2] + nums[-3]
#
#     n = len(nums)
#     closest_sum = float('inf')  # Initialize closest sum to a large value
#
#     for i in range(n - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue  # Skip duplicates for 'i' to avoid repeated work
#
#         # Two pointers
#         left, right = i + 1, n - 1
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
#
#             # Early exit if the sum exactly matches the target
#             if current_sum == target:
#                 return current_sum
#
#             # Update the closest sum if the current sum is closer to the target
#             if abs(current_sum - target) < abs(closest_sum - target):
#                 closest_sum = current_sum
#
#             # Move pointers based on the comparison with the target
#             if current_sum < target:
#                 left += 1
#                 # Skip duplicates for the left pointer
#                 while left < right and nums[left] == nums[left - 1]:
#                     left += 1
#             else:
#                 right -= 1
#                 # Skip duplicates for the right pointer
#                 while left < right and nums[right] == nums[right + 1]:
#                     right -= 1
#
#     return closest_sum
#
# with open("user.out", "w") as f:
#     inp = map(loads, stdin)
#     for nums in inp:
#         print(f"{threeSumClosest(nums, next(inp))}", file=f)
# exit(0)
