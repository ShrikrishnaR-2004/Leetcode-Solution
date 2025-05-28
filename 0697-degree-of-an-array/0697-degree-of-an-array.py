from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n1 = Counter(nums)
        max_freq = max(n1.values())

        max_freq_nums = [num for num, freq in n1.items() if freq == max_freq]

        min_length = float('inf')

        for num in max_freq_nums:
            first_occurrence = nums.index(num)
            last_occurrence = -1
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == num:
                    last_occurrence = i
                    break

            current_length = last_occurrence - first_occurrence + 1
            min_length = min(min_length, current_length)

        return min_length