"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

root = [1, 2, 3, 4, 5, 6, 7]
root = [1, 2, null, 3, null, 4]
root = [1, null, 2, null, 3, null, 4]
root = [1, 1, 1, 1, 1, 1, 1]
root = [-4, -2, -5, -3, 1]

Constraints:

    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100




Follow up: Recursive solution is trivial, could you do it iteratively?
"""
import unittest
from idlelib.tree import TreeNode
from typing import Optional, List


class TestTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        inp = [1, None, 2, 3]
        expected_output = [3, 2, 1]
        self.assertEqual(expected_output, self.solution.postorderTraversal(TreeNode.from_list(inp)))

    def test_example_2(self):
        inp = []
        expected_output = []
        self.assertEqual(expected_output, self.solution.postorderTraversal(TreeNode.from_list(inp)))

    def test_example_3(self):
        inp = [1]
        expected_output = [1]
        self.assertEqual(expected_output, self.solution.postorderTraversal(TreeNode.from_list(inp)))

    # def test_example_4(self):
    #     inp = [1, 2, 3, 4, 5, 6, 7]
    #     expected_output = [7, 6, 5, 4, 3, 2, 1]
    #     self.assertEqual(expected_output, self.solution.postorderTraversal(TreeNode.from_list(inp)))

    def test_example_5(self):
        inp = [1, 2, None, 3, None, 4]
        expected_output = [4, 3, 2, 1]
        self.assertEqual(expected_output, self.solution.postorderTraversal(TreeNode.from_list(inp)))

    def test_example_6(self):
        inp = [3, 1, 2]
        expected_output = [1, 2, 3]
        self.assertEqual(expected_output, self.solution.postorderTraversal(TreeNode.from_list(inp)))

    def test_example_7(self):
        inp = [3, 2, 4, None, None, 1]
        expected_output = [2,1,4,3]
        self.assertEqual(expected_output, self.solution.postorderTraversal(TreeNode.from_list(inp)))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, items) -> Optional[TreeNode]:
        # Handle an empty list input
        if not items:
            return None

        # Create the root of the tree
        root = TreeNode(items[0])
        queue = [root]

        i = 1
        while i < len(items):
            current = queue.pop(0)

            # Add left child
            if i < len(items) and items[i] is not None:
                current.left = TreeNode(items[i])
                queue.append(current.left)
            i += 1

            # Add right child
            if i < len(items) and items[i] is not None:
                current.right = TreeNode(items[i])
                queue.append(current.right)
            i += 1

        return root

    def __repr__(self) -> str:
        """Helper function to print tree level by level (BFS)"""
        # queue = [self]
        # result = []
        # while queue:
        #     current = queue.pop(0)
        #     if current is None:
        #         result.append("null")
        #     else:
        #         result.append(str(current.val))
        #         queue.append(current.left)
        #         queue.append(current.right)
        # return " ".join(result)
        return str(self.val)


# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         result = self.postorderTraversal(root.left)
#         result += self.postorderTraversal(root.right)
#         result.append(root.val)
#         return result

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        result = []
        while queue:
            current = queue.pop()
            if current is not None:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
        return result[::-1]

    # class Solution:
    #     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #         if root is None:
    #             return []
    #         return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
