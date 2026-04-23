class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = 0
        if n == 0:
            return nums1
        while i < m+n and j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
            print (nums1)
        #sort nums1
        nums1.sort()
        return nums1