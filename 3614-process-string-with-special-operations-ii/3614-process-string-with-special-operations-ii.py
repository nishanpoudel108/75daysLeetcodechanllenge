class Solution(object):
    def processStr(self, s, k):
        lengths = []
        cur = 0

        # Forward pass: store lengths
        for ch in s:
            if 'a' <= ch <= 'z':
                cur += 1
            elif ch == '*':
                if cur > 0:
                    cur -= 1
            elif ch == '#':
                cur *= 2
            else:  # '%'
                pass

            lengths.append(cur)

        if k >= cur:
            return '.'

        # Backward pass
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            L = lengths[i]
            prevL = lengths[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':
                if k == prevL:
                    return ch

            elif ch == '*':
                # length increased by 1 when going backward
                pass

            elif ch == '#':
                if k >= prevL:
                    k -= prevL

            else:  # '%'
                k = L - 1 - k

        return '.'