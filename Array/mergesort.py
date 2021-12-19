class Solution(object):
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """
        *** BRUTE_FORCE_ALGORITHM_CODE
        """
#        i = 0
#        for i in range(n):
#            nums1[i+m] = nums2[i]
#        nums1.sort()
        """
        BRUTE_FORCE_ENDS
        """
        i = 0
        j = 0
        nums1copy = nums1[:m]

        for p in range(m + n):
            if(j >= n or (i < m and nums1copy[i] <= nums2[j])):
                nums1[p] = nums1copy[i]
                i += 1
            else:
                nums1[p] = nums2[j]
                j += 1
            print("i is %s, j is %d and p is %d" %(i,j,p))
        print(nums1)           



    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1,m,nums2,n)