# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = 0
        cur = head
        while cur:
            cur = cur.next
            num += 1
        m = num - (n-1)
        
        temp = ListNode(0)
        temp.next = head
        prev = temp
        count = 1
        while count < m:
            prev = prev.next
            count += 1
        nxt = prev.next.next
        prev.next = nxt
        return temp.next


        
        



        