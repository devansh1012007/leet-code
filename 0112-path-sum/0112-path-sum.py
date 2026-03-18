# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        stk = []
        total = 0
        while len(stk) != 0 or root:
            while root:
                targetSum -= root.val
                stk.append(root)
                root = root.left
            root = stk.pop()
            print(total, root.val)
            if targetSum == 0 and root.left is None and root.right is None:
                return True
            targetSum += root.val
            root = root.right
            print(total)      
'''
# can't do this shit with stk
# 
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum - root.val == 0
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)