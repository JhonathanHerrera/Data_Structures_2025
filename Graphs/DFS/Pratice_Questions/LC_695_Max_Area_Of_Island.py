from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row, col = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]  

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0 
            area = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    area += dfs(nr, nc)

            return area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
