class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word):

        def dfs(i, node):
            # reached end of word
            if i == len(word):
                return node.isEnd

            ch = word[i]

            # case 1: normal character
            if ch != '.':
                if ch not in node.children:
                    return False
                return dfs(i + 1, node.children[ch])

            # case 2: wildcard '.'
            for child in node.children.values():
                if dfs(i + 1, child):
                    return True

            return False

        return dfs(0, self.root)