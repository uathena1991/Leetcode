from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        def generate_next_wordList(curr, wordList):
            letters = 'abcdefghijklmnopqrstuvwxyz'
            res = set()
            for w in curr:
                for li in range(len(w)):
                    new_w = wordList & set([w[:li] + x + w[li+1:] for x in letters])
                    [res.add(x) for x in new_w]
            return res

                    

        start, end = {beginWord}, {endWord}
        visited = set()
        length = 0
        while start:
            wordList = wordList - start
            start = generate_next_wordList(start, wordList)
            length += 1
            if start & end:
                return length + 1
            if len(start) > len(end):
                start, end = end, start


        return 0


