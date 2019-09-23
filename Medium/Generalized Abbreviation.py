class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.res = []
        def recursion(word, abb, counts):
            if not word:
                self.res.append(abb + str(counts) if counts > 0 else abb)
            else:
                recursion(word[1:], abb, counts + 1) # del it
                recursion(word[1:], abb + str(counts) + word[0] if counts > 0 else abb + word[0], 0) # keep it

        recursion(word, '', 0)
        return self.res