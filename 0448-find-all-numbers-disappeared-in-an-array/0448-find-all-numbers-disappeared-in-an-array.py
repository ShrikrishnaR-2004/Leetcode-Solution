class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        missing_no=[]
        nums1=set(nums)
        print(nums1)
        for i in range (1,n+1):
            if i not in nums1:
                missing_no.append(i)
        return missing_no