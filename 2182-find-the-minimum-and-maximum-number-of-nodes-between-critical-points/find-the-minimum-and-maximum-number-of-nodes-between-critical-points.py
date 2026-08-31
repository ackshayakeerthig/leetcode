# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance=float('inf')
        maxDistance=float('-inf')
        flag=False
        prev_critical=None
        first_critical=None
        prev=head
        if not head:
            return [-1,-1]
        cur=head.next
        cnt=2
        while cur.next!=None:
            if prev.val<cur.val and cur.next.val<cur.val or prev.val>cur.val and cur.next.val>cur.val:
                if prev_critical:
                    flag=True
                    # maxDistance=max(maxDistance,cnt-prev_critical)
                    minDistance=min(minDistance,cnt-prev_critical)
                else:
                    first_critical=cnt
                prev_critical=cnt
            prev=cur
            cur=cur.next
            cnt+=1
        if not flag :
            return [-1,-1]
        if first_critical!=prev_critical:
            maxDistance=prev_critical-first_critical

        return [minDistance,maxDistance]