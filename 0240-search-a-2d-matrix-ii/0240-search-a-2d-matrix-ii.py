class Solution:
    # the solution i was imagining was way comlex then this; i didn't intuatively think that this can actually solve the problem; i though iw will be something complex;
    # this code works so beautifully
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''m = len(matrix)
        n = len(matrix[0])
        cols = n - 1
        rows = 0
        # print(rows,cols)
        while rows < m and cols >= 0:
            curr = matrix[rows][cols]
            if curr == target:
                return True
            elif curr > target:
                cols -= 1
            else:
                rows += 1
        return False'''
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