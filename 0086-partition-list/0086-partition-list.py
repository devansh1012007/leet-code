# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        l1 = ListNode()
        link_list1 = l1
        l2 = ListNode()
        link_list2=l2
        while head :
            if head.val <x:
                link_list1.next = head
                link_list1 = link_list1.next
            else:
                link_list2.next = head
                link_list2 = link_list2.next
            head = head.next
        link_list1.next = l2.next
        link_list2.next=None
        return l1.next
        # my 1st try: 
        '''
        l1 = None
        l2 = None
        while head:
            if head.val <3:
                if l1:
                    l1.next = head
                else: 
                    l1 = head
                    start1 = ListNode()
                    start1.next = l1
            else:
                if l2:
                    l2.next = head
                else: 
                    l2 = head
                    start2 = ListNode()
                    start2.next = l2
            head = head.next
        l1.next = start2.next
        l2.next =None
        return start1.next'''