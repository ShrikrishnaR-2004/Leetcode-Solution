class Solution:
    def minimumSum(self, num: int) -> int:
        n=sorted(str(num))
        return (int(n[0] + n[-1])+ (int(n[1]+n[2])))
