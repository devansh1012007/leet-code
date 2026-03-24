class Solution(object):# so baisly v take len(nums) now v have n ; now irritate through the sorted array comparing it to range 
# i not study bit multiplication 
# another way of doing it will be to use set insted of compassion direcly to arr
    def missingNumber(self, nums):
        n = len(nums)
        nums_set= set(nums)
        for i in range(0,n+1):
            if i not in nums_set :
                return i