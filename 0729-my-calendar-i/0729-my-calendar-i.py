class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.calendar) == 0:
            self.calendar.add([startTime, endTime])
            return True
        else:
            for i in range(len(self.calendar)):
                curr_start, curr_end = self.calendar[i]

                if endTime <= curr_start:
                    if i > 0 and self.calendar[i-1][1] == startTime:
                        startTime = self.calendar[i-1][0]
                        self.calendar.discard(self.calendar[i-1])
                    if startTime == curr_start:
                        endTime = curr_end
                        self.calendar.discard(self.calendar[i])
                    self.calendar.add([startTime, endTime])
                    return True

                elif startTime >= curr_end:
                    if i == len(self.calendar) - 1:
                        if curr_end == startTime:
                            startTime = curr_start
                            self.calendar.discard(self.calendar[i])
                        self.calendar.add([startTime, endTime])
                        return True
                    continue
                else:
                    return False

            self.calendar.add([startTime, endTime])
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)