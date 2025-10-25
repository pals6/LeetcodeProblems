# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''naive T/S O(n)/O(n)
        seen=set()
        if head is None:
            return False
        curr=head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr=curr.next
        return False'''
        #slow-fast approach O(n)/O(1)
        slow,fast=head,head
        if head is None:
            return False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False


