class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = 0
        visited = set()

        def dfs(node):

            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
       
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)


        return res
        