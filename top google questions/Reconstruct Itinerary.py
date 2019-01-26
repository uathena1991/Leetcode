from collections import defaultdict
class Solution:


    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(curr_ap):
            if len(self.res) ==  len(tickets) + 1:
                return self.res

            dsts = sorted(graph[curr_ap])

            for n_ap in dsts:
                graph[curr_ap].remove(n_ap)
                self.res.append(n_ap)
                status = dfs(n_ap)
                if status:
                    return status

                self.res.pop()
                graph[curr_ap].append(n_ap)


        # create graph
        graph = defaultdict(list)
        for t in tickets:
            graph[t[0]].append(t[1])


        # go through graphs (dfs, check if dfs can go over all places)
        self.res = ["JFK"]
        return dfs("JFK")
        