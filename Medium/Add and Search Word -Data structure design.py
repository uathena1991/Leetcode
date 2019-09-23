class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'.': dict()}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root['.']
        for w in word:
            if w not in curr:
                curr[w] = dict()
            curr = curr[w]
        curr['-1'] = True # word or not



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(cw, c_node):
            if not cw:
                return True if '-1' in c_node else False
            if cw[0] == '.':
                return any([dfs(cw[1:], c_node[x]) for x in c_node if x != '-1'])
            elif cw[0] in c_node:
                return dfs(cw[1:], c_node[cw[0]])
            else:
                return False
        curr = self.root['.']

        return dfs(word, curr)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)