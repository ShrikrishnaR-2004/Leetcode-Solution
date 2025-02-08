class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=n*(n+1)/2
        sum_nums=sum(nums)
        miss_no=sum1-sum_nums
        return int(miss_no)
