# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        flag=False
        while fast!=None :
            if flag:
                slow=slow.next
            flag= not flag
            fast=fast.next
            if fast==slow:
                return True
        return False

        