# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None)
        curr = res
        A, B = list1, list2
        while (A and B):
            if A.val < B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next
            curr = curr.next
        
        if A:
            curr.next = A
        elif B:
            curr.next = B
        
        return res.next