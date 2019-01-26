"""
Brute-Force algorithm
"""
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def combine(x, c):
            return  ''.join(x) + c + ''.join([pools[i] for i in ''.join(x[::-1])])

        import itertools
        pools = {'0':'0', '1':'1', '8':'8','6':'9', '9':'6'}
        if n == 1:
            return ['0', '1', '8']
        if n == 0:
            return []

        res = [x for x in itertools.product(list(pools.keys()), repeat = n//2)]
        if n % 2 == 0:
            return sorted([combine(x, '') for x in res if x[0] != '0'])
        else:
            return sorted([combine(x, y) for y in ['1', '8', '0'] for x in res if x[0] != '0'])


"""
recursion 1

"""
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        evenpools = ["69", "96", "88", "11", "00"]
        singlepools = ["0", "1", "8"]
        if n == 1:
            return singlepools
        if n == 2:
            return evenpools[:-1]
        if n % 2 == 0:
            prev, middle = self.findStrobogrammatic(n-2), evenpools
        else:
            prev, middle = self.findStrobogrammatic(n-1), singlepools
        half_len = (n-1)//2
        # print(prev, middle, half_len)
        return [pr[:half_len] + c + pr[half_len:] for c in middle for pr in prev]


"""
Recursion 2
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recursive(n):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            prev = recursive(n-2)
            res = []
            for pr in prev:
                [res.append(x + pr + self.pools[x]) for x in self.pools]
            return res

        self.pools = {"0":'0','1':'1', '8':'8','6':'9', '9':'6'}
        res = []
        if n == 1:
            return ['0', '1', '8']
        if n == 0:
            return ['']
        p = recursive(n-2)
        for i in p:
            [res.append(x + i + self.pools[x]) for x in {'1':'1', '8':'8','6':'9', '9':'6'}]
        return sorted(res)
