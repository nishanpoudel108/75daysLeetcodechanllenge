class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        word = ['?'] * (n + m - 1)
        locked = [False] * (n + m - 1)

        # Step 1: Apply 'T'
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                        locked[i + j] = True
                    else:
                        return ""

        # Step 2: Fill remaining with 'a'
        for i in range(len(word)):
            if word[i] == '?':
                word[i] = 'a'

        # Step 3: Fix 'F'
        for i in range(n):
            if str1[i] == 'F':
                match = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        match = False
                        break

                if match:
                    changed = False
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        if not locked[idx]:  # only modify free positions
                            for c in 'abcdefghijklmnopqrstuvwxyz':
                                if c != str2[j]:
                                    word[idx] = c
                                    changed = True
                                    break
                        if changed:
                            break

                    if not changed:
                        return ""

        return "".join(word)
        