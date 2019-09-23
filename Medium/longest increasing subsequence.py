class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1 for _ in nums]
        for i in range(1, len(nums)):
            smaller_js = [dp[j] for j in range(i) if nums[j] < nums[i]]
            dp[i] = max(smaller_js) + 1 if smaller_js else 1
        return max(dp)


    def lengthOfLIS_dp_binary_search(self, nums):
        """
	    including binary search, figure it out in future...
	    :param nums:
	    :return:
	    ref: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
	    """
        tails = [0 for _ in nums]
        size = 0
        for n in nums:
            l, h = 0, size
            while l != h:
                m = (l + h) /2
                if n > tails[m]:
                    l = m + 1
                else:
                    h = m
            tails[l] = n
            size = max(size, l+1)

        return size
