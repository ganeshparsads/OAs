class TrieNode:
    def __init__(self):
        self.char = ["" for i in range(26)]
        self.wordEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                curr.char[ord(i) - 97] = TrieNode()
            curr = curr.char[ord(i) - 97]

        curr.wordEnd = True

    def search(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                return False
            curr = curr.char[ord(i) - 97]

        return curr.wordEnd


    def startsWith(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                return False
            curr = curr.char[ord(i) - 97]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)