"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None
        q = deque([node])
        mapping ={node : Node(node.val,[])}
        while q:
            n =q.popleft()
            for i in n.neighbors:
                if i not in mapping:
                    mapping[i] = Node(i.val,[])
                    q.append(i)
                mapping[n].neighbors.append(mapping[i])
        return mapping[node]