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
        memo = {}
        def dfs(head):
            if not head:
                return None
        
            if head in memo:
                return memo[head]

            node = Node(head.val)
            memo[head] = node
            node.next = dfs(head.next)
            node.random = dfs(head.random)

            return node
        
        return dfs(head)

        
        
