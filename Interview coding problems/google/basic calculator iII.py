class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def next_digit(idx):
            res = ''
            while idx < len(s) and s[idx].isdigit():
                res += s[idx]
                idx += 1
            return int(res), idx -1 # return int, last digit

        def cal_in_parentheses(idx):
            stack = []
            while idx < len(s):
                curr = s[idx]
                if curr.isdigit():
                    tmp, idx = next_digit(idx)
                    stack.append(tmp)
                elif curr in {'+', '-'}:
                    stack.append(curr)
                elif curr in {'*', '/'}:
                    if s[idx+1].isdigit():
                        tmp, idx = next_digit(idx + 1)
                    elif s[idx+1] == '(': # '('
                        tmp, idx = cal_in_parentheses(idx+2)
                    else:
                        print('error!')
                    stack[-1] = stack[-1]*tmp if curr == '*' else stack[-1]//tmp
                elif curr == '(':
                    tmp, idx = cal_in_parentheses(idx+1)
                    stack.append(tmp)
                elif curr == ')':
                    # calculate all nums in stack and return
                    # print(stack)
                    res = stack.pop(0)
                    while stack: # +, -, digits
                        sign = 1 if stack.pop(0) == '+' else -1
                        curr = stack.pop(0)
                        res += sign * curr
                    return res, idx
                idx += 1
            # return

        if not s:
            return 0
        s = '(' + s + ')'
        s = s.replace(' ', '')
        total, final_idx = cal_in_parentheses(1)
        return total

