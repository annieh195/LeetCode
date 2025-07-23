class MyCalendar:

    def __init__(self):
        self.startTimes = SortedList()
        self.endTimes = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        left = bisect_left(self.startTimes, endTime)
        right = bisect_right(self.endTimes, startTime)
        if left == right:
            self.startTimes.add(startTime)
            self.endTimes.add(endTime)
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)