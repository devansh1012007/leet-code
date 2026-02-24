# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 0 : 
            return None
        root = TreeNode()
        root.val = max(nums)
        pos = nums.index(root.val)
        root.left = self.constructMaximumBinaryTree(nums[:pos])
        root.right = self.constructMaximumBinaryTree(nums[pos+1:])
        return root