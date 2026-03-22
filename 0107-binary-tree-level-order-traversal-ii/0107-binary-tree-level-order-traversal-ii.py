# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return[]
        ans = []
        que=[]
        que.append(root)
        while que:
            len_q = len(que)
            ans.insert(0, [])
            for _ in range(len_q):
                node = que.pop(0)# first in first out
                ans[0].append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        return ans