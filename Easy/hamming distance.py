class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def dig_2_bits(x):
            res = []
            while x > 0:
                res.append(x%2)
                x //= 2
            return res[::-1]
        large, small = max(x,y), min(x,y)
        bl = dig_2_bits(large)
        bs = dig_2_bits(small)
        if len(bl) > len(bs):
            bs = [0] * (len(bl) - len(bs)) + bs
        # print(bl, bs)
        return sum([x != y for x,y in zip(bl, bs)])