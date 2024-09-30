"""
731. My Calendar II
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

    MyCalendarTwo() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked.
myCalendarTwo.book(50, 60); // return True, The event can be booked.
myCalendarTwo.book(10, 40); // return True, The event can be double booked.
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

Constraints:

    0 <= start < end <= 109
    At most 1000 calls will be made to book.

"""

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.my_calendar = MyCalendarTwo()

    def execute(self, operations, inputs, expected_results):
        # Iterate over the operations and inputs
        for i in range(len(operations)):
            operation = operations[i]
            args = inputs[i]

            if operation == "MyCalendarTwo":
                # Instantiate the MyCalendar class
                result = None
            else:
                # Dynamically call the 'book' method using getattr
                result = getattr(self.my_calendar, operation)(*args)

            # Check the result against the expected value, if not the constructor
            if expected_results[i] is not None:
                self.assertEqual(result, expected_results[i], f"Failed on operation {operation} with args {args}")

    def test_1(self):
        operations = ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
        inputs = [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

        # Expected outcomes for each 'book' operation
        expected_results = [None, True, True, True, False, True, True]
        self.execute(operations, inputs, expected_results)

    def test_2(self):
        operations = ["MyCalendarTwo", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book"]
        inputs = [[], [24, 40], [43, 50], [27, 43], [5, 21], [30, 40], [14, 29], [3, 19], [3, 14], [25, 39], [6, 19]]

        # Expected outcomes for each 'book' operation
        expected_results = [None, True, True, True, True, False, False, True, False, False, False]
        self.execute(operations, inputs, expected_results)

    def test_3(self):
        operations = ["MyCalendarTwo", "book", "book", "book", "book"]
        inputs = [[], [24, 40], [27, 43], [5, 21], [14, 29], ]

        # Expected outcomes for each 'book' operation
        expected_results = [None, True, True, True, False]
        self.execute(operations, inputs, expected_results)


from sortedcontainers import SortedDict


class MyCalendarTwo:

    def __init__(self):
        # Store the number of bookings at each point.
        self.booking_count = SortedDict()
        # The maximum number of overlapped bookings allowed.
        self.max_overlapped_booking = 2

    def book(self, start: int, end: int) -> bool:
        # Increase and decrease the booking count at the start and end respectively.
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlapped_booking = 0

        # Calculate the prefix sum of bookings.
        for count in self.booking_count.values():
            overlapped_booking += count
            # If the number of overlaps exceeds the allowed limit
            # rollback and return False.
            if overlapped_booking > self.max_overlapped_booking:
                # Rollback changes.
                self.booking_count[start] -= 1
                self.booking_count[end] += 1

                # Remove entries if their count becomes zero to clean up the SortedDict.
                if self.booking_count[start] == 0:
                    del self.booking_count[start]
                if self.booking_count[end] == 0:
                    del self.booking_count[end]

                return False

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
