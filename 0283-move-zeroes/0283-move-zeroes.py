class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while i<len(nums):
            if nums[i]==0:
                count+=1
                nums.pop(i)
            else:
                i+=1
        nums.extend([0]*count)
                