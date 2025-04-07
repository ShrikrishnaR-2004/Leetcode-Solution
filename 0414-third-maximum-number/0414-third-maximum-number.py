from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = sorted(list(set(nums)), reverse=True)
        num_distinct = len(distinct_nums)

        if num_distinct >= 3:
            return distinct_nums[2]
        else:
            return distinct_nums[0]