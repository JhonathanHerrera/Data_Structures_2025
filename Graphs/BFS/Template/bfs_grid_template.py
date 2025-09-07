from collections import deque

class Solutions:
    def bfs_grid(self, start, target, grid):

        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque([start])
        visited = set([start])
        steps = 0

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                if (x, y) == target:
                    return steps

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            steps += 1
        return -1
