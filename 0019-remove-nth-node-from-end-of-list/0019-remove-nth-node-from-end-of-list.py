# ways of doing it :
# reverse --> remove --> reverse
# covert to list --> edit list --> make a new LL
# covert only the last n+1 to list --> edit list --> make a new LL --> attach it to exiting LL
# use 2 pointer at a sepration 'n' steps --> move then by 1 unit till the fisrt pointer reaches the end --> remove the node in front of second pointer --> return the head

# imp point if 2nd pointer node is None; return second pointer.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr=head
        second=first=curr
        for _ in range(n):
            first = first.next
        if not first:return second.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head  