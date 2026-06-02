# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next  
            curr.next = prev       
            prev = curr            
            curr = next_node       
        return prev
    
    def isPalindrome(self, head):
        lst =[]
        while head:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]