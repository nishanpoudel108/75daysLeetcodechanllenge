class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution(object):
    def findWords(self, board, words):
        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        # DFS function
        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return

            nxt = node.children[ch]

            # Found a word
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None   # Avoid duplicates

            # Mark visited
            board[r][c] = "#"

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"):
                    dfs(nr, nc, nxt)

            # Restore cell
            board[r][c] = ch

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result