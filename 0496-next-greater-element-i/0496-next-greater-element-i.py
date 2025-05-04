class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num1 in nums1:
            try:
                index_in_nums2 = nums2.index(num1)
                next_greater = -1
                for j in range(index_in_nums2 + 1, len(nums2)):
                    if nums2[j] > num1:
                        next_greater = nums2[j]
                        break
                result.append(next_greater)
            except ValueError:
                result.append(-1)  
        return result