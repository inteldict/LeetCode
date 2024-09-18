"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.



Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.



Constraints:

    The number of nodes in the list is in the range [0, 1000].
    0 <= Node.val <= 1000
    1 <= k <= 50
"""
import unittest
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, nums):
        # Handle an empty list input
        if not nums:
            return None

        # Create the head of the linked list
        head = cls(nums[0])
        current = head

        # Iterate over the rest of the numbers and create linked list nodes
        for num in nums[1:]:
            current.next = cls(num)
            current = current.next

        return head

    def __repr__(self):
        # This method is just for convenience to print the linked list in a readable format
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        # Compare values and recursively compare the next nodes
        current_self = self
        current_other = other

        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next

        # If both are None at the end, lists are equal
        return current_self is None and current_other is None


class TestSplitToParts(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:
        """
        head = [1, 2, 3]
        k = 5
        expected_output = [ListNode.from_list(x) for x in [[1], [2], [3], [], []]]
        self.assertEqual(expected_output, self.solution.splitListToParts(ListNode.from_list(head), k))

    def test_example_2(self):
        """
        Example 2:
        """
        head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        expected_output = [ListNode.from_list(x) for x in [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]]
        self.assertEqual(expected_output, self.solution.splitListToParts(ListNode.from_list(head), k))

    def test_example_3(self):
        """
        Example 3:
        """
        head = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected_output = [ListNode.from_list(x) for x in [[1, 2, 3], [4, 5], [6, 7]]]
        self.assertEqual(expected_output, self.solution.splitListToParts(ListNode.from_list(head), k))


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, current = 0, head
        while current:
            current = current.next
            length += 1

        if k >= length:
            quotient = 1
            reminder = 0
        else:
            quotient, reminder = divmod(length, k)

        result = [head, ]
        current = head
        for i in range(1, k):
            for j in range(quotient-1):
                if not current:
                    break
                current = current.next
            if reminder > 0 and current:
                current = current.next
                reminder -= 1
            if current:
                current.next, current = None, current.next
                result.append(current)
            else:
                result.append(None)

        return result
