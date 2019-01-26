"""
Recursion
"""
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def find_right_p(s,idx):
            lcts = 0
            while idx < len(s):
                if s[idx] == '[':
                    lcts += 1
                elif s[idx] == ']':
                    lcts -=1
                if lcts == 0:
                    return idx
                idx += 1


        curr, cts = '', ''
        idx = 0
        res = ''
        while idx < len(s):
            if s[idx].isdigit():
                curr = ''
                cts += s[idx]
                idx += 1
                # print("digit", curr, cts, idx)
            elif s[idx] == '[':
                end_idx =  find_right_p(s, idx)
                # print(s[idx+1:end_idx])
                curr = self.decodeString(s[idx+1:end_idx])
                # print("curr", curr, cts)
                res += curr * int(cts)
                cts, curr = '', ''
                idx = end_idx + 1
                # print("[]", curr, cts,idx)
            else:
                while idx < len(s) and not (s[idx].isdigit() or (s[idx] in '[]')):
                    curr += s[idx]
                    idx += 1
                if not cts:
                    cts = '1'
                # print('chars', curr, cts, idx)
                res += curr*int(cts)
                cts, cutt = '', ''
        return res


 """
 Stack
 """
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        stack, cts, t = [[1, ""]], '', 0
        while t < len(s):
            if s[t].isdigit():
                cts += s[t]
            elif s[t] == '[':
                stack.append([int(cts), ""])
                cts = ''
            elif s[t] == ']':
                num, cstr = stack.pop()
                stack[-1][1] += cstr*num
            else:
                stack[-1][1] += s[t]
                cts = ''
            t += 1
            # print(stack)


        return stack[-1][1] * stack[-1][0]