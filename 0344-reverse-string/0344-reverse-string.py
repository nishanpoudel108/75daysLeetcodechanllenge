class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            # swap characters
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1