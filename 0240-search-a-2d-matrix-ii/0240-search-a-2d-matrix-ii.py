class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                lo=0
                hi=n
                while (lo<hi):
                    mid=(lo+hi)//2
                    
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        lo = mid + 1
                    else:
                        hi = mid
                        
        return False