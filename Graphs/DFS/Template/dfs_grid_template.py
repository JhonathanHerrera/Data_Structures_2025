class Solution:
    def dfs_grid(self, r, c, grid, visited):
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(x, y):
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS or 
                (x,y) in visited or grid[x][y] == "0"):
                return

            visited.add((x, y))

            for dx, dy in directions:
                dfs(x + dx, y + dy)

        dfs(r, c)
