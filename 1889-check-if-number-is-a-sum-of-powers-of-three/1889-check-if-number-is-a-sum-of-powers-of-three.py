class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def power(n):
            while n>0:
                rem=n%3
                if rem==2:
                    break
                n//=3
            return n==0
        return power(n)