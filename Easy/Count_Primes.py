class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        prime_pool = [True] * n
        prime_pool[0] = prime_pool[1] = False
        i = 2
        while i*i <= n:
            if prime_pool[i]:
                prime_pool[i*i:n:i] = [False] * len(prime_pool[i*i:n:i])
            i += 1
        return sum(prime_pool)