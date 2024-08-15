"""
Published here:
https://leetcode.com/problems/combination-sum-ii/solutions/5640590/this-is-the-best-recursive-solition-with-backtracking-i-can-think-of-doesn-t-use-sets

40. Combination Sum II

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

"""
import time
from typing import List


# class Solution:


class Solution(object):
    @staticmethod
    def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
        # Sort elements in place to make algorithm more efficient and in order to return sorted lists
        candidates.sort()
        result = []
        combination = []

        def findCombination(index: int, target: int) -> None:
            # If target is 0, we found a valid combination
            if target == 0:
                result.append(combination[:])
                return
            for i in range(index, len(candidates)):
                # Skip duplicates in order to avoid repeating the same combination
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                # If the number exceeds the remaining target, no need to continue
                if candidates[i] > target:
                    break
                combination.append(candidates[i])
                # Recurse with the next index and updated remaining target
                findCombination(i + 1, target - candidates[i])
                # Backtrack: remove the last chosen candidate
                combination.pop()

        # Start the recursive search from the first index
        findCombination(0, target)
        return result

    @staticmethod
    def combinationSum2Iterative(candidates: List[int], target: int) -> List[List[int]]:
        """
        An alternative approach using iterative solution. Less efficient in tracking duplicates than the recursive approach
        :param candidates:
        :param target:
        :return:
        """
        candidates = sorted(x for x in candidates if x <= target)
        probes = []
        probe_sums = []
        results = []
        prev_x = -1
        while len(candidates) > 0:
            x = candidates.pop(0)
            # add a new single number probe
            if x == target:
                results.append([x])
                return results
            # add a new item to each probe
            for i in range(len(probe_sums) - 1, -1, -1):
                new_sum = probe_sums[i] + x
                if new_sum < target:  # add an element to a probe and keep searching
                    new_probe = probes[i][:]
                    new_probe.append(x)
                    if new_probe not in probes:
                        probes.append(new_probe)
                        probe_sums.append(new_sum)
                elif new_sum == target:
                    probe = probes.pop(i)
                    del probe_sums[i]
                    probe.append(x)
                    if probe not in results:
                        results.append(probe)
            if x < target and prev_x != x:
                probes.append([x])
                probe_sums.append(x)
                prev_x = x
        return results


if __name__ == '__main__':
    start_time = time.time()
    solution = Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    # solution = Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)
    print(solution)
    print("--- %.6f seconds ---" % (time.time() - start_time))
