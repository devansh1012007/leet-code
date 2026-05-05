# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        ans = head
        while head:
            curr = head
            while head and curr.val == head.val:
                head =head.next            
            curr.next = head
        return ans 
