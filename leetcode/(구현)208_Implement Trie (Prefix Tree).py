from collections import defaultdict


class TrieNode:
    def __init__(self, finish=False):
        self.finish = finish
        self.child = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.child[char]
        node.finish = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.finish

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]
        return True
