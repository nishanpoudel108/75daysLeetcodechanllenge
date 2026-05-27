class Solution(object):
    def findJudge(self, n, trust):
        
        # indegree[i] = how many people trust i
        # outdegree[i] = how many people i trusts
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        # Judge trusts nobody and everyone trusts judge
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        
        return -1