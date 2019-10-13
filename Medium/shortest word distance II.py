class WordDistance:

    def __init__(self, words: List[str]):
        self.hash = dict()
        for i, w in enumerate(words):
            if w not in self.hash:
                self.hash[w] = [i]
            else:
                self.hash[w].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        return min([abs(x - y) for x in self.hash[word1] for y in self.hash[word2]])


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)