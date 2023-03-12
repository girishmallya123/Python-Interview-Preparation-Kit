class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if not (c in curr.children):
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            if not (c in curr.children):
                return False
            curr = curr.children[c]
        
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:
            if not (c in curr.children):
                return False
            curr = curr.children[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)