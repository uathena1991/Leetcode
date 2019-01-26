class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def count_chars(ss):
            if not ss:
                return []
            if len(ss) == 1:
                return [(ss[0], "1")]
            idx, cts, curr = 1, 1, ss[0]
            res = []
            while idx < len(ss):
                if ss[idx] == curr:
                    cts += 1
                    idx += 1
                else:
                    res.append((curr, str(cts)))
                    curr, cts = ss[idx], 1
                    idx += 1
            res.append((curr, str(cts)))
            return res


        def decode(counts):
            res = ""
            for c, cts in counts:
                res += cts + c

            return str(res)


        dp = ['' for i in range(n+1)]
        dp[1] = '1'
        for i in range(2, n+1):
            cts = count_chars(dp[i-1])
            dp[i] = decode(cts)

        # print(dp)
        return dp[-1]

