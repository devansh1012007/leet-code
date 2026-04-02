class Solution(object):
    '''def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ig it's simple 1 BS after other ?
        # can i get it in single BS
        ans = []
        low = 0
        high = len(nums)-1
        while high >= low :
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans.append(mid)
                high = mid - 1
                if len(ans)==2:
                    break    
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        while len(ans)<2:
            ans.append(-1)
        
        return ans[::-1]'''
        # v need some way to make it son that it always go to the 1st occurrence 1st and then the 2nd one 
        # plus pls reduce the nested if and the 2 whhile loop, find better ways to do it 
        # ig it's 1 after other coz in 4th case they want 0
        #######################
        # if will be done using 2 pointers and if will just need 1 loop
        # if none then [-1, -1]
        # if 2 then [i,j]
        # if 1 in list[k,k]
        # Pattern of this type of questions --> the problem maker has no prob if u use nested if else in the BS after some condition is met 
    '''def binarySearch(self,high,low, x, arr):
        while low <= high:

            mid = low + (high - low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        # If we reach here, then the element
        # was not present
        return None '''
    '''def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        low = 0
        high = len(nums)-1
        if high == 0:
            if nums[high] == target: return [high, high] 
            else: return [-1,-1]
        while high >= low :
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ''''''if nums[mid+1]==target: return [mid, mid+1] # what if target is at end this is fucked 
                elif nums[mid-1]==target: return [mid-1, mid]
                else: return [mid, mid]'''''''
                a = self.binarySearch(mid-1, low,target,nums)
                if a == -1:
                    a = self.binarySearch(high, mid+1,target,nums)
                    if a == -1:
                        return [mid,mid]
                    return[mid, a]
                return[a, mid]

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return [-1,-1]'''
    # IMP --> THEY ARE ASKING 1ST AND LAST 
    # nex approch
    '''def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        low = 0
        high = len(nums)-1
        if high == 0:
            if nums[high] == target: return [high, high] 
            else: return [-1,-1]
        while high >= low :
            mid = low + (high - low) // 2
            if nums[mid] == target:
                a = self.binarySearch(mid-1, low,target,nums)
                b = self.binarySearch(high, mid+1,target,nums)
                print(a,b)
                if a >= 0 and b >= 0:
                    return [a,b]
                elif a>= 0:
                    return [a,mid]
                elif b>= 0:
                    return [mid,b]
                else:
                    return [mid,mid]

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return [-1,-1]
    '''
    # my approch is flawed
    # turns out it is 2 saprate BS (i saw sol)
    def searchRange(self, nums, target):
        def first():
            ans=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if(target==nums[mid]):
                    ans=mid
                    high=mid-1
                elif(nums[mid]>target):
                    high=mid-1
                elif(nums[mid]<target):
                    low=mid+1
            return ans

        def last():
            ans=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if(target==nums[mid]):
                    ans=mid
                    low=mid+1
                elif(target>nums[mid]):
                    low=mid+1
                elif(target<nums[mid]):
                    high=mid-1
            return ans
        return [first(),last()]

