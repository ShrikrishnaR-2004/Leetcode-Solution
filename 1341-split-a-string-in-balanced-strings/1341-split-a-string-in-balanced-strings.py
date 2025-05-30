class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal=0
        count=0
        for char in s:
            if char =="R":
                bal+=1
            else:
                bal-=1
            if bal==0:
                count+=1
        return count