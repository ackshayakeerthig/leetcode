# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth_end=None
        cur=head
        for i in range(n):
            if not cur:
                return []
            cur=cur.next
        prev=None
        nth_end=head
        while cur:
            prev=nth_end
            nth_end=nth_end.next
            cur=cur.next
        if prev:
            prev.next=nth_end.next
        else:
            return nth_end.next
        return head