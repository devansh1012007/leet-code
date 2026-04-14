class MyCalendar(object):

    def __init__(self):
        self.booked =[]

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """       
        for s,e in self.booked:
            if not (endTime <= s or startTime >= e):  #(new_end <= old_start) or (new_start >= old_end)
                return False
        # idk how to add and sort + do it with BS         
        self.booked.append((startTime,endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)