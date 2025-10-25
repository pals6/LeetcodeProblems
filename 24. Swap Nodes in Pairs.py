# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        prev=dummy
        dummy.next=head
        while prev.next and prev.next.next:
            a=prev.next
            b=a.next
            prev.next=b
            a.next=b.next
            b.next=a
            prev=a
            
        return dummy.next
#Space/Time O(1)-dummy node/O(n) going through the list and O(1) for pointer swap
