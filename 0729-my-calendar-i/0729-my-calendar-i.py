class MyCalendar:

    def __init__(self):
        self.booked =[]
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.booked:
            if not (endTime <= s or startTime >= e):  
                return False
        self.booked.append((startTime,endTime))
        return True

