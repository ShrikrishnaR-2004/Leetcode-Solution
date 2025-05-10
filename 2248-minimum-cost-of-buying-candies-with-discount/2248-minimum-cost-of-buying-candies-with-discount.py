class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        nums=sorted(cost,reverse=True)
        cost_all=sum(nums)
        return cost_all-sum(nums[2::3])