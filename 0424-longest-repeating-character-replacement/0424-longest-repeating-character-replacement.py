class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        maxFreq = 0
        result = 0

        for right in range(len(s)):
            # add current character
            count[s[right]] = count.get(s[right], 0) + 1
            
            # update max frequency in window
            maxFreq = max(maxFreq, count[s[right]])
            
            # if window is invalid, shrink it
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            # update result
            result = max(result, right - left + 1)
        
        return result