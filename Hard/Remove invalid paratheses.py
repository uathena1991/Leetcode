class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = {s.replace('(', '').replace(')', '')}
        self.len_s = len(s)
        self.lcounts = s.count('(')
        self.rcounts = s.count(')')
        self.min_del = self.lcounts +self.rcounts # del all

        def backtracking(Lrem, Rrem, lcts, rcts, del_counts, sidx, curr_path):
            if lcts < rcts or del_counts > self.min_del:
                # print('fail')
                return
            if sidx == len(s):
                if Lrem == Rrem: # end
                    # print("success", Lrem, Rrem, lcts, rcts, sidx, curr_path, del_counts, self.min_del)
                    if del_counts == self.min_del and curr_path not in self.res:
                        self.res.add(curr_path)
                    elif del_counts < self.min_del:
                        self.res = {curr_path}
                        self.min_del = del_counts
                return

            elif s[sidx] == "(":
                # keep
                backtracking(Lrem, Rrem, lcts + 1, rcts, del_counts, sidx + 1, curr_path + s[sidx])
                # del
                if Lrem > 0:
                    backtracking(Lrem - 1, Rrem, lcts, rcts, del_counts+1 ,sidx + 1, curr_path)
            elif s[sidx] == ')':
                # keep
                backtracking(Lrem, Rrem, lcts, rcts + 1, del_counts, sidx + 1, curr_path + s[sidx])
                # del
                if Rrem > 0:
                    backtracking(Lrem, Rrem-1, lcts, rcts, del_counts+1, sidx + 1, curr_path)
            else: # string
                backtracking(Lrem, Rrem, lcts, rcts, del_counts, sidx + 1, curr_path + s[sidx])

        backtracking(self.lcounts, self.rcounts, 0, 0,0, 0, '')
        return [x for x in self.res]


"""
Optimized
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        cleft, cright = 0, 0
        for c in s:
            if c == '(':
                cleft += 1
            elif c == ')':
                cleft -= 1
                if cleft < 0:
                    cleft = 0
                    cright += 1
        res = set()
        def backtracking(cidx, unmatched, left, right, path):
            for idx in range(cidx, len(s)):
                if s[idx] == '(' and left > 0:
                    backtracking(idx + 1, unmatched, left - 1, right, path) # del
                elif s[idx] == ')' and right > 0:
                    backtracking(idx+1, unmatched, left, right - 1, path) # del

                path += s[idx] # keep (, ), or letters
                if s[idx] == '(':
                    unmatched += 1
                elif s[idx] == ')':
                    unmatched -= 1
                    if unmatched < 0:
                        break
            if left == 0 == right and unmatched == 0:
                res.add(path)


        backtracking(0, 0, cleft, cright, '')
        return [x for x in res]

