# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getdistance(self,left):
        slow,fast = left, left
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        
        second = slow.next
        slow.next = None
        return second
    def Merge(self,left,right):
        if not left:
            return right
        if not right:
            return left
        if left.val < right.val:
            left.next = self.Merge(left.next, right)
            return left
        else:
            right.next = self.Merge(left, right.next)
            return right
    def sortList(self, head):
        # v will use merge sort 
        # this was a learning session for me 
        if not head or not head.next:
            return head
        
        second = self.getdistance(head)
        # actuall this if is not neede as v are already metigating all the possibilities in the if above
        #if head != second:
        head = self.sortList(head)
        second = self.sortList(second)
        return self.Merge(head,second)