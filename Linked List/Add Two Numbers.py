# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        carry = 0
        curr = res
        while(l1 or l2 or carry):
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            curr.next = ListNode(sum % 10)
            carry = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        return res.next
            
            