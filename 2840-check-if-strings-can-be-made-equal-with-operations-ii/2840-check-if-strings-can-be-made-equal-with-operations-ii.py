class Solution(object):
    def checkStrings(self, s1, s2):
        # Extract even and odd indexed characters
        s1_even = sorted(s1[::2])
        s1_odd = sorted(s1[1::2])
        
        s2_even = sorted(s2[::2])
        s2_odd = sorted(s2[1::2])
        
        # Compare both parts
        return s1_even == s2_even and s1_odd == s2_odd