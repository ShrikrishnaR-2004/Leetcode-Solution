import math 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for b in range (int(sqrt(c))+1):
            a=sqrt(c-(b*b))
            if a==int(a):
                return True
        return False