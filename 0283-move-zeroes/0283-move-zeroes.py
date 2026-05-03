class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        i = 0
        length = len(nums)
        if length == 1:
            return nums
        while i < length:
            if nums[i] != 0:
                nums[i],nums[j]= 0,nums[i] 
                j +=1
            i +=1
        return nums