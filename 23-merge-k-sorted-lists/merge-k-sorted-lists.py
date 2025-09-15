# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap=[]
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val,node))
        dummy=ListNode(0)
        cur=dummy
        while heap:
            top_element, top_node=heapq.heappop(heap)
            cur.next=top_node
            cur=top_node
            if top_node.next:
                heapq.heappush(heap,(top_node.next.val,top_node.next))
        return dummy.next