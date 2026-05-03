class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                temp = nums[i]
                nums[i]=0
                nums[j] = temp
                j +=1
            i +=1
        return nums