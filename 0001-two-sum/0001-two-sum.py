class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map={}
        for count,ele in enumerate(nums):
            complement=target-ele
            if complement in h_map:
                return [h_map[complement],count]
            h_map[ele] = count
        return [] 