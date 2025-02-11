from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=Counter(nums)
        n=len(nums)
        for i in x.keys():
            if x[i]>n//2:
                return i
