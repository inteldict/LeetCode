"""
# 641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

    MyCircularDeque(int k) Initializes the deque with a maximum size of k.
    boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
    int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
    int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
    boolean isEmpty() Returns true if the deque is empty, or false otherwise.
    boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:

    1 <= k <= 1000
    0 <= value <= 1000
    At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
"""
import unittest


class Test(unittest.TestCase):

    def execute(self, operations, inputs, expected_results):
        # Iterate over the operations and inputs
        cirq_deque = None
        for i in range(len(operations)):
            operation = operations[i]
            args = inputs[i]
            if operation == "MyCircularDeque":
                # Instantiate the MyCalendar class
                cirq_deque = MyCircularDeque(*args)
                result = None
            else:
                # Dynamically call the 'book' method using getattr
                result = getattr(cirq_deque, operation)(*args)

            # Check the result against the expected value, if not the constructor
            if expected_results[i] is not None:
                self.assertEqual(result, expected_results[i], f"Failed on operation {operation} with args {args}")

    def test_1(self):
        operations = ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull",
                      "deleteLast", "insertFront", "getFront"]
        inputs = [[3], [1], [2], [3], [4], [], [], [], [4], []]

        # Expected outcomes for each 'book' operation
        expected_results = [None, True, True, True, False, 2, True, True, True, 4]
        self.execute(operations, inputs, expected_results)

    def test_2(self):
        operations = ["MyCircularDeque", "insertFront", "insertFront", "insertFront", "isFull", "deleteLast",
                      "deleteLast",
                      "deleteLast", "isEmpty"]
        inputs = [[3], [1], [2], [3], [], [], [], [], []]
        # Expected outcomes for each 'book' operation
        expected_results = [None, True, True, True, True, True, True, True, True]
        self.execute(operations, inputs, expected_results)

    def test_3(self):
        operations = ["MyCircularDeque", "insertFront", "insertLast", "getFront", "insertLast", "getFront",
                      "insertFront", "getRear", "getFront", "getFront", "deleteLast", "getRear"]
        inputs = [[5], [7], [0], [], [3], [], [9], [], [], [], [], []]
        expected_results = [None, True, True, 7, True, 7, True, 3, 9, 9, True, 0]
        self.execute(operations, inputs, expected_results)


class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
        self.maxsize = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.maxsize
        self.arr[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.maxsize
        self.arr[self.rear] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.maxsize
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.maxsize
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.maxsize

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
