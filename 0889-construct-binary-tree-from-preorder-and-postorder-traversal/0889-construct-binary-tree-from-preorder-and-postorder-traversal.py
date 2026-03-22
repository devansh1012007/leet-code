# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# if elif reduced 3ms ! damn ; and pop was good 4 memory efficiency
class Solution(object):    
    def make_tree(self, left, right):
            if left == right:
                return TreeNode(self.preorder.pop()) 
            elif left > right:
                return None
            root = TreeNode(self.preorder.pop())
            mid = self.postodr_map[self.preorder[-1]]
            root.left = self.make_tree(left, mid)
            root.right = self.make_tree(mid + 1, right - 1)
            
            return root

    def constructFromPrePost(self, preorder, postorder):
        self.postodr_map = {val: idx for idx, val in enumerate(postorder)}
        self.preorder = preorder[::-1]
        return self.make_tree(0, len(preorder) - 1)