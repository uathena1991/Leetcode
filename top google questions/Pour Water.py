class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """

        heights = [float('inf')] + heights + [float('inf')]
        m = len(heights)
        if V == 0:
                return
        K += 1
        while V > 0:
            if heights[K] < heights[K-1] and heights[K] < heights[K+1]:
                heights[K] += 1
            else:
                # search left
                idx, min_loc = K - 1, K
                while idx > 0:
                    if heights[idx] > heights[min_loc]:
                        break
                    if heights[idx] < heights[min_loc]:
                        min_loc = idx
                    idx -= 1
                if min_loc == K:
                    # even reach left, and no lower ground, or all higher,  so search right
                    idx = K + 1
                    while idx < m:
                        if heights[idx] > heights[min_loc]:
                            break
                        if heights[idx] < heights[min_loc]:
                            min_loc = idx
                        idx += 1
                heights[min_loc] += 1
            # print(heights)
            V -= 1
        return heights[1:-1]