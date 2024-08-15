"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Intuition
As we know target, we can easily get a compliment for any given number. So it es enought to read the list once.

This solution is efficient with a time complexity of $$O(n)$$, where $$n$$ is the number of elements in nums, since each element is processed once, and dictionary lookups are on average $$O(1)$$.

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

# Code
"""
import unittest
from typing import List


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_output = [1, 2]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # Dictionary to store the index of a last element with the value we have seen so far
        seen = {}
        # Iterate through the all numbers
        for i, num in enumerate(nums):
            right_part = seen.get(target - num)
            if right_part is None:
                seen[num] = i
            else:
                return [right_part, i]
        return []

# if __name__ == '__main__':
#     # unittest.main()
#     start_time = time.time()
#     # solution = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
#     solution = Solution().twoSum(nums=[3, 3], target=6)
#     print(solution)
#     print("--- %.6f seconds ---" % (time.time() - start_time))
