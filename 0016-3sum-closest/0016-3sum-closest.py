class Solution(object):
    def threeSumClosest(self, nums, target):
        # v can do it lil like BS 
        lenght = len(nums) 
        nums.sort()
        closest = float('inf')
        for i in range(lenght - 2):
            lo = i + 1
            hi = lenght -1
            while hi > lo:
                curr = nums[hi]+nums[lo]+nums[i]
                if abs(curr-target)<abs(closest-target):
                    closest = curr
                if curr > target:
                    hi -=1
                elif curr < target:
                    lo += 1
                else :
                    return curr
        return closest