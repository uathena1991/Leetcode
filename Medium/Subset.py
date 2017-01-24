# class Solution(object):
#     def recursive_f(self,nums,res):
#         if not nums:
#             res.append([])
#             return res
#         else:
#             prev_step = self.recursive_f(nums[:-1],res)
#             for t in prev_step:
#                 res.append(t+[nums[-1]])
#             return res
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         return self.recursive_f(nums,res)

class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for idx in range(len(nums)):
            tmp = len(res)
            # res.append([nums[idx]])
            for i in range(tmp):
                res.append(res[i]+[nums[idx]])
        return res

a = Solution()
print a.subsets([1,3,2])