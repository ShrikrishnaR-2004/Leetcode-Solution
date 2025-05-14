class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=""
        for i in s:
            num+=str(ord(i)-ord('a')+1)
        
        while k>0:
            temp=0
            for i in num:
                temp+=int(i)
            num=str(temp)
            k-=1
            print(num)
        
        return int(num)