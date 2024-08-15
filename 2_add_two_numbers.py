""""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""
import unittest
from typing import Optional


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


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = result = None
        curry = False
        while l1 and l2:
            if root is not None:
                result.next = ListNode()
                result = result.next
            else:
                root = result = ListNode()

            sum_val = l1.val + l2.val
            if curry:
                sum_val += 1
                curry = False

            if sum_val > 9:
                sum_val -= 10
                curry = True

            result.val = sum_val
            l1 = l1.next
            l2 = l2.next

        remainder = None
        if l1 is not None:
            remainder = l1
        elif l2 is not None:
            remainder = l2

        while remainder is not None:
            result.next = ListNode()
            result = result.next
            new_val = remainder.val
            if curry:
                new_val += 1
                curry = False
            if new_val > 9:
                new_val -= 10
                curry = True
            result.val = new_val
            remainder = remainder.next

        if curry:
            result.next = ListNode()
            result = result.next
            result.val = 1

        return root


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Example 1:        
        Explanation: 342 + 465 = 807.
        """
        l1 = ListNode.from_list([2, 4, 3])
        l2 = ListNode.from_list([5, 6, 4])
        expected_output = ListNode.from_list([7, 0, 8])
        self.assertEqual(expected_output, self.solution.addTwoNumbers(l1, l2))

    def test_example_2(self):
        """
        Example 2:
        """
        l1 = ListNode.from_list([0])
        l2 = ListNode.from_list([0])
        expected_output = ListNode.from_list([0])
        self.assertEqual(expected_output, self.solution.addTwoNumbers(l1, l2))

    def test_example_3(self):
        """
        Example 3:
        """
        l1 = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
        l2 = ListNode.from_list([9, 9, 9, 9])
        expected_output = ListNode.from_list([8, 9, 9, 9, 0, 0, 0, 1])
        self.assertEqual(expected_output, self.solution.addTwoNumbers(l1, l2))
