class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 1st collum select then BS; 
        ## pt 1
        # column select for 0 and -1 index val of column check if target is between them 
        # v can take index 0 val of all columns and then use BS then v can make dict and save sets of currosponding col

        ## pt 2
        # insted of BS v can also use set  

        for i in matrix :
            if target <= i[-1] and target >= i[0]:
                i_set = set(i)
                if target in i_set:
                    return True
                else:
                    return False
        
        return False