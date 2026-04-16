'''class Solution(object):
    def threeSum(self, nums):

        ans = []
        if not nums:
            return ans
        nums.sort()
        lenth= len(nums)
        for i in range(lenth):
            a = -nums[i]
            for j in range(i + 1, lenth):# how  to use hash tabel and sorting ?
                b = nums[j]
                for k in range(j + 1, lenth):
                    if (j != k and b + nums[k] == a):
                        c = [-a, b,nums[k]]
                        c.sort()
                        if c in ans:         
                            continue
                        ans.append(c)
        return ans
        '''

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res