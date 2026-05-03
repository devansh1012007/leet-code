class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        i = 0
        length = len(nums)
        if length == 1:
            return nums
        for i in range(length):
            if nums[i] != 0:
                nums[i],nums[j]= 0,nums[i] 
                j +=1
        return nums