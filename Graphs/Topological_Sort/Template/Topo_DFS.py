from collections import defaultdict
from typing import List

class Solution:
    def topoSort_DFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)

        visited = {}   # 0=unvisited, 1=visiting, 2=visited
        topo = []
        self.valid = True

        def dfs(node):
            if not self.valid:
                return
            if node in visited:
                if visited[node] == 1:  # cycle detected
                    self.valid = False
                return

            visited[node] = 1  # visiting
            for nei in graph[node]:
                dfs(nei)
            visited[node] = 2  # visited
            topo.append(node)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)

        return topo[::-1] if self.valid else []
