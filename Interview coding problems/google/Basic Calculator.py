class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int

        recursion
        """
        def recursion(start):
            res, curr_n, sign = 0, 0, 1
            while start < len(s):
                curr = s[start]
                if curr.isdigit():
                    curr_n = curr_n * 10 + int(curr)
                elif curr == '+' or curr == '-':
                    res += sign*curr_n
                    sign = 1 if curr == '+' else -1
                    curr_n = 0
                elif curr == '(':
                    tmp, start = recursion(start + 1)
                    res = res + sign*tmp
                    sign, curr_n = 1, 0
                elif curr == ')':
                    if curr_n:
                        res += sign * curr_n
                    return res, start
                start += 1
            if curr_n != 0:
                res += sign * curr_n
            return res, start



        return recursion(0)[0]



class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int

        using stack
        """
        stack = [0, '+']
        idx, sign = 0, 1
        while idx < len(s):
            curr = s[idx]
            if curr.isdigit():
                tmp = int(curr)
                idx += 1
                while idx < len(s) and s[idx].isdigit():
                    tmp = tmp*10 + int(s[idx])
                    idx += 1
                idx -= 1
                sign = 1 if stack.pop() == '+' else -1
                stack[-1] += tmp * sign
            elif curr == '+' or curr == '-':
                stack.append(curr)
            elif curr == '(':
                stack.append(0)
                stack.append('+')

            elif curr == ')':
                tmp = stack.pop()
                sign = 1 if stack.pop() == '+' else -1
                stack[-1] += tmp * sign
            idx += 1
        return stack[0]

