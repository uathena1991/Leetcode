from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isword = False

def buildTrie(words):
    root = TrieNode()
    for w in words:
        curr = root
        for c in w:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.isword = True
    return root


class Solution:
    def dfsTrie(self, r, c, board, curr_node, path):
        curr_c = board[r][c]
        if curr_c not in curr_node.child:
            return
        if curr_node.child[curr_c].isword:
            tt = ''.join(path + [curr_c])
            if tt not in self.res:
                self.res.append(tt)
                curr_node.child[curr_c].isword = False
        board[r][c] = '-1'
        for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < self.lenr and 0 <= nc < self.lenc and board[nr][nc] != '-1':
                self.dfsTrie(nr, nc, board, curr_node.child[curr_c], path + [curr_c])
        board[r][c] = curr_c


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.lenr, self.lenc = len(board), len(board[0])
        if self.lenr * self.lenc == 0 or len(words) == 0:
            return []
        self.res = []
        root = buildTrie(set(words))
        for r in range(self.lenr):
            for c in range(self.lenc):
                self.dfsTrie(r, c, board, root, [])

        return self.res

