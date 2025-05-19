class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        print(indexed_nums)
        indexed_nums.sort(reverse=True)
        top_k = indexed_nums[:k]
        print(top_k)
        top_k.sort(key=lambda x: x[1])
        print(top_k)
        result = [num for num, _ in top_k]
        return result
