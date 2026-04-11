'''class Solution(object):
    def findDuplicate(self, nums):
        # imp point to note is that the provided arr is not sorted 
        # it can be done with 2 pointers but it will take too much time
        L = len(nums)
        for i in range(L):
            j = i + 1
            I = nums[i]
            while j < L:
                if I == nums[j]: 
                    return I
                j += 1
'''
'''
class Solution(object):
    def findDuplicate(self, nums):
        # imp thing to note -> the elements of arr cannot exceed lenght of arr
        # vacan use .count() 
        # but it still cause time out
        for i in nums:
            if nums.count(i) >= 2:
                return i
'''
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        return next(num for num in nums if num in seen or seen.add(num))
