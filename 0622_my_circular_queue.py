"""
622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language.

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:

    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

"""
import unittest


class Test(unittest.TestCase):

    def execute(self, operations, inputs, expected_results):
        # Iterate over the operations and inputs
        cirq_deque = None
        for i in range(len(operations)):
            operation = operations[i]
            args = inputs[i]
            if operation == "MyCircularQueue":
                # Instantiate the MyCalendar class
                cirq_deque = MyCircularQueue(*args)
                result = None
            else:
                # Dynamically call the 'book' method using getattr
                result = getattr(cirq_deque, operation)(*args)

            # Check the result against the expected value, if not the constructor
            if expected_results[i] is not None:
                self.assertEqual(result, expected_results[i], f"Failed on operation {operation} with args {args}")

    def test_1(self):
        operations = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue",
                      "enQueue", "Rear"]
        inputs = [[3], [1], [2], [3], [4], [], [], [], [4], []]

        # Expected outcomes for each 'book' operation
        expected_results = [None, True, True, True, False, 3, True, True, True, 4]
        self.execute(operations, inputs, expected_results)

    def test_2(self):
        operations = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "deQueue", "deQueue", "isEmpty",
                      "isEmpty", "Rear", "Rear", "deQueue"]
        inputs = [[8], [3], [9], [5], [0], [], [], [], [], [], [], []]
        expected_results = [None, True, True, True, True, True, True, False, False, 0, 0, True]
        self.execute(operations, inputs, expected_results)


class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
        self.maxsize = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.maxsize
        self.arr[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.maxsize
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.maxsize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
