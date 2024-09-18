"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.



Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.



Constraints:

    1 <= stones.length <= 1000
    0 <= xi, yi <= 104
    No two stones are at the same coordinate point.
"""
import heapq
import unittest
from typing import List


class TestRemoveStones(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        inp = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
        expected_output = 5
        self.assertEqual(expected_output, self.solution.removeStones(inp))

    # def test_example_2(self):
    #     inp = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    #     expected_output = 3
    #     self.assertEqual(expected_output, self.solution.removeStones(inp))
    #
    # def test_example_3(self):
    #     inp = [[0, 0]]
    #     expected_output = 0
    #     self.assertEqual(expected_output, self.solution.removeStones(inp))
    #
    # def test_example_4(self):
    #     inp = [[5,9],[9,0],[0,0],[7,0],[4,3],[8,5],[5,8],[1,1],[0,6],[7,5],[1,6],[1,9],[9,4],[2,8],[1,3],[4,2],[2,5],[4,1],[0,2],[6,5]]
    #     expected_output = 19
    #     self.assertEqual(expected_output, self.solution.removeStones(inp))


# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         if len(stones) <= 1:
#             return 0
#
#         rows = {}
#         cols = {}
#
#         for i, (r, c) in enumerate(stones):
#             sr = rows.setdefault(r, set())
#             sr.add(i)
#             sc = cols.setdefault(c, set())
#             sc.add(i)
#
#         connectivities = []
#         for i, (r, c) in enumerate(stones):
#             heapq.heappush(connectivities, ((len(rows[r]) + len(cols[c]) - 2), i))
#
#         result = 0
#         while connectivities:
#             connected, i = heapq.heappop(connectivities)
#
#
#             r, c = stones[i]
#             current_row = rows[r]
#             current_row.remove(i)
#             current_col = cols[c]
#             current_col.remove(i)
#             # update connectivity
#             if connected > 0:
#                 result += 1
#                 for i, (rank, index) in enumerate(connectivities):
#                     if index in current_row or index in current_col:
#                         connectivities[i] = (rank - 1, index)
#                 heapq.heapify(connectivities)
#         return result

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        for r, c in stones:
            if r not in parent:
                parent[r] = r
                rank[r] = 0
            if ~c not in parent:  # using ~c to differentiate between rows and cols
                parent[~c] = ~c
                rank[~c] = 0
            union(r, ~c)

        # Number of stones - Number of connected components
        return len(stones) - len({find(x) for x in parent})