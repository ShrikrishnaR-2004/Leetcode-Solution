class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if n < k or k < 1:
            return 0 
        min_difference = float('inf')
        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            current_difference = subarray[-1] - subarray[0]
            min_difference = min(min_difference, current_difference)

        return min_difference
