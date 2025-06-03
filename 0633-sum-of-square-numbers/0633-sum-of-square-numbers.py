class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**0.5)+1
        while a<=b:
            res=a**2 + b**2
            if res==c:
                return True
            if res < c:
                a+=1
            else:
                b-=1
        return False