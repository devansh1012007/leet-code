# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# how to solve : 
'''
        go to the end , count the nodes on the way 
        divide the value of k with no. of nodes ; take the remender 
        join the 1st and last node and then move the pointer counter-remainder number of times 
        return self.next as head and set self.next = None 
        '''
        # big fuck up --> i am think rotation == pointer movemenst
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        counter = 1
        if curr == None: return None
        while curr.next: 
            counter += 1 
            curr = curr.next
        curr.next = head
        #print(counter)
        if counter>k:
            k = counter-k
            #print(k)
            while k > 1:
                head=head.next
                k -= 1
            #print(curr.val, head)
            curr = head.next
            head.next = None
            return curr
        else: 
            k = counter - (k%counter) 
            #print(k)
            while k > 1:
                head=head.next
                k -= 1
            #print(curr.val, head)
            curr = head.next
            head.next = None
            return curr
        #remainder=counter-remainder
        print(remainder)
        