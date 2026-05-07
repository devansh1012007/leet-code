# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# input(head); if head or head.next is None, return None; a = head.next ; a.next = head; a.next.next = recursive call (head.next.next); return a
        
class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None :
            return head
        a = head.next
        head.next = self.swapPairs(head.next.next)
        a.next = head
        return a
        