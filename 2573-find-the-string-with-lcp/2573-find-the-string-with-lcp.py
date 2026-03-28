class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)
        
        # Step 1: Basic validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
        
        # Step 2: DSU
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        # Step 3: Assign characters
        group_to_char = {}
        res = [''] * n
        current_char = 'a'
        
        for i in range(n):
            root = find(i)
            if root not in group_to_char:
                if current_char > 'z':
                    return ""  # more than 26 groups
                group_to_char[root] = current_char
                current_char = chr(ord(current_char) + 1)
            res[i] = group_to_char[root]
        
        word = ''.join(res)
        
        # Step 4: Verify LCP
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0
        
        if dp == lcp:
            return word
        return ""