from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls, lt = len(s), len(t)
        ct_t = Counter(t)
        if ls == 0 or lt == 0:
            return ''
        if s == t:
            return s
        ct_window = Counter()
        start, end, res = 0, 0, (float('inf'), None, None)
        satisf, required = 0, len(ct_t)
        while end < ls:
            if s[end] in ct_t:
                ct_window[s[end]] += 1
                if ct_window[s[end]] == ct_t[s[end]]:
                    satisf += 1
                if satisf == required:
                    # shrink the window
                    while start <= end and satisf == required:
                        if s[start] in ct_t:
                            ct_window[s[start]] -= 1
                            if ct_window[s[start]] < ct_t[s[start]]:
                                satisf -= 1
                        start += 1
                    if res[0] > end - start + 2:
                        res = (end-start+2, start-1, end)
            end += 1


        return s[res[1]:res[2]+1] if res[0] < float('inf') else ''

