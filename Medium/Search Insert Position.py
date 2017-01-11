"""
test case:
[1,3,5] 2
[1] 0,1,2
[1,4,5,6],5.5,4.5
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
	        return 0
        l_idx = 0
        h_idx = len(nums)-1
        while l_idx<=h_idx:
            m_idx = (l_idx+h_idx)/2
            if nums[m_idx] == target:
                return m_idx
            elif nums[m_idx] < target: # target falls within (m_idx,h_idx]
                l_idx = m_idx+1
                if l_idx >= len(nums):
                    return len(nums)
                elif nums[l_idx] > target:
                    return l_idx
            else:# target falls within [l_idx,m_idx)
                h_idx = m_idx-1
                if h_idx < 0:
                    return 0
                elif nums[h_idx] < target:
                    return h_idx+1









a = Solution()
print a.searchInsert([1,3,4,5,6,7],0.5)
print a.searchInsert([1,3,4,5,6,7],1.5)
print a.searchInsert([1,3,4,5,6,7],2.5)
print a.searchInsert([1,3,4,5,6,7],3.5)
print a.searchInsert([1,3,4,5,6,7],4.5)
print a.searchInsert([1,3,4,5,6,7],5.5)
print a.searchInsert([1,3,4,5,6,7],6.5)