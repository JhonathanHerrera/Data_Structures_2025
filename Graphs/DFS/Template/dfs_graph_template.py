class Solution:
    def dfs_graph(self, start, graph):

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(start)
        return visited
