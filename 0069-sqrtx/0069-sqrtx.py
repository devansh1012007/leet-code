class Solution(object):
    def mySqrt(self, x):
        # newton metod of sqr root needed
        if x < 2:
            return x
        low = 1
        high = x//2
        while low <= high:
            mid = (high + low) //2
            a = mid*mid 
            if a == x:
                return mid
            elif a<x:
                low = mid + 1  
            else:
                high = mid - 1

        return high