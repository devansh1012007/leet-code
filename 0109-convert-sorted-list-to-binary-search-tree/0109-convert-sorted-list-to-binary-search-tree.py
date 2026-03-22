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

# this solution is slow af; 2 pointer method Beat me 99%; but this is memory efficient 
class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)
        prev, slow, fast = None, head, head 
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        prev.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root