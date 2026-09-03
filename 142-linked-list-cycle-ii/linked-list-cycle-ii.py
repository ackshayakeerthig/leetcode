# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while True:
            if slow==None or fast==None or fast.next==None:
                return None
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        slow=head
        pos=0
        while slow!=fast:
            slow=slow.next
            fast=fast.next
            pos+=1
        return slow