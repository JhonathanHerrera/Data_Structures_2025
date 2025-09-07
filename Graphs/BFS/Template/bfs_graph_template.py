from collections import deque, defaultdict

class Solution:
    def bfs_graph(self, start, target, edges, n):

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)   

        q = deque([start])
        visited = set([start])
        steps = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node == target:
                    return steps

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            
            steps += 1

        return -1
