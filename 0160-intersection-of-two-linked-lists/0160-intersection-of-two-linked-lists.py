# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''class Solution(object):
    def getIntersectionNode(self, headA, headB):
        mem_dict = {}
        pos = 0
        while headA:
            mem_dict[id(headA)] = pos
            pos += 1
            headA = headA.next
        key = mem_dict.keys()
        while headB:
            if id(headB) in key: return headB
            else:headB = headB.next
        return None
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        A=headA
        B=headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A