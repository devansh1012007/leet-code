# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# EASY

class Solution(object):
    def __init__(self):
        self.ans=[]
    def postorderTraversal(self, root):
        if root is None:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.ans.append(root.val)
        return self.ans