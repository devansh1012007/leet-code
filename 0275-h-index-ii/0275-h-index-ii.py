class Solution:
    def hIndex(self, citations: List[int]) -> int:
        L = len(citations) 
        lo = 0
        high = L-1
        while high > lo:
            mid = lo + (high-lo) //2
            cit = citations[mid]
            paper = L - mid
            if cit == paper:
                return paper
            elif cit< paper:
                lo = mid+1
            else: 
                high = mid
        return min(citations[lo],L-lo)