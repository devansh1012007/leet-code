class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # element shuffing to the end of list 
        i = 0
        j=0
        counter = len(nums)
        while i < counter:
            while nums[i] == nums[j] :
                if j - i >1:
                    nums.append(nums.pop(j)) 
                    j -=1   
                    counter -= 1
                j +=1
                if j >= counter:
                    break 
            i = j
        return counter