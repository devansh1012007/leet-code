class Solution(object):
    def search(self, nums, target):
        high = len(nums)-1
        low = 0
        while high >= low:
            while nums[low] == nums[high] and high - low > 2 :
                if nums[low] == target == nums[high]:
                    return True
                else:
                    low += 1
                    high -= 1
            mid = low + (high-low) //2
            if nums[mid]== target:
                return True
            elif nums[mid] >= nums[low]: ####### make sure that u r checking if they are sorted of not 
                if target >= nums[low] and target < nums[mid]:
                    high = mid -1
                else : 
                    low = mid + 1
            else:# nums[mid] <= nums[high]
                if target <= nums[high] and target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            '''else:
                if nums[mid] < target:
                    low = mid + 1
                else : 
                    high = mid - 1'''

        return False
    
    #other way of doing it but i didn't refine it 
    '''
    def BS(arr, lo, hi, x):
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def findPivot(arr, lo, hi):
        while lo <= hi:
            if arr[lo] <= arr[hi]:
                return lo

            mid = (lo + hi) // 2
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid

        return lo
    
    def search(self,nums,target):
        n = len(arr)
        pivot = findPivot(arr, 0, n - 1)
        if arr[pivot] == target:
            return pivot

        if pivot == 0:
            return binarySearch(arr, 0, n - 1, target)

        if arr[0] <= key:
            return binarySearch(arr, 0, pivot - 1, target)
        return binarySearch(arr, pivot + 1, n - 1, target)
        '''