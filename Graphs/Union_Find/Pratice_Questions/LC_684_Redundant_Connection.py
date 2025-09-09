from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [i for i in range(len(edges)+1)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
            
        def union(x,y):
            x_parent,y_parent = find(x), find(y)
            if x_parent != y_parent:
                parents[y_parent] = x_parent
                return True
            return False
        
        for x,y in edges:
            if not union(x,y):
                return [x,y]
        
      