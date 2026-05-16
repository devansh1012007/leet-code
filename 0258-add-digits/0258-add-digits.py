class Solution(object):
    def addDigits(self, num):
        total = 0
        for i in str(num):
            total += int(i)
        if total<10:return total
        else:return self.addDigits(total)
        