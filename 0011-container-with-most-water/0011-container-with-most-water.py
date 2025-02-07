class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_area=0
        area=0
        while i < j:
            area= min(height[i], height[j]) * (j - i)
            max_area = max(area,max_area )
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return max_area