class Solution(object):
    def lengthOfLIS(self, nums):
        """
        DP
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        dp = [1 for _ in nums]
        longest = 1
        for i in range(1, len(nums)):
            tmp_len = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp_len = max(tmp_len, dp[j])
            dp[i] = tmp_len + 1
            longest = max(longest, dp[i])
        return longest

    def lengthOfLIS_dp_binary_search(self, nums):
	    """
	    including binary search, figure it out in future...
	    :param nums:
	    :return:
	    """