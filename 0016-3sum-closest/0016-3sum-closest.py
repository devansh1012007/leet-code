class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # v can do it lil like BS 
        lenght = len(nums) 
        nums.sort()
        closest = float('inf')
        num_dict = {i: val for i, val in enumerate(nums)}
        for i in range(lenght - 2):
            lo = i + 1
            hi = lenght -1
            while hi > lo:
                curr = num_dict[hi]+num_dict[lo]+num_dict[i]
                if abs(curr-target)<abs(closest-target):
                    closest = curr
                if curr > target:
                    hi -=1
                elif curr < target:
                    lo += 1
                else :
                    return curr
        return closest  