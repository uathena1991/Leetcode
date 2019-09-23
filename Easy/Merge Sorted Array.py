class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l1, l2 = m-1, n-1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[l1 + l2+1] = nums2[l2]
                l2 -= 1
            else:
                nums1[l1 + l2+1] = nums1[l1]
                l1 -= 1

        if l2 >= 0:
            nums1[:l2+1] = nums2[:l2+1]