class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        i = 0
        length = len(nums)
        if length == 1:
            return nums
        while i < length:
            if nums[i] != 0:
                temp = nums[i]
                nums[i]=0
                nums[j] = temp
                j +=1
            i +=1
        return nums