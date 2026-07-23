class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       nums.sort()
       length = len(nums)
       return nums[length//2]

'''
I think i over though the solution, we can make a num class for a custom dick which updates at every step to change according to the highest occuring num. but it was over kill , i didn't think about making it simple and using some sorting techniques coz it's a sorting question 
'''