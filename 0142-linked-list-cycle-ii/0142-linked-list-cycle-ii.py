# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#  This was a learning experinece 
class Solution(object):
    def detectCycle(self, head):
        s = f = head
        while f and f.next:
            s,f =s.next, f.next.next
            if s == f:break
        else: return None
        while head != s:
            s = s.next
            head = head.next
        return head