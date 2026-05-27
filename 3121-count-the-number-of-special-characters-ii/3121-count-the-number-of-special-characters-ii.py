class Solution(object):
    def numberOfSpecialChars(self, word):
        last_lower = {}
        first_upper = {}
        
        # Store last position of lowercase letters
        # and first position of uppercase letters
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                lower = ch.lower()
                if lower not in first_upper:
                    first_upper[lower] = i
        
        count = 0
        
        # Check condition for each character
        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                count += 1
        
        return count