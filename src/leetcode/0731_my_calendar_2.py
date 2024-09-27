class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlapping_bookings = []
        

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping_bookings:
            if s < end and start < e:
                return False
        for s, e in self.bookings:
            if s < end and start < e:
                self.overlapping_bookings.append((max(start, s), min(end, e)))
        self.bookings.append((start, end))
        return True
    
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)