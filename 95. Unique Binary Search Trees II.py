# try one (hardest way of doing it wrong approch)
class Solution(object):
    def tree(self, prev_trees, num):
        num = self.TreeNode(val = num)
        a = []
        for root in prev_trees:
            pass # function for adding new number in prev trees
        for nodes in prev_trees:
            pass # function for keeping num as root and then adding trees under it 
        # function for adding n in between the nodes of the prev_tree

        return a
    def generateTrees(self, n):
        # v need dp for savivg structure 
        # v need recursion for finding out all possible combo of trees
        dp = [[] for i in range(n+1)]
        dp[0] = []
        dp[1] = [1]
        for i in range(2,n+1):
            a = self.tree(dp[i-1],i)
            dp[i].append(a)

