from collections import defaultdict
class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.children = defaultdict(TrieNode)
            self.is_word=False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for l in word:
            curr = curr.children[l]
        curr.is_word = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for l in word:
            curr = curr.children.get(l)
            if curr is None:
                return False
        return curr.is_word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for l in prefix:
            curr = curr.children.get(l)
            if curr is None:
                return False
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)