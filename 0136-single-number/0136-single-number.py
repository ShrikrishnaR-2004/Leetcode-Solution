from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        counter=Counter(nums)
        for key,value in counter.items():
            if value==1:
                return key

