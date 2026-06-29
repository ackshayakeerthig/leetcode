# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curodd=head
        # cureve=head.next if head!=None else return head
        if  head==None or head.next==None:
            return head
        cureve=head.next
        head=cureve
        prevodd=None
        preveve=None
        # while curodd!=None or curodd.next!=None:
        while curodd!=None:
            if curodd.next==None:
                return head
            cureve=curodd.next
            prevodd=curodd
            preveve=cureve
            curodd=preveve.next
            if curodd==None:
                cureve=None
            else:
                cureve=curodd.next

            # // swapping prevs
            preveve.next=prevodd
            prevodd.next=cureve if cureve!=None else curodd

        return head