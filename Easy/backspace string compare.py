class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def helper(ss, sign = "#"):
            # two pointers and scan from end
            skip = 0
            ns = ''
            for i in range(len(ss)-1, -1, -1):
                if ss[i] == sign:
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    ns += ss[i]
            # print(ns)
            return ns

        return helper(S) == helper(T)

