class Solution(object):
    def numberOfSpecialChars(self, word):
        S = set(word)
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in S and ch.upper() in S:
                count += 1

        return count