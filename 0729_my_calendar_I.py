"""
# 729. My Calendar I
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

    MyCalendar() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

Constraints:

    0 <= start < end <= 109
    At most 1000 calls will be made to book.

"""
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(15, 25))
        self.assertTrue(cal.book(20, 30))

    def test_2(self):
        operations = ["MyCalendar", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book"]
        inputs = [
            [],  # MyCalendar constructor (no arguments)
            [47, 50],  # book(47, 50)
            [33, 41],  # book(33, 41)
            [39, 45],  # book(39, 45)
            [33, 42],  # book(33, 42)
            [25, 32],  # book(25, 32)
            [26, 35],  # book(26, 35)
            [19, 25],  # book(19, 25)
            [3, 8],  # book(3, 8)
            [8, 13],  # book(8, 13)
            [18, 27],  # book(18, 27)
        ]

        # Expected outcomes for each 'book' operation
        expected_results = [
            None,  # MyCalendar constructor returns nothing
            True,  # book(47, 50)
            True,  # book(33, 41)
            False,  # book(39, 45)
            False,  # book(33, 42)
            True,  # book(25, 32)
            False,  # book(26, 35)
            True,  # book(19, 25)
            True,  # book(3, 8)
            True,  # book(8, 13)
            False,  # book(18, 27)
        ]

        my_calendar = None  # Variable to hold MyCalendar instance

        # Iterate over the operations and inputs
        for i in range(len(operations)):
            operation = operations[i]
            args = inputs[i]

            if operation == "MyCalendar":
                # Instantiate the MyCalendar class
                my_calendar = MyCalendar()
                result = None
            else:
                # Dynamically call the 'book' method using getattr
                result = getattr(my_calendar, operation)(*args)

            # Check the result against the expected value, if not the constructor
            if expected_results[i] is not None:
                self.assertEqual(result, expected_results[i], f"Failed on operation {operation} with args {args}")


# A Simple brute force solution
# class MyCalendar:
#
#     def __init__(self):
#         self.schedule = []
#
#     def book(self, start: int, end: int) -> bool:
#         if start >= end:
#             return False
#
#         for (s, e) in self.schedule:
#             if s < end and start < e:
#                 return False
#         else:
#             # heappush(self.schedule, (start, end))
#             self.schedule.append((start, end))
#         return True

class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        start_idx = bisect.bisect_left(self.starts, end)
        end_idx = bisect.bisect_right(self.ends, start)
        if start_idx == end_idx:
            self.starts.insert(start_idx, start)
            self.ends.insert(end_idx, end)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
