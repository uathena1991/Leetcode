class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort the list
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums)-1
            while j < k:
                curr_sum = nums[i]+nums[j]+nums[k]
                if curr_sum < target:
                    j+=1
                elif curr_sum > target:
                    k-=1
                else:
                    return curr_sum
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum

        return res
            


a = Solution()
print(a.threeSumClosest([0,1,2],0))