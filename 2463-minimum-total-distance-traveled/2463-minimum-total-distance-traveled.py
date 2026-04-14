class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        positions = []
        for pos, limit in factory:
            positions.extend([pos] * limit)
        
        memo = {}
        
        def dp(i, j):
            if i == len(robot):
                return 0
            if j == len(positions):
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dp(i, j + 1)
            res = min(res, abs(robot[i] - positions[j]) + dp(i + 1, j + 1))
            
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)