# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next  
            curr.next = prev       
            prev = curr            
            curr = next_node       
        return prev
    '''def isPalindrome(self, head):
        fast = slow = head
        values = []
        if not head.next:return True
        while fast and fast.next:
            fast = fast.next.next
            values.append(slow.val)
            slow = slow.next
        print(values)
        if slow.
        while slow:
            val = values.pop()
            print(val)
            if val != slow.val :
                return False
            slow = slow.next
        return True if len(values)==0 else False
    '''
    '''def isPalindrome(self, head):
        fast = slow = head
        if not head.next:return True
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        second_half = slow.next
        slow.next = None
        
        first_half = self.reverseList(head)
        print(second_half)
        print(first_half)
        return first_half == second_half'''    
    def isPalindrome(self, head):
        fast = slow = head
        values = []
        if not head.next:return True
        while fast and fast.next:
            fast = fast.next.next
            values.append(slow.val)
            slow = slow.next
        first_half = values[::-1]
        second_half = []
        while slow:
            second_half.append(slow.val)
            slow = slow.next
        if first_half == second_half:
            return True
        second_half.pop(0)
        if first_half == second_half:
            return True
        else:return False