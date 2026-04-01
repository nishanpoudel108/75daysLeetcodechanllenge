class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        # sort by position
        robots.sort()
        
        stack = []  # store indices of robots
        
        for robot in robots:
            pos, health, dirc, idx = robot
            
            if dirc == 'R':
                stack.append(robot)
            else:
                # collision with previous R robots
                while stack and stack[-1][2] == 'R' and health > 0:
                    prev = stack[-1]
                    
                    if prev[1] < health:
                        # R dies
                        stack.pop()
                        health -= 1
                    elif prev[1] > health:
                        # L dies
                        prev[1] -= 1
                        health = 0
                    else:
                        # both die
                        stack.pop()
                        health = 0
                        break
                
                if health > 0:
                    stack.append([pos, health, dirc, idx])
        
        # collect survivors
        stack.sort(key=lambda x: x[3])  # sort by original index
        
        return [robot[1] for robot in stack]