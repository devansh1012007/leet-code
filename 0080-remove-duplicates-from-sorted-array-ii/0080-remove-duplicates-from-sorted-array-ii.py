class Solution(object):
    def removeDuplicates(self, nums):
        """
        i = 0
        j=0
        counter = len(nums)
        while i < counter:
            while nums[i] == nums[j] :
                if j - i >1:
                    nums[j]==nums[j+1] 
                    j -=1   
                    counter -= 1
                j +=1
                if j >= counter:
                    break 
            i = j
        return counter
        """
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 

        return k