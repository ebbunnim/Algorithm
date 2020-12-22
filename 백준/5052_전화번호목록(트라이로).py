from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word=False
        self.child=defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,target):
        node = self.root
        for char in target:
            node=node.child[char]
        node.word=True

    def search(self,target):
        node = self.root
        # 만약에 word를 순회하는 중간 과정에서 word flag가 true인 부분이 있으면 false return
        for char in target:
            if char not in node.child:
                return False
            if node.word==True:
                return False
            node = node.child[char]
        return node.word # hello 가 들어있는데 he까지만 가도 FOR문은 그대로 나오므로 완전한 단어인지 체크

for T in range(int(input())):
    l = int(input())
    words = [input() for _ in range(l)]
    words.sort()
    trie = Trie()
    flag = 0
    for word in words:
        trie.insert(word)
        if not trie.search(word):
            flag=1
            break
    if flag==0:
        print('YES')
    else:
        print('NO')
