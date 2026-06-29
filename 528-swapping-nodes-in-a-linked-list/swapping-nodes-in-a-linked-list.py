# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # # finding kth end
        # cur=head
        # prev=None
        # kth_end=None
        # kth_start=None
        # for i in range(k):
        #     if cur!=None and cur.next!=None:
        #         prev=cur
        #         cur=cur.next
        #     else:
        #         break
        # kth_end=head.next
        # kth_start=prev
        # while cur!=None and cur.next!=None:
        #     kth_end=kth_end.next
        #     cur=cur.next
        # kth_end.val,kth_start.val=kth_start.val,kth_end.val
        # return head

        
        cur=head
        prev=None
        kth_end=None
        kth_start=None
        for i in range(k-1):
                prev=cur
                cur=cur.next
        kth_end=head
        kth_start=cur
        while cur!=None and cur.next!=None:
            kth_end=kth_end.next
            cur=cur.next
        kth_end.val,kth_start.val=kth_start.val,kth_end.val
        return head
        
        