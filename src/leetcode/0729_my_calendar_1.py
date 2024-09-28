class MyCalendar:

    def __init__(self):
        self.appointments = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.appointments:
            if start < e and s < end:
                return False
        self.appointments.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
