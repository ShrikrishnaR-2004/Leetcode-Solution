class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=int(num**0.5)
        return n**2==num