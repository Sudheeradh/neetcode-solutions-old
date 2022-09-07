# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if (lists == None) or (len(lists) == 0):
            return None
        while(len(lists) > 1):
            mergedLists = []
            for i in range(0, len(lists), 2):
                A = lists[i]
                B = lists[i + 1] if ((i + 1) < len(lists)) else None
                mergedLists.append(self.merge2Lists(A, B))
            lists = mergedLists
        
        return lists[0]
        
    def merge2Lists(self, A, B):
        dummy = ListNode()
        curr = dummy
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
        if B:
            curr.next = B
        
        return dummy.next
                    
            