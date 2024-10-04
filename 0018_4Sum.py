"""
# 18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]



Constraints:

    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109

"""

import unittest
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        out = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(sorted(out), sorted(sorted(x) for x in self.solution.fourSum(nums, target)))

    def test_2(self):
        nums = [2, 2, 2, 2, 2]
        target = 8
        out = [[2, 2, 2, 2]]
        self.assertEqual(sorted(out), sorted(sorted(x) for x in self.solution.fourSum(nums, target)))


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#
#         def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
#             res = []
#
#             # If we have run out of numbers to add, return res.
#             if len(nums) < k:
#                 return res
#
#             # the average value in k array
#             average_value = target // k
#             # compare smallest and largest value with the average
#             if average_value < nums[0] or nums[-1] < average_value:
#                 return res
#
#             if k == 2:
#                 return twoSum(nums, target)
#
#             for i in range(len(nums)):
#                 if i == 0 or nums[i - 1] != nums[i]:
#                     for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
#                         res.append([nums[i]] + subset)
#             return res
#
#         # def twoSum(nums: List[int], target: int) -> List[List[int]]:
#         #     res = []
#         #     num_set = set()
#         #     for i in range(len(nums)):
#         #         if not res or res[-1][1] != nums[i]:  # avoid duplicates in result
#         #             if (target - nums[i]) in num_set:
#         #                 res.append([target - nums[i], nums[i]])
#         #         num_set.add(nums[i])
#         #     return res
#
#         def twoSum(nums, target):
#             # Two pointer approach to find pairs summing to target
#             left, right = 0, len(nums) - 1
#             res = []
#             while left < right:
#                 pair_sum = nums[left] + nums[right]
#                 if pair_sum == target:
#                     res.append([nums[left], nums[right]])
#                     left += 1
#                     right -= 1
#                     # Avoid duplicates
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1
#                 elif pair_sum < target:
#                     left += 1
#                 else:
#                     right -= 1
#             return res
#
#         nums.sort()
#         return kSum(nums, target, 4)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int, prefix) -> None:
            # If we have run out of numbers to add, return res.
            if len(nums) < k:
                return

            # the average value in k array
            average_value = target // k
            # compare smallest and largest value with the average
            if average_value < nums[0] or nums[-1] < average_value:
                return

            if k == 2:
                twoSum(nums, target, prefix)
                return

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    kSum(nums[i + 1:], target - nums[i], k - 1, prefix + [nums[i]])

        def twoSum(nums, target, prefix) -> None:
            # Two pointer approach to find pairs summing to target
            left, right = 0, len(nums) - 1

            while left < right:
                pair_sum = nums[left] + nums[right]
                if pair_sum == target:
                    result.append(prefix + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Avoid duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif pair_sum < target:
                    left += 1
                else:
                    right -= 1

        result = []
        nums.sort()
        kSum(nums, target, 4, [])
        return result

# with open("user.out", "w") as f:
#     inputs = map(loads, stdin)
#     i = 0
#     args = []
#     for a in inputs:
#         i += 1
#         args.append(a)
#         if i & 1:
#             continue
#         print(str(fourSum(*args)).replace(" ", ""), file=f)
#         args.clear()
# exit(0)
