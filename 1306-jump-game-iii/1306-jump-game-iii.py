class Solution(object):
    def canReach(self, arr, start):
    
        visited = set()

        def dfs(i):
            # Out of bounds or already visited
            if i < 0 or i >= len(arr) or i in visited:
                return False

            # Found index with value 0
            if arr[i] == 0:
                return True

            visited.add(i)

            # Try both directions
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)