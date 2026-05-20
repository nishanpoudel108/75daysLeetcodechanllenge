class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        seenA = set()
        seenB = set()
        result = []
        
        common = 0
        
        for i in range(len(A)):
            # Add current elements
            seenA.add(A[i])
            seenB.add(B[i])
            
            # If A[i] already appeared in B
            if A[i] in seenB:
                common += 1
            
            # If B[i] already appeared in A
            # Avoid double count when A[i] == B[i]
            if B[i] in seenA and A[i] != B[i]:
                common += 1
            
            result.append(common)
        
        return result