# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def make_tree(self,left, right):
            if left>right:
                return None
            root = TreeNode(self.preorder[self.preord_idx])
            self.preord_idx += 1
            if left == right: # i forgot this in 1st try
                return root
            mid = self.postodr_map[self.preorder[self.preord_idx]]
            root.left = self.make_tree(left, mid)
            root.right = self.make_tree(mid + 1, right-1)
            return root
    def constructFromPrePost(self, preorder, postorder):
        self.preord_idx = 0
        self.postodr_map = {val:idx for idx, val in enumerate(postorder)}
        self.preorder = preorder
        self.postorder = postorder
        return self.make_tree(0, len(preorder)-1)
        