class Solution:
    # the solution i was imagining was way comlex then this; i didn't intuatively think that this can actually solve the problem; i though iw will be something complex
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
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
        return False