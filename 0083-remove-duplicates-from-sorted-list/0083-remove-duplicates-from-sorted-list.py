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
            while curr.val == head.val and head.next:
                head =head.next
            if head.val == curr.val:
                curr.next = None
                break    
            curr.next = head
            head = curr.next
        return ans 
