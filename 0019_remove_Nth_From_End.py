"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?
"""
import unittest
from typing import Optional


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        n = 2
        out = ListNode.from_list([1, 2, 3, 5])
        self.assertEqual(out, self.solution.removeNthFromEnd(head, n))

    def test_2(self):
        head = ListNode.from_list([1])
        n = 1
        out = None
        self.assertEqual(out, self.solution.removeNthFromEnd(head, n))

    def test_3(self):
        head = ListNode.from_list([1, 2])
        n = 1
        out = ListNode.from_list([1])
        self.assertEqual(out, self.solution.removeNthFromEnd(head, n))

    def test_4(self):
        head = ListNode.from_list([1, 2])
        n = 2
        out = ListNode.from_list([2])
        self.assertEqual(out, self.solution.removeNthFromEnd(head, n))

    def test_5(self):
        head = ListNode.from_list([59])
        n = 1
        out = None
        self.assertEqual(out, self.solution.removeNthFromEnd(head, n))

    def test_6(self):
        head = ListNode.from_list([71, 70])
        n = 1
        out = ListNode.from_list([71])
        self.assertEqual(out, self.solution.removeNthFromEnd(head, n))

    def test_7(self):
        head = ListNode.from_list([92, 91, 90])
        n = 3
        out = ListNode.from_list([91, 90])
        self.assertEqual(out, self.solution.removeNthFromEnd(head, n))


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


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         curr = head
#         for _ in range(n):
#             curr = curr.next
#         # edge case were we need to remove first element of the array
#         if not curr:
#             return head.next
#         n_min_curr = head
#         while curr.next:
#             curr = curr.next
#             n_min_curr = n_min_curr.next
#
#         if n_min_curr:
#             n_min_curr.next = n_min_curr.next.next
#         return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

# This part was reverse engineered, but makes not improvement in execution time
# def format_output(result):
#     return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'
#
#
# input_data = sys.stdin.read().strip()
# inp = input_data.splitlines()
#
# with open("user.out", "w") as f:
#     results = []
#
#     for i in range(0, len(inp), 2):
#         nums = json.loads(inp[i])
#         # Create the head of the linked list
#         head = ListNode(nums[0])
#         current = head
#
#         # Iterate over the rest of the numbers and create linked list nodes
#         for num in nums[1:]:
#             current.next = ListNode(num)
#             current = current.next
#         n = int(inp[i + 1])
#         result = removeNthFromEnd(head, n)
#         list_result = []
#         while result:
#             list_result.append(result.val)
#             result = result.next
#         results.append(format_output(list_result))
#     # raise Exception(results)
#     for result in results:
#         f.write(f"{result}\n")
#     f.flush()
# exit(0)