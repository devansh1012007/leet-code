class Solution(object):
    def searchInsert(self, nums, target):
        idx = 0
        try:
            while target>nums[idx]:
                idx += 1
            return idx
        
        except:
            return idx