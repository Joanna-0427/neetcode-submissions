# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        if not list1 or not list2: return list1 or list2

        dummy = ListNode(0,None)
        p = dummy

        #不创建任何新节点，使用p把list1，list2重新按顺序串联起来；
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        p.next = list1 if list1 else list2

        return dummy.next

