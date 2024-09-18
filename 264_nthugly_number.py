"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.



Constraints:

    1 <= n <= 1690

An incredible solution using time and space complexity of $O(N)$

"""
import unittest


class TestMaxPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        n = 10
        expected_output = 12
        self.assertEqual(expected_output, self.solution.nthUglyNumber(n))

    def test_example_2(self):
        """
        Example 1:
        """
        n = 1
        expected_output = 1
        self.assertEqual(expected_output, self.solution.nthUglyNumber(n))

    def test_example_3(self):
        """
        Example 1:
        """
        n = 7
        expected_output = 8
        self.assertEqual(expected_output, self.solution.nthUglyNumber(n))


# class Solution:
#     @staticmethod
#     def nthUglyNumber(n: int) -> int:
#         heap = [1]
#         i = 0
#         while i < n:
#             num = heap[i]
#             insert_sorted(heap, num * 2)
#             insert_sorted(heap, num * 3)
#             insert_sorted(heap, num * 5)
#             i += 1
#         return heap[n - 1]
#
#
# def insert_sorted(arr, item):
#     index = bisect.bisect_left(arr, item)
#     # Check if the item is already in the array
#     if index < len(arr) and arr[index] == item:
#         return
#     arr.insert(index, item)


class Solution:
    @staticmethod
    def nthUglyNumber(n: int) -> int:
        heap = [1]
        l2, l3, l5 = 2, 3, 5
        i2, i3, i5 = 1, 1, 1

        for i in range(1, n):
            min_val = min(l2, l3, l5)
            heap.append(min_val)
            if min_val == l2:
                l2 = heap[i2] * 2
                i2 += 1
            if min_val == l3:
                l3 = heap[i3] * 3
                i3 += 1
            if min_val == l5:
                l5 = heap[i5] * 5
                i5 += 1
        return heap[n - 1]

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         p2, p3, p5 = 1, 1, 1
#         head2, head3, head5 = 1, 1, 1
#         # Final merged linked list and pointer
#         ugly = [0] * (n + 1)
#         p = 1
#
#         # Start merging 3 linked list, until finding the nth ugly number
#         while p <= n:
#             min_val = min(head2, head3, head5)
#             ugly[p] = min_val
#             p += 1
#             # move forward the corresponding linked list pointer
#             if min_val == head2:
#                 head2 = ugly[p2] * 2
#                 p2 += 1
#             if min_val == head3:
#                 head3 = ugly[p3] * 3
#                 p3 += 1
#             if min_val == head5:
#                 head5 = ugly[p5] * 5
#                 p5 += 1
#
#         return ugly[n]
