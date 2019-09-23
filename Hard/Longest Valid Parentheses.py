class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        left_locs = []
        curr_start, res = 0, 0
        for i,c in enumerate(s):
            if c == '(':
                left_locs.append(i)
            else: # ')'
                if not left_locs:
                    curr_start = i + 1
                    continue
                left_locs.pop()
                if not left_locs: # empty
                    res = max(res, i - curr_start + 1)
                else:  # not empty
                    res = max(res, i - left_locs[-1])
            
        return res
                    
                    
                