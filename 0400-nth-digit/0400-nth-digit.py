class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idt v need to make a series which ia denoted by the index of largest num
        # bcoz that is very complex + no smartness
        # bro idk how to use BS here
        # i think there might be some function for spliting the num
        # maybe v do BS for a number series 1 to 2^21-1 and for evaluation v use a custom formula for cal the actual index of a num --> fuck it 
        # lets just use a custom formula for finding the num in which this index belongs to , and the v do BS inside that number --> bad idea 
        # it is just mainly maths --> learning abt it now

        count = 9
        digit = 1
        start = 1
        # following is the BS btw
        while n > count*digit:
            n -= count*digit
            count *= 10
            digit += 1
            start *=10
        number = start + (n - 1) // digit
        return int(str(number)[(n-1)%digit])