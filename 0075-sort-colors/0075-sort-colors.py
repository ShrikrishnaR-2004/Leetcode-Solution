class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1=[]
        for i in nums:
            if i == 0:
                nums1.append(i)
        for i in nums:
            if i == 1:
                nums1.append(i)
        for i in nums:
            if i == 2:
                nums1.append(i)
        nums[:]=nums1