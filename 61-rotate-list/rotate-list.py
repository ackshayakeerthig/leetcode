# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0:
            return head
        if head==None:
            return None
        start=head
        listlen=1
        end=head
        while end and end.next:
            end=end.next
            listlen+=1
        end.next=start
        k%=listlen
        prev=end
        for i in range(listlen-k):
            prev=start
            start=start.next
        prev.next=None
        return start
