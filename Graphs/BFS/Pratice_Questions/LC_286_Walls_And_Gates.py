from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # find the gates
        row = len(rooms)
        col = len(rooms[0])
        q = deque()
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:  # If it's a gate
                    q.append((r, c))


        #once we find the gates, then do a bfs to using the gates in queue to modify 
        #the empty box in place

        while q:
            r,c= q.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
            for dx, dy in directions:
                new_x, new_y = r + dx, c + dy

                if 0 <= new_x < row and 0 <= new_y < col and rooms[new_x][new_y] == 2147483647:

                    rooms[new_x][new_y] = rooms[r][c] + 1

                    q.append((new_x,new_y))

                    






        