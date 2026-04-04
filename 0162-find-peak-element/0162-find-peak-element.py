class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
        """
        :type nums: List[int]
        :rtype: int
        
        # i am thinking that it can be done like this
        if len(nums) == 0:
            return None 
        if len(nums) == 1:
            return 0   
        def process(num):
            high = len(num) -1 
            low = 0
            while high >= low:
                mid = low + (high-low) // 2
                if num[mid] > num[mid-1] and num[mid+1] < num[mid]:
                    return mid
                elif num[mid] < num[mid-1]: ## this one i could not click 
                    high = mid - 1
                else:
                    low = mid + 1
            return 0
        '''def process(num, mode):
            high = len(num) -1 
            low = 0
            while high >= low:
                mid = low + (high-low) // 2
                if num[mid] > num[mid-1] and num[mid+1] < num[mid]:
                    return mid
                elif mode: 
                    high = mid -1
                else :
                    low = mid+1 '''
        if(nums[0] > nums[1]): return 0 ## this didn't hit
        if(nums[-1] > nums[-2]): return len(nums)-1## this didn't hit
        return process(nums)

        # refined approch 
        """