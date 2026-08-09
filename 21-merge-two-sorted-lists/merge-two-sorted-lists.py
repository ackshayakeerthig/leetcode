# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start=None
        prev_node=None
        while list1 and list2:
            cur_node=ListNode()
            if start==None:
                start=cur_node
            if list1.val>list2.val:
                cur_node.val=list2.val
                list2=list2.next
                
            else:
                cur_node.val=list1.val
                list1=list1.next
            if prev_node:
                prev_node.next=cur_node
            prev_node=cur_node
        if list1:
            if prev_node:
                prev_node.next=list1
            else:
                return list1
        elif list2:
            if prev_node:
                prev_node.next=list2
            else:
                return list2
        return start
