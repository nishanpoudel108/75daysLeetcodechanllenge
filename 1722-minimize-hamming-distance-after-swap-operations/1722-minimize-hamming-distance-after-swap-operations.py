from collections import defaultdict, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        
        # Step 1: DSU (Union-Find)
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        # Step 2: Build components
        for a, b in allowedSwaps:
            union(a, b)

        # Step 3: Group indices by root
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)

        # Step 4: Calculate minimum Hamming distance
        hamming = 0

        for indices in groups.values():
            count = Counter()
            
            # count values in source
            for i in indices:
                count[source[i]] += 1
            
            # match with target
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    hamming += 1

        return hamming