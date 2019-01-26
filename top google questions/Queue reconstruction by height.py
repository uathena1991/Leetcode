class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) <= 1:
            return people
        sorted_stack =  sorted(people, key = lambda x: (x[0], -x[1]))
        heightest = sorted_stack[-1][0]
        # res = sorted([[x,y] for x,y in sorted_stack if x == heightest])
        res = []
        # while sorted_stack[-1][0] == heightest:
            # sorted_stack.pop()

        while sorted_stack:
            cppl, mct = sorted_stack.pop()
            # cidx, cts = 0, 0
            # while cts < mct:
            #     if res[cidx][0] >= cppl:
            #         cts += 1
            #     cidx += 1
            res.insert(mct, [cppl, mct])
            # print(res)
        return res
