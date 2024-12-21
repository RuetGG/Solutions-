class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1Pointer = 0 
        nums2Pointer = 0 
        size =  len(nums1) - m  
        while nums1Pointer < m + n and nums2Pointer < n:
            if (nums1[nums1Pointer] > nums2[nums2Pointer]):
                nums1.insert(nums1Pointer, nums2[nums2Pointer])
                nums1.pop()
                nums2Pointer += 1
                nums1Pointer += 1
                size -= 1
            else:
                nums1Pointer += 1
        nums1Pointer -= (size )

        while size > 0:
            nums1[nums1Pointer] = nums2[nums2Pointer]
            nums1Pointer += 1
            nums2Pointer += 1
            size-=1
        return nums1 
