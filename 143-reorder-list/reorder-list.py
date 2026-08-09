# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack=[]
        cur=head
        while cur:
            stack.append(cur)
            cur=cur.next
        start=0
        end=len(stack)-1
        while start<end:
            stack[start].next=stack[end]
            start+=1
            if start==end:
                break
            stack[end].next=stack[start]
            end-=1
        stack[end].next=None
        