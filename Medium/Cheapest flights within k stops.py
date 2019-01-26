class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        cost = [float('inf')] * n # shortest path from any node to dst
        # create graph as graph[u]
        graph = defaultdict(dict)
        for fl in flights:
            graph[fl[0]][fl[1]] = fl[2] ## Assume there is only one flight from src to dst

        # bfs
        queue = [(0, src, K+1)] # curr cost, curr_dst, curr most transfers
        while queue:
            curr_cost, curr_dst, K = queue.pop(0)
            if K > 0:
                for new_dst in graph[curr_dst]:
                    tnew_cost = curr_cost + graph[curr_dst][new_dst]
                    if tnew_cost < cost[new_dst]:
                        cost[new_dst] = min(tnew_cost, cost[new_dst])
                        queue.append((tnew_cost, new_dst, K - 1))
        if cost[dst] == float('inf'):
            return -1
        return cost[dst]









