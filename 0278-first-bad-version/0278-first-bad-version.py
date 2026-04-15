class Solution(object):
    def firstBadVersion(self, n):
        hi = n
        lo = 1
        while hi > lo:
            mid = lo + (hi-lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid+1
        return hi
# [1,2,3,4,5] --> [False, False, True, True, True]

## Same same but different --> 
"""
class Solution(object):
    def firstBadVersion(self, n):
        hi = n
        lo = 1
        while hi > lo:
            mid = lo + (hi-lo) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return hi
"""
"""
class Solution(object):
    def firstBadVersion(self, n):
        hi = n
        lo = 1
        while hi >= lo:
            mid = lo + (hi-lo) // 2
            if isBadVersion(mid):
                hi = mid-1
            else:
                lo = mid+1
        return lo
"""