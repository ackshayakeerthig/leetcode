"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited={}
        def clone(oldvertex):
            if oldvertex  in visited:
                return visited[oldvertex]
            newvertex=Node(oldvertex.val)
            visited[oldvertex]=newvertex
            for child in oldvertex.neighbors:
                newvertex.neighbors.append(clone(child))
            return newvertex

        return clone(node)
        

