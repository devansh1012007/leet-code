class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        i = 0
        j = len(height)-1
        while i < j:
            max_vol = max((min(height[i],height[j])*(j-i)), max_vol)
            if height[i]> height[j]:
                j -= 1
            else :
                i += 1

        return max_vol