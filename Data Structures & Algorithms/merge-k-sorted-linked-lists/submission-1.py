# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []

        dummy = ListNode(0,None)
        p = dummy

        for i, node in enumerate(lists):
            #[[]]
            if node:
            #heap里面比较的是大小，所以用node.val; node节点不能比较大小；
            #因为pop出来要知道是在哪个node，所以要同时存入node;防止两个node的大小一样，又去比较node所以用i
                heapq.heappush(minheap,(node.val,i,node))
        
        while minheap:
            val, i, node = heapq.heappop(minheap)
            #p.next连接的是节点node，不能连接数值
            p.next = node
            p = p.next

            #需要判断是否已经为None，才能用next性质
            if node.next:
                heapq.heappush(minheap,(node.next.val,i,node.next))
        
        return dummy.next
        

            
        