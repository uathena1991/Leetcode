class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if not nums:
            return []
        Len, Max, res = len(nums), nums[-1], set()
        for a in range(Len-3): # 1st
            if nums[a] + Max*3 < target:
                continue
            if 4* nums[a] > target:
                break
            if a > 0 and nums[a] == nums[a-1]:
                continue

            for b in range(a+1, Len - 2): # 2nd
                if nums[a] + nums[b] + Max*2 < target:
                    continue
                if 2*(nums[a] + nums[b]) > target:
                    break
                if b > a+1 and nums[b] == nums[b-1]:
                    continue

                sum2 = target - nums[a] - nums[b]
                i3, i4 = b + 1, Len - 1
                while i3 < i4:
                    aa = nums[i3] + nums[i4]
                    if aa == sum2:
                        res.add((nums[a], nums[b], nums[i3], nums[i4]))
                        i3 += 1
                        i4 -= 1
                    elif aa < sum2:
                        i3 += 1
                    else:
                        i4 -= 1
        return [list(x) for x in res]








