from collections import deque, defaultdict

class Solution(object):
    def minJumps(self, arr):
        
        n = len(arr)

        if n == 1:
            return 0

        # Store indices for each value
        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        q = deque([(0, 0)])  # (index, steps)
        visited = set([0])

        while q:
            idx, steps = q.popleft()

            # Reached last index
            if idx == n - 1:
                return steps

            neighbors = graph[arr[idx]] + [idx - 1, idx + 1]

            for nei in neighbors:
                if 0 <= nei < n and nei not in visited:
                    visited.add(nei)
                    q.append((nei, steps + 1))

            # Clear to avoid repeated processing
            graph[arr[idx]] = []