class Solution(object):
    def BS(self, low, high, target,nums):
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    def search(self, nums, target): 
        L = len(nums)-1
        if L==-1:
            return L
        elif L == 0:
            return self.BS(0,0,target,nums)
        prev = nums[0]
        for i in range(1,L+1):
            a = nums[i]
            if a > prev: prev = a
            else:
                if target <= nums[-1]:
                    return self.BS(i,L,target,nums)
                else:
                    return self.BS(0,i-1,target,nums)
        
        return self.BS(0,L,target,nums)

# solution is not eligent , THINK !

# Think how u can do it without making another loop !!!

# so baicly by compairing mid and low and high v can tell which side is sorted and which is not
# but v need to add anoth