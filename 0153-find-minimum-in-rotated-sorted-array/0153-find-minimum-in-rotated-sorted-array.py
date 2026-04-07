class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = len(nums)-1
        low = 0
        # similar to Search in a Rotated Array
        while high>low :
            if nums[low] < nums[high]:
                return nums[low]
            mid = low + (high-low) //2
            if nums[mid] > nums[high]:
                low = mid + 1
                print(high, low)
            elif nums[mid] < nums[low]:
                high = mid 
                print(high, low)
        return nums[low]