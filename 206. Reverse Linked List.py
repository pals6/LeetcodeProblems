# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        while (cur!=None):
            temp=cur.next #store current node's next reference
            cur.next=prev #reverse the current pointer to previous node
            prev=cur #previous node will now be the current node
            cur=temp #current will now be the last assigned next node
        return prev #return the new head (which was tail before reversing)
