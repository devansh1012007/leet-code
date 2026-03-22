# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        length = -1
        self.stk = []
        while head:
            length += 1
            self.stk.append(head.val)
            head = head.next
        def make_tree(left, right):
            if left == right: 
                mid = (left + right) // 2
                return TreeNode(self.stk[mid])
            elif left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(self.stk[mid])# ned to fix this logic    
            root.left = make_tree(left,mid - 1)
            root.right = make_tree(mid + 1, right)
            return root
        return make_tree(0 , length)