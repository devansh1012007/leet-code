# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        low = 0
        high = n
        while high >= low:
            mid = low + (high-low) //2
            check = guess(mid)
            if check == 0 :
                return mid
            elif check == 1:
                low = mid +1
            else:
                high = mid -1