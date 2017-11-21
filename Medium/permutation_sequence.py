# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s) < 1 or s == ' ':
#             return ''
#         s_list = ''
#         curr_word = ''
#         pre_word = s[-1]
#         for i in range(len(s)-1, -1, -1):
#             if s[i] == ' ' and pre_word == ' ':
#                 pre_word = s[i]
#                 continue
#             if s[i] == ' ':
#                 s_list += str(curr_word[::-1])
#                 s_list += ' '
#                 curr_word = ''
#             else:
#                 curr_word += str(s[i])
#             print curr_word
#             pre_word = s[i]
#         if s[0] != ' ':
#             s_list += str(curr_word[::-1])
#         while len(s_list) > 0 and s_list[0] == ' ':
#             s_list = s_list[1:]
#         while len(s_list) > 0 and s_list[-1] == ' ':
#             s_list = s_list[:-1]
#         # print curr_word
#         return s_list

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])

a = Solution()
print a.reverseWords(" abc def ghi  jkl ")