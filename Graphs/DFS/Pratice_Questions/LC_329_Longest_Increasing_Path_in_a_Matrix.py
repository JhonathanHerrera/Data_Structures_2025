from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        memo = {}
        def dfs(r,c):
            if (r, c) in memo:
                return memo[(r, c)]

            direction = [[1,0],[0,1],[-1,0],[0,-1]]
            max_path = 1 
            for x, y in direction:
                new_x = r + x
                new_y = c + y
                
                if 0 <= new_x < ROW and 0 <= new_y < COL and matrix[new_x][new_y] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(new_x, new_y))
            memo[(r, c)] = max_path
            return memo[(r, c)]

        longest_path = 0
        for r in range(ROW):
            for c in range(COL):
                longest_path = max(longest_path, dfs(r, c))

        return longest_path
        