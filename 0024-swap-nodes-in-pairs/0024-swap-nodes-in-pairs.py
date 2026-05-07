# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# input(head); if head or head.next is None, return None; a = head.next ; head.next = recursive call (head.next.next);a.next = head; return a

# 1ST try baby !!!

class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None :
            return head
        a = head.next
        # method 1
        #a.next = self.swapPairs(head.next.next)
        #head.next = self.swapPairs(head.next.next) # <-- another way
        #a.next = head
        # method 2
        head.next, a.next = self.swapPairs(head.next.next), head # <-- another way
        
        return a
        