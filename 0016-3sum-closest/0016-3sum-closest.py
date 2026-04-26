'''class Solution(object):
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
        return closest'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        
        return closest_sum