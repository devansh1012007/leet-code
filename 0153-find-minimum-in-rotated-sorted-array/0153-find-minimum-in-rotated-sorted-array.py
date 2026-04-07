class Solution(object):
    def findMin(self, nums):
        high = len(nums)-1
        low = 0
        # similar to Search in a Rotated Array
        while high>low :
            L = nums[low]
            H = nums[high]
            if L < H:
                return L
            mid = low + (high-low) //2
            M = nums[mid]
            if M > H:
                low = mid + 1
            elif M < L:
                high = mid # reason v don't use (mid-1) here is because v didn't verify the mid and also this is the same reason why v didb't set high>=low coz what if mid is the lowest then low pointer will come to high's index and the loop will stop
        return nums[low]