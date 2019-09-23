import heapq as hq
from collections import defaultdict
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort all dots, and record heights, left (+), right(-)
        spoints = []
        for l,r,h in buildings:
            spoints.append((l, h))
            spoints.append((r, -h))
        hq.heapify(spoints)
        # max_heap, record current max heights
        ch = [0]
        res = defaultdict(int)   # dict: in case same x has multiple starts/ends
        while spoints:
            i,h = hq.heappop(spoints)
            if h > 0: # left
                if h > -ch[0]:
                    res[i] = max(h, res[i])
                hq.heappush(ch, -h)
            else: # right
                ch.remove(h)
                hq.heapify(ch)
                if -h > -ch[0]:
                    res[i] = -ch[0] if res[i] == 0 else min(-ch[0], res[i])

        res_list = [[-1,-1]]
        for x in res:
            if res[x] != res_list[-1][1]:
                res_list.append([x, res[x]])


        return res_list[1:]
