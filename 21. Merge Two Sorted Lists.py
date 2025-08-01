# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode() #create an empty node, val=0, next=None
        tail=dummy #merged linked list tail 
        while list1 and list2: # compare and attach smaller node to tail
            if list1.val<list2.val:
                tail.next=list1 
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        tail.next=list1 or list2 #after the loop ends, attach one of the two lists that might still have nodes left
        return dummy.next
