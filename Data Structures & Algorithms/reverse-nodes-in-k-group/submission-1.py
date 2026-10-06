# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        
        cnt = count // k
        if cnt < 1: return head

        prev = dummy
        cur = head
        for _ in range(cnt):
            for _ in range(k-1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            prev = cur
            cur = cur.next
        return dummy.next



            
