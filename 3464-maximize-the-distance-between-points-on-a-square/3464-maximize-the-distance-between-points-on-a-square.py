import bisect

class Solution(object):
    def maxDistance(self, side, points, k):
        
        def getPos(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y
        
        arr = sorted(getPos(x, y) for x, y in points)
        n = len(arr)
        perimeter = 4 * side
        
        arr2 = arr + [x + perimeter for x in arr]
        
        def can(d):
            for i in range(n):
                count = 1
                first = arr2[i]
                prev = first
                
                for _ in range(1, k):
                    target = prev + d
                    j = bisect.bisect_left(arr2, target)
                    
                    if j >= i + n:
                        break
                    
                    prev = arr2[j]
                    count += 1
                
                if count >= k:
                    # ✅ critical fix: check circular gap
                    if prev - first <= perimeter - d:
                        return True
            
            return False
        
        left, right = 0, 2 * side
        
        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1
        
        return left