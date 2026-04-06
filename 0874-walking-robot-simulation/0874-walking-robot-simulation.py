class Solution(object):
    def robotSim(self, commands, obstacles):
        # Convert obstacles to set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Directions: North, East, South, West
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        direction = 0  # start facing North
        
        x = y = 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:  # turn right
                direction = (direction + 1) % 4
            elif cmd == -2:  # turn left
                direction = (direction + 3) % 4
            else:
                dx, dy = dirs[direction]
                
                for _ in range(cmd):  # move step by step
                    if (x + dx, y + dy) in obstacle_set:
                        break  # stop if obstacle
                    
                    x += dx
                    y += dy
                    
                    # update max distance squared
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist