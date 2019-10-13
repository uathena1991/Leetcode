import heapq as hq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1, l2 = len(nums1), len(nums2)
        if k >= l1*l2:
            return [[x,y] for x in nums1 for y in nums2]
        prior = [(nums1[0] + nums2[0], (0, 0))]
        hq.heapify(prior)
        res = []
        visited = [[False for _ in nums2] for _ in nums1]
        while k > 0:
            csum, (i, j) = hq.heappop(prior)
            res.append([nums1[i],nums2[j]])
            k -= 1
            visited[i][j] = True
            if i + 1 < l1 and not visited[i+1][j]:
                hq.heappush(prior, (nums1[i+1] + nums2[j], (i+1, j)))
                visited[i+1][j] = True
            if j + 1 < l2 and not visited[i][j+1]:
                hq.heappush(prior, (nums1[i] + nums2[j+1], (i, j+1)))
                visited[i][j+1] = True
        return res
