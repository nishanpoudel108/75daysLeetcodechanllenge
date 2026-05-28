class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1
        self.best_length = float('inf')


class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # Update best candidate for a node
        def update(node, length, index):
            if (length < node.best_length or
               (length == node.best_length and index < node.best_index)):
                node.best_length = length
                node.best_index = index

        # Insert reversed words into trie
        for i, word in enumerate(wordsContainer):
            rev = word[::-1]
            node = root

            update(node, len(word), i)

            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                update(node, len(word), i)

        ans = []

        # Query longest common suffix
        for word in wordsQuery:
            rev = word[::-1]
            node = root

            for ch in rev:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best_index)

        return ans