class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        res=0
        left=0
        right=n-1
        left_max=height[left]
        right_max=height[right]
        while left < right:
            if left_max<right_max:
                res+=left_max-height[left]
                left+=1
                left_max=max(left_max,height[left])
            else:
                res+=right_max-height[right]
                right-=1
                right_max=max(right_max,height[right])

        return res