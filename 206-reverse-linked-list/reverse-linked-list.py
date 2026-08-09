# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        cur_node,prev_node,next_node=head,None,head.next
        while cur_node!=None:
            next_node=cur_node.next
            cur_node.next=prev_node
            prev_node=cur_node
            cur_node=next_node
        return prev_node
        