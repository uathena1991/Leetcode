"""
1. put index of '(' in a stack
2. record each index of ')', if stack is empty, new_start
3. Note: curr_length
Test cases: "()(()", "(()"
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_list = 0
        idx = 0
        tmp_list = []
        tmp_start = -1
        while idx < len(s):
            if s[idx] == '(':
                tmp_list.append(idx)
                idx += 1
            else:
                if not tmp_list:
                    tmp_start = idx
                else:
                    tmp_list.pop()
                    if not tmp_list:
                        len_list = max(len_list,idx-tmp_start)
                    else:
                        len_list = max(len_list,idx-tmp_list[-1])

                idx += 1
        return (len_list)


        
a = Solution()
print a.longestValidParentheses("())()(())")
