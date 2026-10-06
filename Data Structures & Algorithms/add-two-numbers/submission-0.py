# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0,None)
        p = dummy

        while l1 or l2 or carry:
            if l1 and l2:
                q, re = divmod(l1.val + l2.val + carry,10)
                node = ListNode(re)
                p.next = node
                p = p.next
                carry = q
                l1 = l1.next
                l2 = l2.next
            elif l1:
                q, re = divmod(l1.val + carry,10)
                node = ListNode(re)
                p.next = node
                p = p.next
                carry = q
                l1 = l1.next
            elif l2:
                q, re = divmod(l2.val + carry,10)
                node = ListNode(re)
                p.next = node
                p = p.next
                carry = q
                l2 = l2.next
            elif carry:
                node = ListNode(carry)
                p.next = node
                p = p.next
                carry = 0
            
        return dummy.next



