"""
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation:
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Example 2:

Input: skill = [3,4]
Output: 12
Explanation:
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation:
There is no way to divide the players into teams such that the total skill of each team is equal.

Constraints:

    2 <= skill.length <= 105
    skill.length is even.
    1 <= skill[i] <= 1000
"""
import operator
import unittest
from bisect import bisect_right

from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        skill = [3, 2, 5, 1, 3, 4]
        out = 22
        self.assertEqual(out, self.solution.dividePlayers(skill))

    def test_2(self):
        skill = [3, 4]
        out = 12
        self.assertEqual(out, self.solution.dividePlayers(skill))

    def test_3(self):
        skill = [1, 1, 2, 3]
        out = -1
        self.assertEqual(out, self.solution.dividePlayers(skill))

    def test_4(self):
        skill = [40, 24, 16, 14]
        out = -1
        self.assertEqual(out, self.solution.dividePlayers(skill))


# def multiplyList(arr):
#     # Multiply elements one by one
#     result = 1
#     for x in arr:
#         result *= x
#     return result

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        total_sum = sum(skill)
        num_teams = n // 2
        # check if it is possible to divide persons by skills evenly
        if total_sum % num_teams != 0:
            return -1
        skill.sort()
        team_skill = skill[0] + skill[-1]
        result = skill[0] * skill[-1]
        for i in range(1, num_teams):
            if team_skill != skill[i] + skill[n - i - 1]:
                return -1
            result += skill[i] * skill[n - i - 1]
        return result
#
# with open("user.out", "w") as f:
#     inputs = map(loads, stdin)
#     for nums in inputs:
#         print(Solution().dividePlayers(nums),file=f)
# exit(0)
