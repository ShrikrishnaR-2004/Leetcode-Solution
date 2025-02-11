class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        for j in range(i,len(nums)):
            nums[j]=0