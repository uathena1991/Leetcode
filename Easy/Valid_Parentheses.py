class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        idx = 0
        if len(s)%2 != 0:
            return False
        while len(s) > 0 and idx < len(s) and idx >= 0:
            if s[idx] not in [')',']','}']:
                idx += 1
            else:
                if idx == 0 or (s[idx] == ')' and s[idx-1] != '(') or (s[idx] == '}' and s[idx-1] != '{') or (s[idx] == ']' and s[idx-1] != '['):
                    return False
                else:
                    s = s[:idx-1] + s[idx+1:]
                    idx -= 1                
        if len(s) > 0 and idx >= len(s):
            return False
        else:
            return True




# stack
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in [')',']','}']:
                if stack:
                    curr = stack.pop()
                else:
                    return False
                if (curr + c) not in ['[]', '{}', '()']:
                    return False
            else:
                return False

        if not stack:
            return True
        else:
            return False
