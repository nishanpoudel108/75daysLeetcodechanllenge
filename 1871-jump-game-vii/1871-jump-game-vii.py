class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        
        # Number of reachable indices in current window
        pre = 0
        
        for i in range(1, n):
            
            # Add left side of window
            if i - minJump >= 0 and reachable[i - minJump]:
                pre += 1
            
            # Remove indices outside window
            if i - maxJump - 1 >= 0 and reachable[i - maxJump - 1]:
                pre -= 1
            
            # Current position is reachable
            if s[i] == '0' and pre > 0:
                reachable[i] = True
        
        return reachable[-1]