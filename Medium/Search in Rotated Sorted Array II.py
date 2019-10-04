class Solution:
    def search(self, nums, target):
        lenn = len(nums)
        if lenn == 0:
            return False
        l, h = 0, lenn - 1
        while l <= h:
            while l < h and nums[l] == nums[h]:
                l += 1

            m = (l + h)//2
            if target == nums[m]:
                return True
            if nums[l] <= nums[m] <= nums[h]: # normal sorted array
                if target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1

            elif nums[m] >= nums[h]: # rotation on the right of nums[m]
                if nums[l] <= target <= nums[m]: # on the left side
                    h = m - 1
                else:
                    l = m + 1
            else: # nums[l] >= nums[m] and nums[h] <= nums[l]
                if nums[m] <= target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        return False


n = [2,5,6,0,0,1,2]
for t in n:
    print(t)
    print(Solution().search(n, t))
    print(Solution().search(n, t+0.5))