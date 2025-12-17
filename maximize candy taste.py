def binarySearch(nums, avgVal, k):
    k -= 1
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        l = False
        r = False
        if nums[mid] == avgVal:
            ans.append(nums[mid])
        
        if nums[mid] < avgVal:
            left = mid + 1
            l = True
        else:# need to remove nums[] from every where
            right = mid - 1
            r = True
    # if it is not in the nums 
    if r:
        a = min(avgVal - nums[left],nums[right+1] - avgVal )
        if a == avgVal - nums[left]:
            ans.append(nums[left])
        else:
            ans.append(nums[right+1])
    else:
        a = min(avgVal - nums[left-1],nums[right] - avgVal )#need to check it 
        if a == avgVal - nums[left-1]:
            ans.append(nums[left-1])
        else:
            ans.append(nums[right])
    return k 
def mid_num(UL,LL,k,nums):
    if k>0:
        avg = (UL+LL)/2
        k = binarySearch(nums,avg, k) 
        mid_num(avg,LL,k/2,nums)#left 
        mid_num(UL,avg,k/2,nums)#right
    return None
class Solution(object):

    def maximumTastiness(self, price, k):
        #The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.
        #  maximum tastiness of a candy basket. ==> measn select candy in such a way that the smallest difference b/w prices is maximum  
        # plan => sort -> biggest and smallest val -> middle term of both val (avg) -> binary search for the avg -> if can't find number then select the number closest to avg -> closest number will be left and right limits of binary search -> repeat it till k is satisfied
        # -> select a,b,c as biggest, smallest and avg -> return there min abs diff 
        # if k in even then no mid pt
        price.sort()
        global ans
        ans = []# if issue with global var then just pass them as paramenters in functions
        if k%2 != 0:
            odd = True
        ans.append(price[0])
        ans.append(price[-1])
        min_val = abs(price[0] - price[-1])
        k -= 2
        while k > 0: # maybe we can remove this while loop
            mid_num(ans[0], ans[1], k , price) 
        if odd :
            ans.pop[2]
        ans.sort()
        i = 1
        while i < len(ans): #find the difference double pointer 
            min_val = min(ans[i]- ans[i-1], min_val)
            i += 1
        return min_val

# eximple usage
sol = Solution()
print(sol.maximumTastiness([1,3,5,7,9], 3))  # Example call to the function
