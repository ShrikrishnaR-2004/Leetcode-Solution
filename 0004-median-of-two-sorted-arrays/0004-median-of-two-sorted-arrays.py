class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        r=len(nums)
        if r %2 !=0:
            return nums[r//2]
        else:
            r=int(r)
            return (nums[r//2]+nums[r//2-1])/2
