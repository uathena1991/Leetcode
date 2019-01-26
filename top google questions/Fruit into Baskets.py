from collections import OrderedDict
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
            return 0
        mlen = 1
        start, end, pool = 0, 0, OrderedDict({tree[0]:0}) # record last appearance of each index
        while start <= end < len(tree) - 1:
            # print(start, end, pool)
            while len(pool) <= 2 and end < len(tree) - 1:
                end += 1
                pool[tree[end]] = end
            if end == len(tree) - 1 and len(pool) <= 2:
                end += 1
            mlen = max(mlen, end - start)
            # print(pool, mlen, start, end)
            # pool.pop(tree[start])
            sort_keys = sorted(pool, key = lambda x: pool[x])
            start = pool[sort_keys[0]] + 1
            pool.pop(sort_keys[0])
            # print(start, end, sort_keys, pool, '\n')

        return mlen






from collections import Counter
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
            return 0
        mlen = 1
        start = 0
        counts = Counter()
        for end,fruit in enumerate(tree):
            counts[fruit] += 1
            while len(counts) >= 3:
                counts[tree[start]] -= 1
                if counts[tree[start]] == 0:
                    counts.pop(tree[start])
                start += 1

            mlen = max(mlen, end - start + 1)

        return mlen
