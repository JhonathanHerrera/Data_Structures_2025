from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        def dfs(i):
            if visited[i]:
                return 
            visited[i] = True
            for j in range(n):
                if not visited[j] and isConnected[i][j] == 1:
                    dfs(j)
            

        n = len(isConnected)
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        
        return res

        