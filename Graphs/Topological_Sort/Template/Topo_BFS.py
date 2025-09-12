from collections import defaultdict, deque

class Solution:
    def topoSort_BFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * numCourses


        for dest, srt in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        
        q = deque([ i for i in range(numCourses) if indegree[i] == 0])

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            while q:
                node = q.popleft()
                topo.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

        return topo if len(topo) == numCourses else []
        