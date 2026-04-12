class Solution(object):
    def minimumDistance(self, word):
        def dist(a, b):
            if a == -1:
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        dp = [0] * 26  # dp[j] = max saving if second finger at j
        res = 0
        
        for i in range(n - 1):
            cur = ord(word[i]) - ord('A')
            nxt = ord(word[i + 1]) - ord('A')
            
            d = dist(cur, nxt)
            
            for j in range(26):
                dp[cur] = max(dp[cur], dp[j] + d - dist(j, nxt))
            
            res += d
        
        return res - max(dp)