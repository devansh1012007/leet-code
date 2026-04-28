# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and tail
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next

        # Step 2: Make it circular
        curr.next = head

        # Step 3: Find new head (length - k steps from start)
        k %= length
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        # Step 4: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
