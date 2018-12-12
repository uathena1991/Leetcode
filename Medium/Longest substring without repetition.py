class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        dy_dict = dict()
        l,r = 0, 0
        longest = 1
        # dy_dict = 0
        while l <= r < len(s):
            if s[r] not in dy_dict or dy_dict[s[r]] < l:
                dy_dict[s[r]] = r
                r += 1
            else:
                # print(l,r, s[l:r])
                # print(dy_dict)
                if r - l > longest:
                    longest = r - l
                l = dy_dict[s[r]] + 1
                dy_dict[s[r]] = r
                r += 1
        if r - l > longest:
            longest = r - l
        # print(dy_dict)
        return longest


