# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midlle
        #left, right : left, reverse right
        #inset right to left one by one
        
        if not head: return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow
        cur = slow.next
        mid.next = None
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        right = prev
        left = head

        while right:
            right_nxt = right.next
            left_nxt = left.next
            right.next = left.next
            left.next = right
            right = right_nxt
            left = left_nxt
