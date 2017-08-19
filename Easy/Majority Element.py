class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_dict = dict()
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                hash_dict[nums[i]] += 1
            else:
                hash_dict[nums[i]] = 1
        max_len = 1
        res = nums[0]
        # print hash_dict
        for x in hash_dict:
            if hash_dict[x] > max_len:
                max_len = hash_dict[x]
                res = x
        return res

    """
    fastest solution in java
#     """
# public class Solution {
#     public int majorityElement(int[] num) {
#
#         int major=num[0], count = 1;
#         for(int i=1; i<num.length;i++){
#             if(count==0){
#                 count++;
#                 major=num[i];
#             }else if(major==num[i]){
#                 count++;
#             }else count--;
#
#         }
#         return major;
#     }
# }