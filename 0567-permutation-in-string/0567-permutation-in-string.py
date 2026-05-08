class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 26 lowercase letters
        count1 = [0] * 26
        count2 = [0] * 26

        # Fill frequency for s1 and first window of s2
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # Check first window
        if count1 == count2:
            return True

        # Sliding window
        for i in range(len(s1), len(s2)):
            # Add new character
            count2[ord(s2[i]) - ord('a')] += 1
            
            # Remove old character
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Compare frequency arrays
            if count1 == count2:
                return True

        return False
        