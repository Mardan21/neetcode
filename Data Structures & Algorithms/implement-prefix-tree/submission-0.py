class PrefixTree:

    def __init__(self):
        self.tree = []

    def insert(self, word: str) -> None:
        self.tree.append(word)
        return None

    def search(self, word: str) -> bool:
        for w in self.tree:
            if w == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for w in self.tree:
            wordSize, prefixSize = len(w), len(prefix)
            if prefixSize <= wordSize and w[:prefixSize] == prefix:
                return True
            else:
                continue
        return False

        
        