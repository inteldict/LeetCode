"""
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

    CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
    void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
    int pop() Pops and returns the top of the stack or -1 if the stack is empty.
    void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.



Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[None,None,None,2,None,None,None,None,None,103,202,201,-1]
Explanation
CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1);                          // stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.push(3);                          // stack becomes [1, 2, 3]
stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100);                // stack becomes [101, 102, 103]
stk.increment(2, 100);                // stack becomes [201, 202, 103]
stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
stk.pop();                            // return -1 --> Stack is empty return -1.



Constraints:

    1 <= maxSize, x, k <= 1000
    0 <= val <= 100
    At most 1000 calls will be made to each method of increment, push and pop each separately.


"""
import unittest


class Test(unittest.TestCase):

    def execute(self, operations, inputs, expected_results):
        # Iterate over the operations and inputs
        obj = None
        for i in range(len(operations)):
            operation = operations[i]
            args = inputs[i]
            if operation == "CustomStack":
                # Instantiate the MyCalendar class
                obj = CustomStack(*args)
                result = None
            else:
                # Dynamically call a method using getattr
                result = getattr(obj, operation)(*args)

            # Check the result against the expected value, if not the constructor
            if expected_results[i] is not None:
                self.assertEqual(result, expected_results[i], f"Failed on operation {operation} with args {args}")

    def test_1(self):
        operations = ["CustomStack", "push", "push", "pop", "push", "push", "push", "increment", "increment", "pop",
                      "pop", "pop", "pop"]
        inputs = [[3], [1], [2], [], [2], [3], [4], [5, 100], [2, 100], [], [], [], []]
        expected_results = [None, None, None, 2, None, None, None, None, None, 103, 202, 201, -1]
        self.execute(operations, inputs, expected_results)


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)
        self.inc.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        if k == 0:
            return
        self.inc[k - 1] += val

# class Node:
#     def __init__(self, val, prev=None):
#         self.val = val
#         self.next = None
#         self.prev = prev
#
#
# class CustomStack:
#
#     def __init__(self, maxSize: int):
#         self.bottom = None
#         self.top = None
#         self.size = 0
#         self.max_size = maxSize
#
#     def push(self, x: int) -> None:
#         if self.size >= self.max_size:
#             return
#         node = Node(x, self.top)
#         if self.top:
#             self.top.next = node
#         self.top = node
#         if not self.bottom:
#             self.bottom = self.top
#         self.size += 1
#
#     def pop(self) -> int:
#         if not self.size:
#             return -1
#         node = self.top
#         self.top = node.prev
#         if not self.top:
#             self.bottom = None
#         self.size -= 1
#         return node.val
#
#     def increment(self, k: int, val: int) -> None:
#         if self.size == 0:
#             return
#         node = self.bottom
#         for _ in range(k):
#             if not node:
#                 break
#             node.val += val
#             node = node.next
