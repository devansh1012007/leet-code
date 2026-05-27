# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution(object):
    def removeElements(self, head, val):
        curr = head
        while curr:
            if curr.val == val: 
                if curr.next:
                    curr.val = curr.next.val
                    curr.next= curr.next.next 
                else: 
                    curr = None
                    return head
            curr = curr.next
        return head
'''
class Solution(object):
    def removeElements(self, head, val):
        final = ListNode()
        curr = final
        if not head:return final.next 
        while True:
            curr.next = head
            while head and head.val != val: curr, head = curr.next, head.next
            
            if head: head = head.next
            else: return final.next