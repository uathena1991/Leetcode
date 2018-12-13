class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) == 1:
            return [-1]
        if len(nums2) == 0:
            return []
        from collections import defaultdict
        check_dict = defaultdict(int)
        check_dict[nums2[-1]] = -1
        destack = [nums2[0]]
        # print(destack, check_dict)

        for i,n in enumerate(nums2[1:]):
            if len(destack) == 0 or n <= destack[-1]:
                destack.append(n)
            else:
                while len(destack) > 0:
                    if destack[-1] < n:
                        check_dict[destack.pop()] = n
                    else:
                        break
                destack.append(n)
            # print(n, destack, check_dict)

        res = []
        print(check_dict)
        print(destack)
        for n in nums1:
            res.append(check_dict[n] if n in check_dict else -1)
        return res




