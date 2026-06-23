"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoMap = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldtoMap[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldtoMap[cur]
            copy.next = oldtoMap[cur.next]
            copy.random = oldtoMap[cur.random]
            cur = cur.next
        
        return oldtoMap[head]
