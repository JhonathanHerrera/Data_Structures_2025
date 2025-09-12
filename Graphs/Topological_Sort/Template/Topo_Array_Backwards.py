from collections import defaultdict

def topo_sort(N, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * N
    ordering = [0] * N
    i = N - 1  # start from the last index

    def dfs(at, i):
        visited[at] = True
        for nei in graph[at]:
            if not visited[nei]:
                i = dfs(nei, i)
        ordering[i] = at
        return i - 1

    for at in range(N):
        if not visited[at]:
            i = dfs(at, i)

    return ordering
