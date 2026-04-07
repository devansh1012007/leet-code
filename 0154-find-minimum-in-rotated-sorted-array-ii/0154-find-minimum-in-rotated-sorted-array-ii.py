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
                high = mid
            else:
                high -= 1
        return nums[low]