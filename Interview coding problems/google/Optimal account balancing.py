from collections import defaultdict
class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        bal = defaultdict(int)
        for f,t, m  in transactions:
            bal[f] += m
            bal[t] -= m
        fil_bal = [bal[x] for x in bal if bal[x] != 0]
        # print(fil_bal, bal)
        res = len(fil_bal)
        def splits(fil_bal):
            queue = [([0], fil_bal[0])] # set of idexs, sum
            while queue:
                cset, csum = queue.pop(0)
                if csum == 0:
                    break
                for j in range(cset[-1] + 1, len(fil_bal)):
                    queue.append((cset+[j], csum + fil_bal[j]))
            fil_bal = [fil_bal[x] for x in range(len(fil_bal)) if x not in cset]
            return fil_bal

        while fil_bal:
            fil_bal = splits(fil_bal)
            res -= 1
        return res

