"""
1514. Path with Maximum Probability
Medium
Topics
Companies
Hint

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:

    2 <= n <= 10^4
    0 <= start, end < n
    start != end
    0 <= a, b < n
    a != b
    0 <= succProb.length == edges.length <= 2*10^4
    0 <= succProb[i] <= 1
    There is at most one edge between every two nodes.
"""
import heapq
import math
import unittest
from typing import List


class TestMaxProbability(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start = 0
        end = 2
        expected_output = 0.25000
        self.assertEqual(expected_output, self.solution.maxProbability(n, edges, succProb, start, end))

    def test_example_2(self):
        """
        Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
        Output: 0.30000
        :return:
        """
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.3]
        start = 0
        end = 2
        expected_output = 0.30000
        self.assertEqual(expected_output, self.solution.maxProbability(n, edges, succProb, start, end))

    def test_example_3(self):
        """
        Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
        Output: 0.00000
        """
        n = 3
        edges = [[0, 1]]
        succProb = [0.5]
        start = 0
        end = 2
        expected_output = 0.0
        self.assertEqual(expected_output, self.solution.maxProbability(n, edges, succProb, start, end))

    def test_example_4(self):
        n = 5
        edges = [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]]
        succProb = [0.37, 0.17, 0.93, 0.23, 0.39, 0.04]
        start = 3
        end = 4
        expected_output = 0.21390
        self.assertTrue(
            math.fabs(expected_output - self.solution.maxProbability(n, edges, succProb, start, end)) <= 1e-5)

    def test_example_5(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.0, 0.00001]
        start = 0
        end = 2
        expected_output = 0.00001
        self.assertTrue(
            math.fabs(expected_output - self.solution.maxProbability(n, edges, succProb, start, end)) <= 1e-5)


class Solution:
    """
    Solving the problem using Dijkstra's algorithm with a priority queue
    """

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # Build the graph as an adjacency list with negative log probabilities
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            w = succProb[i]
            if w > 0.0:
                graph[u].append((v, -math.log(w)))
                graph[v].append((u, -math.log(w)))

        # Min-heap priority queue for Dijkstra's algorithm
        pq = [(0, start_node)]  # (negative log probability, node)
        dist = [float("Inf")] * n
        dist[start_node] = 0

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if node == end_node:
                return math.exp(-curr_dist)

            if curr_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        # If end_node is unreachable, return 0.0
        return 0.0
