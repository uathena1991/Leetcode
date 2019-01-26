class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if len2 < len1:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        l, h, halflen = 0, len1, (len1 + len2 + 1)//2
        while l <= h:
            m1 = (l + h)//2
            m2 =  halflen - m1
            # print(m1, m2)
            if m1 > 0 and nums1[m1-1] > nums2[m2]:
                h = m1 - 1
            elif m1 < len1 and nums2[m2-1] > nums1[m1]:
                l = m1 + 1
            else:
                if m1 == 0:
                    maxLeft = nums2[m2-1]
                elif m2 == 0:
                    maxLeft = nums1[m1-1]
                else:
                    maxLeft = max(nums1[m1-1], nums2[m2-1])
                if (len1 + len2) % 2 == 1:
                    return maxLeft
                else:
                    if m1 == len1:
                        minRight = nums2[m2]
                    elif m2 == len2:
                        minRight = nums1[m1]
                    else:
                        minRight = min(nums2[m2], nums1[m1])
                    return (maxLeft + minRight) /2