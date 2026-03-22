# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        postodr_map = {val:idx for idx, val in enumerate(postorder)}
        self.preord_idx = 0
        def make_tree(left, right):
            if left>right:
                return None
            root = TreeNode(preorder[self.preord_idx])
            self.preord_idx += 1
            if left == right:
                return root
            mid = postodr_map[preorder[self.preord_idx]]
            root.left = make_tree(left, mid)
            root.right = make_tree(mid + 1, right-1)
            return root
        return make_tree(0, len(preorder)-1)