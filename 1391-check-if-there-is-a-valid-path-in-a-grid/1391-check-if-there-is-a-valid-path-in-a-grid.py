class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        from collections import deque
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while q:
            x, y = q.popleft()
            
            # reached destination
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    
                    # check reverse connection
                    for rdx, rdy in dirs[grid[nx][ny]]:
                        if nx + rdx == x and ny + rdy == y:
                            visited.add((nx, ny))
                            q.append((nx, ny))
                            break
        
        return False