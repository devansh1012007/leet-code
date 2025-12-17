# this should work right ? ------->> YAAA the correct ans is not differ form this one --> i fucked up by writting nums = nums.sort() instead of nums.sort() only
class Solution(object):
    def arrayPairSum(self, nums):
        nums = nums.sort()
        sums = 0
        for i in nums[::2]: ## error 
            sums += i
        return sums
    
###
class Solution(object):
    def arrayPairSum(self, nums):
        nums = nums.sort()
        sums = 0
        i = 0
        while i < len(nums):
            sums += nums[i]
            i += 2
        return sums

###
class Solution(object):
    def arrayPairSum(self, nums):# nums in not itrateable 
        nums = nums.sort() ## Assigning nums = nums.sort() sets nums to None because list.sort() sorts in place and returns None. This causes len(nums) on line 26 to fail with a 'NoneType' object has no len()' error.
        sums = 0 #### --> it looks like they are passing parameters in loop (MAYBE) 
        x = len(nums)
        for i in range(0,x,2): ## error --> object of type 'NoneType' has no len()
            sums += nums[i]

        return sums
    

### corrct ans for some reason 
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        sums = 0
        for i in range(0, len(nums), 2):
            # Add every element at even positions
            sums += nums[i]
            
        return sums