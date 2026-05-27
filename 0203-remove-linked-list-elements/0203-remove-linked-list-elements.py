# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution(object):
    def removeElements(self, head, val):
        curr = head
        while curr:
            if curr.val == val: 
                if curr.next:
                    curr.val = curr.next.val
                    curr.next= curr.next.next 
                    curr = curr.next
                else: 
                    curr = None
                    return head
        return head'''
class Solution(object):
    def removeElements(self, head, val):
        final = ListNode()
        curr = final
        while head:
            if head.val != val: 
                curr.next = head
                curr = curr.next
            else:
                curr.next = None
            head = head.next
        return final.next