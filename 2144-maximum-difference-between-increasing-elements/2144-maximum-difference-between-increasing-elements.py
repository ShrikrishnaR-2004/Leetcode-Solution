class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    res=nums[j]-nums[i]
                    ans=max(ans,res)
        return ans