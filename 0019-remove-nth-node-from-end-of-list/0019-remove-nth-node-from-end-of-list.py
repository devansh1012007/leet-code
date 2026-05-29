# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr=head
        second=first=curr
        for _ in range(n):
            first = first.next
        if not first:return second.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head  