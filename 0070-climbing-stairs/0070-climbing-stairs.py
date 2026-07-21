class Solution:
    def climbStairs(self, n: int) -> int:
        arr= [-1]*(n+1)
        return self.climbStairsRecursive(n, arr)
    
    def climbStairsRecursive(self, n : int, arr: list) -> int:
        if n == 1 or n == 0 : return 1
        if arr[n] != -1:
            return arr[n]
        arr[n] = self.climbStairsRecursive(n-1 , arr) + self.climbStairsRecursive(n-2, arr)
        return arr[n]