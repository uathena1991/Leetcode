class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        def num2list(num):
            if num < 10:
                return [str(num)]
            res = []
            while num > 0:
                res.append(str(num%10))
                num //=10
            return res[::-1]

        if len(chars) <= 1:
            return len(chars)
        new_idx, old_idx = 0, 0
        while old_idx < len(chars):
            curr = chars[old_idx]
            cts = 0
            while old_idx < len(chars) and chars[old_idx] == curr :
                old_idx += 1
                cts += 1
            # replace
            chars[new_idx] = curr
            new_idx += 1
            if cts > 1:
                for tmp in num2list(cts):
                    chars[new_idx] = tmp
                    new_idx += 1
            # print(chars)
        # print(chars)
        return new_idx

